code = """import json
# var_call_2QymsbPVn48cGe5Bsaxymzhq is available from previous query_db call
records = var_call_2QymsbPVn48cGe5Bsaxymzhq
agent_id = None
if isinstance(records, list) and len(records) > 0:
    first = records[0]
    # handle possible keys with varying cases
    agent_id = first.get('OwnerId') if isinstance(first, dict) else None
# Ensure agent_id is a plain string or null
output = json.dumps(agent_id)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_2QymsbPVn48cGe5Bsaxymzhq': [{'OwnerId': '005Wt000003NIXCIA4', 'total_sales': '46919.149999999994'}]}

exec(code, env_args)
