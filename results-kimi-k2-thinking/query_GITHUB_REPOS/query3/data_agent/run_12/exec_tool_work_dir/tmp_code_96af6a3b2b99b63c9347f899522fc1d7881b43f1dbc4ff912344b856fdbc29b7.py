code = """import json

# Get Apache-2.0 licensed repos
apache_repos = locals()['var_functions.query_db:0']

# Get repos that use Shell
shell_repos_raw = locals()['var_functions.query_db:5']

# Extract repo names that use Shell
shell_repos = set()
for item in shell_repos_raw:
    lang_desc = item['language_description'].lower()
    # Check if Shell is mentioned in the language description
    if 'shell' in lang_desc:
        shell_repos.add(item['repo_name'])

# Find intersection
apache_repos_set = set([item['repo_name'] for item in apache_repos])
common_repos = apache_repos_set.intersection(shell_repos)

print('__RESULT__:')
print(json.dumps({'common_repos_count': len(common_repos), 'common_repos_sample': list(common_repos)[:20]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
