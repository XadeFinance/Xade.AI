# data_cycle.py
import os
import json
import requests
from dotenv import load_dotenv
from supabase import create_client, Client
import time
from celery import shared_task
import pipeline.agent
import pipeline.variables
import pipeline.prompts
import pipeline.fewshots
import datetime

load_dotenv()

MOBULA_DATA_FILE = "./pipeline/mobula-data.json"
LUNARCRUSH_DATA_FILE = "./pipeline/lunarcrush-data.json"

lunarcrush_headers = {'Authorization': 'Bearer deb9mcyuk3wikmvo8lhlv1jsxnm6mfdf70lw4jqdk'}
mobula_headers ={"Authorization": "e26c7e73-d918-44d9-9de3-7cbe55b63b99"}
lunarcrush_base_url ="https://lunarcrush.com/api4"
mobula_base_url = "https://production-api.mobula.io/api/1"

header_map = {
    "lunarcrush": lunarcrush_headers,
    "mobula": mobula_headers
}

base_urls = {
    "lunarcrush": lunarcrush_base_url,
    "mobula": mobula_base_url
}


supabase_url: str = os.environ.get("SUPABASE_PROJECT_URL")
supabase_key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


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

def fetch_unique_endpoints_from_supabase():
    try:
        response = supabase.table('apis_to_call').select('endpoint').execute()
        endpoints_data = response.data
        unique_endpoints = set()
        for item in endpoints_data:
            endpoint = item.get('endpoint')
            if endpoint:
                unique_endpoints.add(endpoint)
        return list(unique_endpoints)
    except Exception as e:
        print(f"Exception during endpoint fetching from Supabase: {e}")
        return None

def determine_provider(endpoint_path): 
    if endpoint_path.startswith("/public"): 
        return "lunarcrush"
    else:
        return "mobula"

@shared_task(name='data_cycle.run_data_cycle_task') # Define Celery task and set name
def run_data_cycle_task(): # Renamed function to run_data_cycle_task
    print("Starting data cycle...")
    endpoints = fetch_unique_endpoints_from_supabase()
    if not endpoints:
        print("No endpoints fetched from Supabase. Data cycle aborted.")
        return

    print(f"Fetched {len(endpoints)} unique endpoints from Supabase.")

    for endpoint_path in endpoints: # Renamed variable to endpoint_path
        provider = determine_provider(endpoint_path) # Pass endpoint_path to determine_provider
        if not provider:
            print(f"Could not determine provider for endpoint path: {endpoint_path}. Skipping.") # Updated log message
            continue

        base_url = base_urls.get(provider) # Get base URL based on provider
        if not base_url:
            print(f"No base URL defined for provider '{provider}'. Skipping endpoint path: {endpoint_path}") # Updated log message
            continue

        full_url = base_url + endpoint_path # Construct full URL by joining base URL and endpoint path
        headers = header_map.get(provider)
        if headers is None:
            print(f"No headers defined for provider '{provider}'. Skipping endpoint: {endpoint_path}") # Updated log message
            continue

        print(f"Fetching data from: {full_url} (Provider: {provider})") # Log full URL

        # Check local data first (Removed in previous step for hourly refresh)

        try:
            start_time = time.time()
            response = requests.get(full_url, headers=headers, timeout=20) # Use full_url for request
            response.raise_for_status()  # Raise an exception for HTTP errors
            response_data = response.json()
            end_time = time.time()
            fetch_duration = end_time - start_time
            print(f"Successfully fetched data from {full_url} in {fetch_duration:.2f} seconds.") # Use full_url in log message


            # Update local data
            endpoint_data_to_save = {'endpoint': full_url, 'response': response_data} # Use full_url for saving
            # Load, update, and save local data (logic same as before)
            provider_local_data = load_local_data(provider)
            existing_data_index = -1
            for index, item in enumerate(provider_local_data):
                if item.get('endpoint') == full_url:
                    existing_data_index = index
                    break
            if existing_data_index != -1:
                provider_local_data[existing_data_index] = endpoint_data_to_save
            else:
                provider_local_data.append(endpoint_data_to_save)
            save_local_data(provider, provider_local_data)

            print(f"Data saved to local file for endpoint: {full_url}") # Use full_url in log message


        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error fetching {full_url}: {http_err}") # Use full_url in error message
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error fetching {full_url}: {conn_err}") # Use full_url in error message
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error fetching {full_url}: {timeout_err}") # Use full_url in error message
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception fetching {full_url}: {req_err}") # Use full_url in error message
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error from {full_url}: {json_err}. Response text was: {response.text[:200]}...") # Use full_url in error message
        except Exception as e:
            print(f"General error fetching or processing {full_url}: {e}") # Use full_url in error message
        time.sleep(1) # Add a small delay to be nice to APIs

    print("Data cycle finished.")


