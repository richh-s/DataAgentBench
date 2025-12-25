code = """import json

swift_repo_names_file = locals()['var_function-call-14128026620781659525']
with open(swift_repo_names_file, 'r') as f:
    swift_repo_names = json.load(f)

# Prepare the list of repo names for the SQL IN clause
swift_repo_names_str = ', '.join([f"'{repo}'" for repo in swift_repo_names])

# Construct the DuckDB query
duckdb_query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({swift_repo_names_str}) AND repo_data_description NOT LIKE '%binary%';"

print("__RESULT__:")
print(json.dumps(duckdb_query))"""

env_args = {'var_function-call-2005781600627313199': 'file_storage/function-call-2005781600627313199.json', 'var_function-call-14128026620781659525': 'file_storage/function-call-14128026620781659525.json'}

exec(code, env_args)
