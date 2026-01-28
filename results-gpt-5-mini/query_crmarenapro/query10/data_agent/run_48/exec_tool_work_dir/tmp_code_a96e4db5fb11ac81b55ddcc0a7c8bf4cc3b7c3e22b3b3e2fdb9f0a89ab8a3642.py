code = """import json
# var_call_5Izpu0pBYAIkATyUulchxMFk is available from the previous query
result = var_call_5Izpu0pBYAIkATyUulchxMFk
# Extract the agent id
agent_id = None
if isinstance(result, list) and len(result) > 0:
    agent_id = result[0].get('agent_id')
# Prepare JSON-serializable string
output = json.dumps({'agent_id': agent_id})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_5Izpu0pBYAIkATyUulchxMFk': [{'agent_id': '005Wt000003NEtOIAW'}]}

exec(code, env_args)
