code = """import json

with open(locals()['var_function-call-15310726728020166586'], 'r') as f:
    shell_repos = json.load(f)

with open(locals()['var_function-call-17618719300682475407'], 'r') as f:
    apache_repos = json.load(f)

shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}

common_repos = list(shell_repo_names.intersection(apache_repo_names))

print("__RESULT__:")
print(json.dumps(common_repos))"""

env_args = {'var_function-call-15310726728020166586': 'file_storage/function-call-15310726728020166586.json', 'var_function-call-17618719300682475407': 'file_storage/function-call-17618719300682475407.json'}

exec(code, env_args)
