code = """import json
with open(locals()['var_function-call-14251406341580762770'], 'r') as f:
    repo_names_data = json.load(f)
repo_names = [repo['repo_name'] for repo in repo_names_data]
repo_names_str = "', '".join(repo_names)
print("__RESULT__:")
print(json.dumps(repo_names_str))"""

env_args = {'var_function-call-14251406341580762770': 'file_storage/function-call-14251406341580762770.json'}

exec(code, env_args)
