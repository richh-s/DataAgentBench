code = """import json

# Read the result from the previous query
result_file = locals()['var_functions.query_db:4']
with open(result_file, 'r') as f:
    repos = json.load(f)

# Extract repo names
repo_names = [repo['repo_name'] for repo in repos]
print('__RESULT__:')
print(json.dumps(repo_names[:10]))  # Just print the first 10 to verify"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
