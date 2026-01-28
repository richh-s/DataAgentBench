code = """import json

# Read the Apache-2.0 licensed repos
with open('/tmp/tmphx5o9n70.json', 'r') as f:
    apache_repos = json.load(f)

# Read the repos that use Shell
with open('/tmp/tmpqlzrqd4g.json', 'r') as f:
    shell_repos_data = json.load(f)

# Extract repo names that use Shell
shell_repos = set()
for item in shell_repos_data:
    lang_desc = item['language_description'].lower()
    # Check if Shell is mentioned in the language description
    if 'shell' in lang_desc:
        shell_repos.add(item['repo_name'])

# Find intersection
apache_repos_set = set([item['repo_name'] for item in apache_repos])
common_repos = apache_repos_set.intersection(shell_repos)

print('__RESULT__:')
print(json.dumps(list(common_repos)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
