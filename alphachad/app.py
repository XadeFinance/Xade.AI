from flask import Flask, render_template, request, jsonify
from pipeline.agent import Agent
import langchain
import os
from langchain_openai import ChatOpenAI
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

app = Flask(__name__) 

@app.route('/', methods=['POST'])
def api():
    try: 
        load_dotenv()
        app.logger.info("Starting API request")

        # Add request debugging
        app.logger.info(f"Request Headers: {dict(request.headers)}")
        app.logger.info(f"Request Data: {request.get_data()}")

        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        query = data.get('query')
        if not query:
            return jsonify({"error": "No query provided"}), 400

        character_description = data.get('character_description', 'degen analyst')           
        app.logger.info(f"Processing query: {query} with character: {character_description}")

        # Fix model name typo
        llm = ChatOpenAI(
            api_key=getenv("OPENAI_API_KEY"),
            model_name="gpt-4o", 
            verbose=True,
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
        analysis_user_template = pipeline.prompts.analysis_human_template
        response_template = pipeline.prompts.response_template
        tweet_template = pipeline.prompts.tweet_template

        app.logger.info("Creating agent")
        agent = Agent(LLM=llm, query=query, character_description=character_description,
                    lunarcrush_endpoints=lunarcrush_endpoints, mobula_endpoints=mobula_endpoints,
                    sectors=sectors, blockchain_ids=blockchain_ids, sorting_parameters=sorting_parameters, avoid_tokens=avoid_tokens,
                    master_llm_system_template=master_llm_system_template, master_llm_user_template=master_llm_user_template, master_llm_fewshot=master_llm_fewshot,
                    data_agent_system_template=data_agent_system_template, data_agent_user_template=data_agent_user_template, data_agent_fewshot=data_agent_fewshot, data_agent_example_output=data_agent_example_output,
                    data_guardrail_template=data_guardrail_template, analysis_system_template=analysis_system_template, analysis_user_template=analysis_user_template,
                    response_template=response_template, tweet_template=tweet_template  
                    )
        
        master_output =  agent.create_process()

        apis = agent.create_apis(master_output)

        app.logger.info(apis)

        parent_call = agent.execute_parent_calls(agent.form_parent_calls(apis))

        app.logger.info(parent_call)

        top_tokens = agent.get_top_tokens(parent_call, top_n=5)

        app.logger.info(top_tokens)

        apis = agent.update_api_calls(apis, top_tokens)

        app.logger.info(apis)

        nested_call = agent.execute_nested_calls(apis)

        analysis = agent.get_analysis(top_tokens, nested_call, master_output)

        tweet = agent.create_tweet(analysis)

        return tweet

    except json.JSONDecodeError as e:
        app.logger.error(f"JSON decode error: {str(e)}")
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500
     

if __name__ == '__main__':
    app.run(port=8000, debug=True)
