code = """import json

swift_repo_names_str = json.loads(locals()['var_function-call-16989735739502139074'])

query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({swift_repo_names_str}) AND repo_data_description NOT LIKE '%binary%' AND repo_data_description LIKE '%copies:%';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-12751596650224583812': 'file_storage/function-call-12751596650224583812.json', 'var_function-call-16989735739502139074': 'file_storage/function-call-16989735739502139074.json'}

exec(code, env_args)
