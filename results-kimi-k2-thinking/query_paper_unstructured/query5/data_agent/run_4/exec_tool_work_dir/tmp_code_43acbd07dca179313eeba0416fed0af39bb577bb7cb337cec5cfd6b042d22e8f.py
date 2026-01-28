code = """import json

# Read the result from the previous query - stored as a file path
result_file_path = locals()['var_functions.query_db:0']

with open(result_file_path, 'r') as f:
    citations_2020 = json.load(f)

print('__RESULT__:')
print(json.dumps({"count": len(citations_2020)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
