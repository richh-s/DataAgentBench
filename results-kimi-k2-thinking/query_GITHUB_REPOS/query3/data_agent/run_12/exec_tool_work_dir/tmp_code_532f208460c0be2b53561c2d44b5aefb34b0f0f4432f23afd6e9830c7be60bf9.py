code = """import json

# Get the list of Apache-2.0 licensed repos
apache_repos = locals()['var_functions.query_db:0']
# Get the list of Shell repos
shell_repos = locals()['var_functions.query_db:12']

# Extract repo names
apache_repo_names = set(repo['repo_name'] for repo in apache_repos)
shell_repo_names = set(repo['repo_name'] for repo in shell_repos)

# Find intersection
common_repos = apache_repo_names.intersection(shell_repo_names)

print('__RESULT__:')
print(json.dumps(list(common_repos)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
