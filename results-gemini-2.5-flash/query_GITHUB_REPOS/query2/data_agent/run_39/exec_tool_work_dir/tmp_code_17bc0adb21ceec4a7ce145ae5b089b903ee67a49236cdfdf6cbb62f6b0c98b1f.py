code = """import json

swift_repo_names_file_path = locals()['var_function-call-10884086476726228607']
with open(swift_repo_names_file_path, 'r') as f:
    swift_repo_names = json.load(f)

# Prepare repo names for SQL IN clause: escape single quotes and enclose in single quotes
formatted_repo_names = [f"'{repo.replace("'", "''")}'" for repo in swift_repo_names]
repo_names_in_clause = ', '.join(formatted_repo_names)

# Construct the SQL query as a single string
query = f"SELECT id, sample_repo_name, repo_data_description, sample_path FROM contents WHERE sample_repo_name IN ({repo_names_in_clause}) AND repo_data_description NOT LIKE '%binary%' AND sample_path LIKE '%.swift';"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-9684736512811943360': 'file_storage/function-call-9684736512811943360.json', 'var_function-call-10884086476726228607': 'file_storage/function-call-10884086476726228607.json', 'var_function-call-1691160880071320013': 'file_storage/function-call-1691160880071320013.json'}

exec(code, env_args)
