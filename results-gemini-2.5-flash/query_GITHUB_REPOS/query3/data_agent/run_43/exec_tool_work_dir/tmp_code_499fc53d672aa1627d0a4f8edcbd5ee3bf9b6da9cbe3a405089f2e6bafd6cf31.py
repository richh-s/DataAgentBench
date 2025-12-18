code = """import json

shell_repos_file = locals()['var_function-call-14413834201273722301']
apache_repos_file = locals()['var_function-call-5517308377400078705']

with open(shell_repos_file, 'r') as f:
    shell_repos = json.load(f)

with open(apache_repos_file, 'r') as f:
    apache_repos = json.load(f)

shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}

common_repos = list(shell_repo_names.intersection(apache_repo_names))

print('__RESULT__:')
print(json.dumps(common_repos))"""

env_args = {'var_function-call-14413834201273722301': 'file_storage/function-call-14413834201273722301.json', 'var_function-call-5517308377400078705': 'file_storage/function-call-5517308377400078705.json'}

exec(code, env_args)
