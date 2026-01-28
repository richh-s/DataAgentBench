code = """import json
# Access the variable using locals() since it has a colon in the name
result_file = locals()['var_functions.query_db:0']

with open(result_file, 'r') as f:
    non_python_repos = json.load(f)

print('__RESULT__:')
print(json.dumps(len(non_python_repos)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