@shared_task(name='data_cycle.process_agent_task')
def process_agent_task(agent_id):
    print(f"Starting agent processing task for agent ID: {agent_id}")

    try:
        # 1. Fetch agent details from Supabase
        response_agent = supabase.table('agents').select('*').eq('id', agent_id).execute()
        if not response_agent or not response_agent.data:
            print(f"Error fetching agent details for ID: {agent_id} from Supabase or agent not found.")
            return
        agent_data = response_agent.data[0]
        agent_apis = agent_data.get('agent_apis')
        query = agent_data.get('query')
        character_description = agent_data.get('character', 'Degen Analyst') # Default character - consistent naming
        agent_name = agent_data.get('agent_name')
        agent_description = agent_data.get('agent_description')
        agent_image = agent_data.get('image') # Consistent naming: agent_image
        chat_url = agent_data.get('chat_url')
        about_agent_db = agent_data.get('about_agent') # Retrieve about_agent from DB

        if not agent_apis or not query:
            print(f"Agent APIs or query missing for agent ID: {agent_id}. Aborting task.")
            return

        # 2. Create Agent Object - consistent naming
        llm = pipeline.agent.ChatOpenAI( # Use pipeline.agent.ChatOpenAI to avoid re-init problems
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="gpt-4o", # Use gpt-4o model
            verbose=False, # Keep verbose False for background tasks
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

        agent_instance = pipeline.agent.Agent( # Use pipeline.agent.Agent, consistent naming
            LLM=llm, query=query, character_description=character_description, # Consistent naming: character_description
            lunarcrush_endpoints=lunarcrush_endpoints, mobula_endpoints=mobula_endpoints,
            sectors=sectors, blockchain_ids=blockchain_ids, sorting_parameters=sorting_parameters, avoid_tokens=avoid_tokens,
            master_llm_system_template=master_llm_system_template, master_llm_user_template=master_llm_user_template, master_llm_fewshot=master_llm_fewshot,
            data_agent_system_template=data_agent_system_template, data_agent_user_template=data_agent_user_template, data_agent_fewshot=data_agent_fewshot, data_agent_example_output=data_agent_example_output,
            data_guardrail_template=data_guardrail_template, analysis_system_template=analysis_system_template, analysis_user_template=analysis_user_template,
            response_template=response_template, tweet_template=tweet_template,
        )

        # 3. Extract Endpoints from agent_apis - no changes needed here, names are okay

        parent_api_results = [] # consistent naming is fine

        header_map_agent = { # Use agent_instance's headers and base URLs - though we won't be calling APIs directly here - naming is fine
            "lunarcrush": agent_instance.lunarcrush_headers,
            "mobula": agent_instance.mobula_headers
        }
        base_urls_agent = { # naming is fine
            "lunarcrush": agent_instance.lunarcrush_base_url,
            "mobula": agent_instance.mobula_base_url
        }



        top_tokens = agent_instance.get_top_tokens(parent_api_results, top_n=5) # Use agent_instance - naming is fine
        updated_apis = agent_instance.update_api_calls(agent_apis, top_tokens) # Use agent_apis here as base - naming is fine
        nested_api_responses = [] # naming is fine
        base_urls_nested = { # naming is fine
            "lunarcrush": agent_instance.lunarcrush_base_url, # Use agent's base urls for nested calls too - even if not calling directly, might be used in analysis
            "mobula": agent_instance.mobula_base_url
        }
        header_map_nested = { # naming is fine
            "lunarcrush": agent_instance.lunarcrush_headers,
            "mobula": agent_instance.mobula_headers
        }


        for parent_api_call in updated_apis: # Iterate through parent API calls (potentially with nested calls) - naming is fine
            if isinstance(parent_api_call, dict) and isinstance(parent_api_call.get("nested_calls"), list): # naming is fine
                for nested_call_def in parent_api_call["nested_calls"]: # naming is fine
                    provider = str(nested_call_def.get("provider", "")).lower().strip() # naming is fine
                    endpoint = nested_call_def.get("endpoint", "") # naming is fine
                    parameters = nested_call_def.get("parameters", {}) # naming is fine
                    base_url_nested = base_urls_nested.get(provider) # Use agent's base URLs - for analysis context even if not calling directly - naming is fine
                    headers_nested = header_map_nested.get(provider, {}) # Use agent's headers - same as above - naming is fine
                    full_url_nested = base_url_nested + endpoint # naming is fine


                    # Look for nested data in local files - same logic as parent calls - naming is fine
                    local_data_nested = load_local_data(provider) # naming is fine
                    existing_nested_data = None # naming is fine
                    for data_entry in local_data_nested: # naming is fine
                        full_url_in_data = data_entry.get('endpoint') # naming is fine
                        if full_url_in_data and full_url_nested in full_url_in_data: # Check if full URL contains nested full_url - naming is fine
                            existing_nested_data = data_entry.get('response') # naming is fine
                            print(f"Found local data for nested endpoint: {full_url_nested} (Agent Processing)") # naming is fine
                            break # naming is fine

                    nested_api_responses.append(existing_nested_data) # Append found data or None if not found - naming is fine


        # Use about_agent from DB instead of calling agent_instance.create_process() - naming is fine
        analysis = agent_instance.get_analysis(top_tokens, nested_api_responses, about_agent_db) # Use about_agent_db here - naming is fine
        tweet = agent_instance.create_tweet(analysis) # naming is fine


        # 5. Create Tweet and Update Terminal Table - naming is fine
        lastrun = datetime.datetime.now(datetime.timezone.utc).isoformat() # naming is fine
        terminal_object = { # naming is fine
            "agent_id": agent_id,
            "created_at": lastrun,
            "tweet_content": tweet,
            "posted": "FALSE"
        }
        response_terminal = supabase.table('terminal').insert(terminal_object).execute() # naming is fine
        print(f"Tweet created and terminal table updated for agent ID: {agent_id}") # naming is fine

        # 6. Update lastrun in agents table - naming is fine
        response_agent_update = supabase.table('agents').update({'last_run': lastrun}).eq('id', agent_id).execute() # naming is fine
        print(f"Agent table updated with last_run timestamp for agent ID: {agent_id}") # naming is fine


    except Exception as e:
        print(f"Error processing agent ID: {agent_id}: {e}")
        return f"Error processing agent ID: {agent_id}: {e}" # For Celery error handling - naming is fine

    print(f"Agent processing task finished for agent ID: {agent_id}") # naming is fine
    return tweet # Return tweet content, can be useful for logging/monitoring # naming is fine


if __name__ == "__main__": # Keep main block for manual data cycle test
    if not os.path.exists(MOBULA_DATA_FILE):
        os.makedirs(os.path.dirname(MOBULA_DATA_FILE), exist_ok=True) # Ensure directory exists
        with open(MOBULA_DATA_FILE, 'w') as f:
            json.dump([], f)
    if not os.path.exists(LUNARCRUSH_DATA_FILE):
        os.makedirs(os.path.dirname(LUNARCRUSH_DATA_FILE), exist_ok=True) # Ensure directory exists
        with open(LUNARCRUSH_DATA_FILE, 'w') as f:
            json.dump([], f)
    run_data_cycle_task() # Run data cycle task for manual test
    # Example of manually triggering agent task for testing (replace with actual agent_id)
    # process_agent_task.delay(agent_id=1) # Example: process agent with ID 1