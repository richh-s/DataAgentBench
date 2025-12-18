code = """import json

# Load the full list of Swift repo names
with open(locals()['var_function-call-4564026000236805491'], 'r') as f:
    swift_repos_data = json.load(f)

swift_repo_names = [repo['repo_name'] for repo in swift_repos_data]

# Take a subset of repo names (e.g., first 100) to avoid query length issues
limited_swift_repo_names = swift_repo_names[:100]

# Convert the limited list of repo names to a format suitable for an SQL IN clause
swift_repo_names_str = ", ".join([f"'{repo}'" for repo in limited_swift_repo_names])

query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({swift_repo_names_str}) AND repo_data_description NOT LIKE '%binary%' AND repo_data_description LIKE '%copies:%';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-12751596650224583812': 'file_storage/function-call-12751596650224583812.json', 'var_function-call-16989735739502139074': 'file_storage/function-call-16989735739502139074.json', 'var_function-call-15365977269115016359': "SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN (file_storage/function-call-16989735739502139074.json) AND repo_data_description NOT LIKE '%binary%' AND repo_data_description LIKE '%copies:%';", 'var_function-call-4945953849579423437': 'file_storage/function-call-4945953849579423437.json', 'var_function-call-7021517103587843317': 'file_storage/function-call-7021517103587843317.json', 'var_function-call-11831139689095748826': [], 'var_function-call-4564026000236805491': 'file_storage/function-call-4564026000236805491.json'}

exec(code, env_args)
