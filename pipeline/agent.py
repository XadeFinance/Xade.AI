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

try:
    import json5
except ImportError:
    json5 = None
    
load_dotenv()

class Agent:
  def __init__(self, LLM, query, lunarcrush_endpoints, mobula_endpoints, sectors, blockchain_ids, sorting_parameters, avoid_tokens,
               master_llm_system_template, master_llm_user_template, master_llm_fewshot,
               data_agent_system_template, data_agent_user_template, data_agent_fewshot, data_agent_example_output,
               data_guardrail_template, analysis_system_template, analysis_user_template, response_template, tweet_template, character_description):
    
    self.lunarcrush_base_url = "https://lunarcrush.com/api4"
    self.mobula_base_url = "https://production-api.mobula.io/api/1"
    self.lunarcrush_headers = {'Authorization': 'Bearer deb9mcyuk3wikmvo8lhlv1jsxnm6mfdf70lw4jqdk'}
    self.mobula_headers = {"Authorization": "e26c7e73-d918-44d9-9de3-7cbe55b63b99"}
    self.mobula_coins = "pipeline/mobula-coins.json"
    self.lunarcrush_coins = "pipeline/lunarcrush-coins.json"

    self.LLM = LLM
    self.query = query
    self.lunarcrush_endpoints = lunarcrush_endpoints
    self.mobula_endpoints = mobula_endpoints
    self.sectors = sectors
    self.blockchain_ids = blockchain_ids
    self.sorting_parameters = sorting_parameters
    self.avoid_tokens = avoid_tokens
    self.character_description = character_description

    self.master_llm_system_template = master_llm_system_template
    self.master_llm_user_template = master_llm_user_template
    self.master_llm_fewshot = master_llm_fewshot

    self.data_agent_system_template = data_agent_system_template
    self.data_agent_user_template = data_agent_user_template
    self.data_agent_fewshot = data_agent_fewshot
    self.data_agent_example_output = data_agent_example_output

    self.data_guardrail_template = data_guardrail_template
    self.analysis_system_template = analysis_system_template
    self.analysis_user_template = analysis_user_template
    self.response_template = response_template
    self.tweet_template = tweet_template

  def create_process(self):
    master_llm_prompt = [
      SystemMessagePromptTemplate.from_template(self.master_llm_system_template).format(sectors=self.sectors),
      HumanMessagePromptTemplate.from_template(self.master_llm_user_template).format(
        input=self.query,
        master_fewshot=self.master_llm_fewshot
      )
    ]
    
    master_output = self.LLM.invoke(master_llm_prompt)
    return master_output.content

  def create_apis(self, master_output):

    data_agent_prompt = [
      SystemMessagePromptTemplate.from_template(self.data_agent_system_template).format(
        sectors=self.sectors,
        lunarcrush_endpoints=self.lunarcrush_endpoints,
        mobula_endpoints=self.mobula_endpoints,
        data_fewshot=self.data_agent_fewshot,
        data_output_format=self.data_agent_example_output
      ),
      HumanMessagePromptTemplate.from_template(self.data_agent_user_template).format(
        input=self.query,
        master_output=master_output
      )
    ]
    
    data_agent_output = self.LLM.invoke(data_agent_prompt).content

    data_agent_output = self.extract_api_json(data_agent_output)

    print(data_agent_output)

    data_guardrail_prompt = ChatPromptTemplate.from_template(self.data_guardrail_template).format(
        query=self.query, 
        sectors=self.sectors, 
        lunarcrush_endpoints=self.lunarcrush_endpoints,
        mobula_endpoints=self.mobula_endpoints,
        blockchain_ids=self.blockchain_ids,
        sorting_parameters=self.sorting_parameters,
        data_output=data_agent_output
      )
    
    data_guardrail_output = self.LLM.invoke(data_guardrail_prompt).content

    data_guardrail_output = self.extract_api_json(data_guardrail_output)

    return data_guardrail_output
  

  
  def form_parent_calls(self, api_list):
    base_urls = {
        "lunarcrush": self.lunarcrush_base_url,
        "mobula": self.mobula_base_url
    }
    api_calls = []
    for api_def in api_list:
        if not isinstance(api_def, dict):
            continue
        provider = str(api_def.get("provider", "")).lower().strip()
        base_url = base_urls.get(provider)
        if not base_url:
            print(f"Unknown provider '{provider}' – skipping definition.")
            continue
        try:
            url = self.form_parent_call(api_def, base_url)
        except Exception as e:
            print(f"Error forming API call for {provider}: {e}")
            continue
        description = api_def.get("description", "")
        api_calls.append({
            "provider": provider,
            "url": url,
            "description": description
        })
    return api_calls
  

  def execute_parent_calls(self, api_calls):
    header_map = {
        "lunarcrush": self.lunarcrush_headers,
        "mobula": self.mobula_headers
    }
    results = []
    for call in api_calls:
        provider = str(call.get("provider", "")).lower().strip()
        url = call.get("url", "")
        description = call.get("description", "")
        headers = header_map.get(provider)
        if headers is None:
            results.append({
                "url": url,
                "description": description,
                "error": f"Unknown provider '{provider}'"
            })
            continue
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            results.append({
                "url": url,
                "response": response.json()
            })
        except Exception as e:
            results.append({
                "url": url,
                "description": description,
                "error": str(e)
            })
    return results
  

  def aggregate_tokens_simple(self, obj, avoid_tokens, collected=None):
      if collected is None:
          collected = {}
      if isinstance(obj, dict):
          if "symbol" in obj:
              symbol = str(obj.get("symbol", "")).upper().strip()
              if symbol and symbol not in avoid_tokens:
                  if symbol not in collected:
                      collected[symbol] = obj
          for value in obj.values():
              self.aggregate_tokens_simple(value, avoid_tokens, collected)
      elif isinstance(obj, list):
          for item in obj:
              self.aggregate_tokens_simple(item, avoid_tokens, collected)
      return collected
  

  def get_top_tokens(self, parent_api_results, top_n=5):
      
      valid_coins = self.load_valid_coins(self.mobula_coins, self.lunarcrush_coins)
      avoid_tokens = self.avoid_tokens

      avoid_set = {token.upper() for token in avoid_tokens}
      valid_set = {coin.upper() for coin in valid_coins}

      aggregated = self.aggregate_tokens_simple(parent_api_results, avoid_set)

      
      filtered_tokens = []
      for symbol, token in aggregated.items():
          if symbol in valid_set:
              filtered_tokens.append(token)
          if len(filtered_tokens) >= top_n:
              break
          
      print("Top Tokens:", [token.get('symbol') for token in filtered_tokens])
      return filtered_tokens
  

  def update_nested_calls(self, api_call, top_tokens):
    try:
        if not (isinstance(api_call, dict) and "nested_calls" in api_call and isinstance(api_call["nested_calls"], list)):
            return api_call

        # Extract and validate token symbols
        token_symbols = [str(t.get("symbol", "")).upper().strip() for t in top_tokens if t.get("symbol")]
        print(f"Available tokens for replacement: {token_symbols}")
        
        for nc in api_call["nested_calls"]:
            try:
                # Check if endpoint has placeholders
                endpoint = nc.get("endpoint", "")
                has_endpoint_placeholders = False
                if isinstance(endpoint, str):
                    placeholder_count = len(re.findall(r":\w+", endpoint))
                    has_endpoint_placeholders = placeholder_count > 0
                    print(f"Found {placeholder_count} placeholders in endpoint: {endpoint}")

                # If endpoint contains placeholders, handle them directly
                if has_endpoint_placeholders and token_symbols:
                    placeholders = re.findall(r"(:\w+)", endpoint)
                    print(f"Endpoint placeholders to replace: {placeholders}")
                    
                    new_endpoint = endpoint
                    for idx, placeholder in enumerate(placeholders):
                        token = token_symbols[idx % len(token_symbols)]
                        new_endpoint = new_endpoint.replace(placeholder, token)
                        print(f"Replacing {placeholder} with {token}")
                    
                    print(f"Updated endpoint: {new_endpoint}")
                    nc["endpoint"] = new_endpoint

                # Handle the symbols parameter if it exists
                if isinstance(nc.get("parameters"), dict) and "symbols" in nc["parameters"]:
                    if token_symbols:
                        nc["parameters"]["symbols"] = ",".join(token_symbols)
                        print(f"Updated parameters.symbols with all tokens: {nc['parameters']['symbols']}")
                    
            except Exception as e:
                print(f"Error processing nested call: {e}")
                continue
        
        return api_call
    except Exception as e:
        print(f"Error updating nested calls: {e}")
        return api_call

  def update_api_calls(self, parent_api_calls, top_tokens):
    try:
        if isinstance(parent_api_calls, list):
            return [self.update_nested_calls(call, top_tokens) for call in parent_api_calls]
        elif isinstance(parent_api_calls, dict):
            return self.update_nested_calls(parent_api_calls, top_tokens)
        else:
            return parent_api_calls
    except Exception as e:
        print("Error updating API calls:", e)
        return parent_api_calls
    

  def execute_nested_call(self, api_call):
      base_urls = {
        "lunarcrush": self.lunarcrush_base_url,
        "mobula": self.mobula_base_url
      }

      header_map = {
        "lunarcrush": self.lunarcrush_headers,
        "mobula": self.mobula_headers
      }

      try:
          provider = str(api_call.get("provider", "")).lower().strip()
          endpoint = api_call.get("endpoint", "")
          parameters = api_call.get("parameters", {})
          base_url = base_urls.get(provider)
          headers = header_map.get(provider, {})
          if not base_url:
              raise ValueError(f"No base URL defined for provider '{provider}'.")
          full_url = base_url + endpoint
          response = requests.get(full_url, params=parameters, headers=headers, timeout=10)
          response.raise_for_status()
          return response.json()
      except Exception as e:
          print(f"Error executing API call ({provider}): {e}")
          return None
      

  def execute_nested_calls(self, parent_api_calls):
      responses = []
      try:
          if isinstance(parent_api_calls, list):
              for parent in parent_api_calls:
                  if isinstance(parent, dict) and isinstance(parent.get("nested_calls"), list):
                      for nested in parent["nested_calls"]:
                          res = self.execute_nested_call(nested)
                          responses.append(res)
          elif isinstance(parent_api_calls, dict):
              for nested in parent_api_calls.get("nested_calls", []):
                  responses.append(self.execute_nested_call(nested))
          else:
              print("Unsupported structure for api_calls.")
      except Exception as e:
          print(f"Error executing pipeline: {e}")
      return responses
  

  def get_analysis(self, top_tokens, nested_responses, master_output):
      
      analysis_data = [top_tokens, nested_responses]

      analysis_system_prompt = SystemMessagePromptTemplate.from_template(self.analysis_system_template).format()

      analysis_human_prompt = HumanMessagePromptTemplate.from_template(self.analysis_user_template).format(input=self.query, analysis_data=analysis_data)
      
      analysis_output = self.LLM.invoke([analysis_system_prompt, analysis_human_prompt]).content
      
      return analysis_output
      

  def get_response(self, top_tokens, nested_responses):

    data = [top_tokens, nested_responses]

    response_prompt = ChatPromptTemplate.from_template(self.response_template).format(
        query=self.query, 
        data=data
    )

    response_output = self.LLM.invoke(response_prompt).content
    
    return response_output
  

  def create_tweet(self, analysis):

    tweet_prompt = ChatPromptTemplate.from_template(self.tweet_template).format(
        analysis=analysis,
        input=self.query, 
        character_description=self.character_description
    )

    tweet = self.LLM.invoke(tweet_prompt).content
    
    return tweet

  @staticmethod
  def extract_api_json(llm_output):
      pattern = r"```json(.*?)```"
      matches = re.findall(pattern, llm_output, re.DOTALL)
      
      if matches:
          json_str = matches[0].strip()
      else:
          fallback_marker = "FINAL API CALL STRUCTURE:"
          idx = llm_output.find(fallback_marker)
          if idx != -1:
              json_str = llm_output[idx + len(fallback_marker):].strip()
          else:
              print("No JSON content found in the LLM output.")
              return None

      try:
          return json.loads(json_str)
      except json.JSONDecodeError as e:
          if json5:
              try:
                  return json5.loads(json_str)
              except Exception as e:
                  print(f"Error decoding JSON with json5: {e}")
                  return None
          else:
              print(f"JSON decoding error: {e}. Consider installing json5 for non-strict parsing.")
              return None
          
  @staticmethod
  def form_parent_call(api_def, base_url):
    if not isinstance(api_def, dict):
        raise ValueError(f"Expected dict for API definition, got {type(api_def)}")
    endpoint = str(api_def.get("endpoint", ""))
    params = api_def.get("parameters", {})
    if not isinstance(params, dict):
        params = {}
    params = params.copy()
    if "desc" in params:
        if params["desc"] is True:
            del params["desc"]
        elif params["desc"] is False:
            params["desc"] = 1
    ordered_params = []
    if "sort" in params:
        ordered_params.append(("sort", params["sort"]))
    if "filter" in params:
        ordered_params.append(("filter", params["filter"]))
    for key, value in params.items():
        if key not in ("sort", "filter"):
            ordered_params.append((key, value))
    try:
        query_str = urllib.parse.urlencode(ordered_params)
    except Exception as e:
        print(f"Error encoding parameters: {ordered_params} - {e}")
        query_str = ""
    return f"{base_url}{endpoint}?{query_str}" if query_str else f"{base_url}{endpoint}"
  
  @staticmethod
  def load_valid_coins(coins_file, coins_lunarcrush_file):
      valid_sets = []
      for file_path in [coins_file, coins_lunarcrush_file]:
          try:
              with open(file_path, 'r') as f:
                  data = json.load(f)
          except Exception as e:
              print(f"Error loading {file_path}: {e}")
              data = {}
          if isinstance(data, dict):
              items = data.get("data") or data.get("coins") or []
              if not isinstance(items, list):
                  items = [items]
          elif isinstance(data, list):
              items = data
          else:
              items = []
          valid = set()
          for coin in items:
              if isinstance(coin, dict):
                  sym = str(coin.get("symbol", "")).upper().strip()
                  if sym:
                      valid.add(sym)
              elif isinstance(coin, str):
                  sym = coin.upper().strip()
                  if sym:
                      valid.add(sym)
          valid_sets.append(valid)
      if valid_sets:
          return list(set.intersection(*valid_sets))
      else:
          return []

  @staticmethod
  def contains_placeholder(obj):
      try:
          if isinstance(obj, str):
              return ":" in obj
          elif isinstance(obj, dict):
              return any(Agent.contains_placeholder(v) for v in obj.values())
          elif isinstance(obj, list):
              return any(Agent.contains_placeholder(item) for item in obj)
          return False
      except Exception as e:
          print(f"Error checking for placeholder in {obj}: {e}")
          return False
