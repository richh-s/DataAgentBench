code = """import json
# var_call_sPHxAEet36BCsb0lyj6rO3bR is available in storage
with open(var_call_sPHxAEet36BCsb0lyj6rO3bR, 'r') as f:
    data = json.load(f)
ids = [int(item['article_id']) for item in data]
print('__RESULT__:')
print(json.dumps(ids))"""

env_args = {'var_call_sPHxAEet36BCsb0lyj6rO3bR': 'file_storage/call_sPHxAEet36BCsb0lyj6rO3bR.json'}

exec(code, env_args)
