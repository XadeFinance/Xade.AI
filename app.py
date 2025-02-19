from flask import Flask, render_template, request, jsonify
from pipeline.agent import Agent, ChatOpenAI # Import Agent and ChatOpenAI
import langchain
import os
from langchain_openai import ChatOpenAI as LangchainChatOpenAI # Rename to avoid conflict
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import json
import urllib.parse
from os import getenv
from dotenv import load_dotenv
import re
import requests
import pipeline.fewshots
import pipeline.prompts
import pipeline.variables
from supabase import create_client, Client
import datetime
from celery_app import celery_app # Import celery_app for dynamic scheduling
from celery.schedules import crontab # Import crontab for dynamic scheduling
import data_cycle
from redbeat import RedBeatSchedulerEntry
from redbeat.schedules import rrule

app = Flask(__name__)

supabase_url: str = os.environ.get("SUPABASE_PROJECT_URL")
supabase_key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

MOBULA_DATA_FILE = "./pipeline/mobula-data.json"
LUNARCRUSH_DATA_FILE = "./pipeline/lunarcrush-data.json"


def load_local_data(provider):
    file_path = MOBULA_DATA_FILE if provider == "mobula" else LUNARCRUSH_DATA_FILE
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_local_data(provider, endpoint_data):
    file_path = MOBULA_DATA_FILE if provider == "mobula" else LUNARCRUSH_DATA_FILE
    with open(file_path, 'w') as f:
        json.dump(endpoint_data, f, indent=2)


