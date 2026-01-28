code = """import json
# var_call_e1SR9NwwhTM7KqtI4CpfNGeC is available from storage
records = var_call_e1SR9NwwhTM7KqtI4CpfNGeC
# extract the OwnerId
agent_id = None
if records and isinstance(records, list):
    agent_id = records[0].get('OwnerId')
# print result in required format
print("__RESULT__:")
print(json.dumps(agent_id))"""

env_args = {'var_call_e1SR9NwwhTM7KqtI4CpfNGeC': [{'OwnerId': '005Wt000003NJgAIAW', 'avg_days': '49.0'}]}

exec(code, env_args)
