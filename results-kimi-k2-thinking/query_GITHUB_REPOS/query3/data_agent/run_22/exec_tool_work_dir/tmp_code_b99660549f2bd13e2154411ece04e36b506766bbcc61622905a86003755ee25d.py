code = """import json
# Get the file path from the storage variable
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    repo_data = json.load(f)

repos = [item['repo_name'] for item in repo_data]
print('__RESULT__:')
print(json.dumps(repos))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
