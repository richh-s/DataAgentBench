code = """import json

with open(locals()['var_function-call-12911428571959370466'], 'r') as f:
    repo_names_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_names_data]

print('__RESULT__:')
print(json.dumps(repo_names))"""

env_args = {'var_function-call-12911428571959370466': 'file_storage/function-call-12911428571959370466.json'}

exec(code, env_args)
