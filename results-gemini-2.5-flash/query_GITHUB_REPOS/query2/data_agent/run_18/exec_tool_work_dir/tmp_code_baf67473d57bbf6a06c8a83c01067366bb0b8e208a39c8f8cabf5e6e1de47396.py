code = """import json
with open(locals()['var_function-call-10437230453846877627'], 'r') as f:
    swift_repos_data = json.load(f)
swift_repos = [repo['repo_name'] for repo in swift_repos_data]
print('__RESULT__:')
print(json.dumps(swift_repos))"""

env_args = {'var_function-call-10437230453846877627': 'file_storage/function-call-10437230453846877627.json'}

exec(code, env_args)
