code = """import json
# var_call_e2w6mWjWo2gPxIyS9yDawDcD is available from storage
records = var_call_e2w6mWjWo2gPxIyS9yDawDcD
# Extract AgentId
agent_id = None
if records and isinstance(records, list) and 'AgentId' in records[0]:
    agent_id = records[0]['AgentId']
# Prepare JSON-serializable string (just the agent id)
result = json.dumps(agent_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_e2w6mWjWo2gPxIyS9yDawDcD': [{'AgentId': '005Wt000003NIXCIA4', 'total_sales': '46919.149999999994'}]}

exec(code, env_args)
