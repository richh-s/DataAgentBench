code = """import json

rl = locals()['var_functions.query_db:0']

# If rl is a string (file path), read the JSON file
if isinstance(rl, str):
    with open(rl, 'r') as f:
        rl = json.load(f)

num_companies = len(rl)
result_str = 'Total: ' + str(num_companies)
print('__RESULT__:')
print(json.dumps(result_str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
