code = """import json

# Load the previous query results
with open('/tmp/tmp1g3lyh2f.json', 'r') as f:
    shell_repos = json.load(f)
    
with open('/tmp/tmp0q3v9h4_.json', 'r') as f:
    apache_repos = json.load(f)

# Extract repo names as sets
shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}

# Find intersection - repos that both use Shell and are Apache-2.0
common_repos = shell_repo_names.intersection(apache_repo_names)

print("__RESULT__:")
print(json.dumps(list(common_repos)))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