@app.route('/agent/create', methods=['POST'])
def create_agent():
    try:
        load_dotenv()
        app.logger.info("Starting API request")

        app.logger.info(f"Request Headers: {dict(request.headers)}")
        app.logger.info(f"Request Data: {request.get_data()}")

        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        query = data.get('query')
        if not query:
            return jsonify({"error": "No query provided"}), 400

        character = data.get('character', 'Degen Analyst')
        agent_name = data.get('agent_name')
        if not agent_name:
            return jsonify({"error": "No agent name provided"}), 400

        user_id = data.get('user_id')

        agent_description = data.get('agent_description')

        image = data.get('image')

        chat_url = data.get('chat_url')

        app.logger.info(f"Processing query: {query} with character: {character}")

        # Fix model name typo and use imported ChatOpenAI
        llm = ChatOpenAI( # Use imported pipeline.agent.ChatOpenAI
            api_key=getenv("OPENAI_API_KEY"),
            model_name="gpt-4o", # Corrected model name
            verbose=False, # Set verbose to False for background tasks
            temperature=0
        )

        lunarcrush_endpoints = pipeline.variables.lunarcrush_endpoints
        mobula_endpoints = pipeline.variables.mobula_endpoints
        sectors = pipeline.variables.sectors
        blockchain_ids = pipeline.variables.blockchain_ids
        sorting_parameters = pipeline.variables.sorting_parameters
        avoid_tokens = pipeline.variables.avoid_tokens

        master_llm_system_template = pipeline.prompts.master_system_template
        master_llm_user_template = pipeline.prompts.master_human_template
        master_llm_fewshot = pipeline.fewshots.master_llm_fewshot

        data_agent_system_template = pipeline.prompts.data_system_template
        data_agent_user_template = pipeline.prompts.data_human_template
        data_agent_fewshot = pipeline.fewshots.data_fewshot
        data_agent_example_output = pipeline.variables.data_output_format

        data_guardrail_template = pipeline.prompts.data_guardrail_template
        analysis_system_template = pipeline.prompts.analysis_system_template
        analysis_user_template = pipeline.prompts.analysis_user_template
        response_template = pipeline.prompts.response_template
        tweet_template = pipeline.prompts.tweet_template

        app.logger.info("Creating agent")
        agent_instance = Agent( # Use imported pipeline.agent.Agent, rename to agent_instance to avoid shadowing
                    LLM=llm, query=query, character_description=character,
                    lunarcrush_endpoints=lunarcrush_endpoints, mobula_endpoints=mobula_endpoints,
                    sectors=sectors, blockchain_ids=blockchain_ids, sorting_parameters=sorting_parameters, avoid_tokens=avoid_tokens,
                    master_llm_system_template=master_llm_system_template, master_llm_user_template=master_llm_user_template, master_llm_fewshot=master_llm_fewshot,
                    data_agent_system_template=data_agent_system_template, data_agent_user_template=data_agent_user_template, data_agent_fewshot=data_agent_fewshot, data_agent_example_output=data_agent_example_output,
                    data_guardrail_template=data_guardrail_template, analysis_system_template=analysis_system_template, analysis_user_template=analysis_user_template,
                    response_template=response_template, tweet_template=tweet_template,
                    )

        master_output =  agent_instance.create_process()

        about_agent = master_output

        apis = agent_instance.create_apis(master_output)

        app.logger.info(apis)

        parent_call = agent_instance.execute_parent_calls(agent_instance.form_parent_calls(apis)) # Use agent_instance

        app.logger.info(parent_call)

        top_tokens = agent_instance.get_top_tokens(parent_call, top_n=5) # Use agent_instance

        app.logger.info(top_tokens)

        apis = agent_instance.update_api_calls(apis, top_tokens) # Use agent_instance

        app.logger.info(apis)

        agent_apis = apis # capture updated apis

        nested_call = agent_instance.execute_nested_calls(apis) # Use agent_instance

        analysis = agent_instance.get_analysis(top_tokens, nested_call, master_output) # Use agent_instance

        tweet = agent_instance.create_tweet(analysis) # Use agent_instance

        agent_status = "ACTIVE"

        lastrun = datetime.datetime.now(datetime.timezone.utc).isoformat()

        agent_data = {
            "agent_name": agent_name,
            "user_id": user_id,
            "agent_apis": agent_apis, # Use the updated agent_apis here
            "twitter": "NA",
            "description": agent_description,
            "query": query,
            "chat_url": chat_url,
            "image": image,
            "about_agent": about_agent, # Store about_agent here
            "agent_status": agent_status,
            "last_run": lastrun,
            "character": character,
        }

        response_agents = supabase.table('agents').insert(agent_data).execute()

        app.logger.info(response_agents)

        new_agent = response_agents.data[0]
        new_agent_id = new_agent['id']

        def extract_endpoints(api_config_list, endpoints_list):
            for api_config in api_config_list:
                if isinstance(api_config, dict) and "endpoint" in api_config:
                    endpoints_list.append(api_config["endpoint"])
                if isinstance(api_config, dict) and "nested_calls" in api_config and isinstance(api_config["nested_calls"], list):
                    extract_endpoints(api_config["nested_calls"], endpoints_list) # Recursive call


        all_endpoints_to_call = []
        extract_endpoints(agent_apis, all_endpoints_to_call)

        apis_to_call_inserts = []
        for endpoint in all_endpoints_to_call:
            apis_to_call_inserts.append({
                'agent_id': new_agent_id,
                'endpoint': endpoint
            })
        response_apis_to_call = supabase.table('apis_to_call').insert(apis_to_call_inserts).execute()

        app.logger.info(response_apis_to_call)

        terminal_object = {
            "agent_id": new_agent_id,
            "created_at": lastrun,
            "tweet_content": tweet, 
            "posted": "FALSE"
        }

        response_terminal = supabase.table('terminal').insert(terminal_object).execute()

        app.logger.info(response_terminal)

        # Dynamic Scheduling Logic - Add schedule for new agent
        created_agent_timestamp = datetime.datetime.fromisoformat(new_agent['created_at'])
        creation_minute = created_agent_timestamp.minute

        app.logger.info(type(creation_minute))

        task_name = f'process-agent-task-agent-{new_agent_id}' # Unique task name
        interval = crontab(minute=f"{creation_minute}")

        entry = RedBeatSchedulerEntry(task_name, "data_cycle.process_agent_task", interval, args=[new_agent_id], app=celery_app)
        entry.save()
        app.logger.info(f"Dynamic schedule added for agent ID: {new_agent_id}, to run at minute: {creation_minute} of every hour.")


        from data_cycle import process_agent_task
        process_agent_task.delay(agent_id=new_agent_id) # Run immediately


        return jsonify(tweet), 200 # Return tweet content, not just "tweet" string


    except json.JSONDecodeError as e:
        app.logger.error(f"JSON decode error: {str(e)}")
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    if not os.path.exists(MOBULA_DATA_FILE):
        with open(MOBULA_DATA_FILE, 'w') as f:
            json.dump([], f)
    if not os.path.exists(LUNARCRUSH_DATA_FILE):
        with open(LUNARCRUSH_DATA_FILE, 'w') as f:
            json.dump([], f)

    app.run(port=8000, debug=True)