code = """import pandas as pd
import json

swift_repos_json_path = locals()['var_function-call-16997509447462690496']
with open(swift_repos_json_path, 'r') as f:
    swift_repos_data = pd.read_json(f)
swift_repo_names = swift_repos_data['repo_name'].tolist()

# Prepare the list of repo names for the SQL IN clause
# DuckDB supports `IN` clause with a large number of values
# Construct the WHERE clause for the SQL query
quoted_repo_names = [f"'{repo}'" for repo in swift_repo_names]
repo_names_in_clause = ", ".join(quoted_repo_names)

# Construct the query for the artifacts_database to get relevant file data
# We need id, sample_repo_name, and repo_data_description for non-binary files in Swift repositories.
# The 'repo_data_description' field needs to be checked for 'binary' and should not contain it.

query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({repo_names_in_clause}) AND repo_data_description NOT LIKE '%binary%';"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-2850923003014532866': 'file_storage/function-call-2850923003014532866.json', 'var_function-call-1766463442254537415': 'file_storage/function-call-1766463442254537415.json', 'var_function-call-713632137538016356': 'file_storage/function-call-713632137538016356.json', 'var_function-call-13432594123923521291': [], 'var_function-call-16997509447462690496': 'file_storage/function-call-16997509447462690496.json'}

exec(code, env_args)
