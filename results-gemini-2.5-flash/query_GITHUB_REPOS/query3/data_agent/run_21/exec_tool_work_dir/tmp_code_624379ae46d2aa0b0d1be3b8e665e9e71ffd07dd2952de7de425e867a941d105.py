code = """import json

with open(locals()['var_function-call-10299713719053882032'], 'r') as f:
    repo_names_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_names_data['results']]
repo_names_str = ", ".join(f"'{name}'" for name in repo_names)

print("__RESULT__:")
print(json.dumps(repo_names_str))"""

env_args = {'var_function-call-10299713719053882032': 'file_storage/function-call-10299713719053882032.json'}

exec(code, env_args)
