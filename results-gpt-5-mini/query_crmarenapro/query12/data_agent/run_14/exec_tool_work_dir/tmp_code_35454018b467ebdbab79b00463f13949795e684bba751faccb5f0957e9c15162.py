code = """import json
records = var_call_cLlpGwsn9OX1SB5F6wYDMSF0
owner = None
if isinstance(records, list) and len(records) > 0:
    owner = records[0].get('ownerid')
print("__RESULT__:")
print(json.dumps(owner))"""

env_args = {'var_call_cLlpGwsn9OX1SB5F6wYDMSF0': [{'ownerid': '#005Wt000003NEa3IAG', 'avg_days': '168.0'}]}

exec(code, env_args)
