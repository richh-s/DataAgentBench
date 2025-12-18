code = """import json
swift_repo_names_str = locals()['var_function-call-6600485790849630513']
query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({swift_repo_names_str}) AND repo_data_description NOT LIKE '%binary file%';"
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-14885285498389857858': 'file_storage/function-call-14885285498389857858.json', 'var_function-call-6600485790849630513': 'file_storage/function-call-6600485790849630513.json', 'var_function-call-9412376694438898591': []}

exec(code, env_args)
