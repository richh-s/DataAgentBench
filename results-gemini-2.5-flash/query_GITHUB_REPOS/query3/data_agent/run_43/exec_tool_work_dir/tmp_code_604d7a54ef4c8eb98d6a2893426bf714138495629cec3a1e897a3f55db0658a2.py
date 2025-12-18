code = """import json

common_repos_file = locals()['var_function-call-2976728976911467240']

with open(common_repos_file, 'r') as f:
    common_repos = json.load(f)

repo_names_str = ", ".join([f"'{repo}'" for repo in common_repos])

query = "SELECT COUNT(message) FROM commits WHERE repo_name IN (" + \
        repo_names_str + \
        ") AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (message LIKE 'merge%' OR message LIKE 'update%' OR message LIKE 'test%');"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-14413834201273722301': 'file_storage/function-call-14413834201273722301.json', 'var_function-call-5517308377400078705': 'file_storage/function-call-5517308377400078705.json', 'var_function-call-2976728976911467240': 'file_storage/function-call-2976728976911467240.json'}

exec(code, env_args)
