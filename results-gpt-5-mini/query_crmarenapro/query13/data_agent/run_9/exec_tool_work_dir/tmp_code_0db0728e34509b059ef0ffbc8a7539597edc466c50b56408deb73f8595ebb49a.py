code = """import json
# var_call_dOsGvpeHb4gTtuUvg6ENg4IL is available from previous query_db call
data = var_call_dOsGvpeHb4gTtuUvg6ENg4IL
agent_id = None
if isinstance(data, list) and len(data) > 0:
    # handle possible dict keys and nulls
    first = data[0]
    # keys may have whitespace or different casing; normalize
    if isinstance(first, dict):
        # find AgentId-like key
        for k in first:
            if k.strip().lower() in ('agentid', 'ownerid', 'owner_id'):
                agent_id = first[k]
                break
        # fallback to common keys
        if agent_id is None:
            for k in ('AgentId', 'OwnerId', 'Id'):
                if k in first:
                    agent_id = first[k]
                    break

# print result in required format
print("__RESULT__:")
print(json.dumps(agent_id))"""

env_args = {'var_call_dOsGvpeHb4gTtuUvg6ENg4IL': [{'AgentId': '005Wt000003NIXCIA4', 'SalesAmount': '46919.149999999994'}]}

exec(code, env_args)
