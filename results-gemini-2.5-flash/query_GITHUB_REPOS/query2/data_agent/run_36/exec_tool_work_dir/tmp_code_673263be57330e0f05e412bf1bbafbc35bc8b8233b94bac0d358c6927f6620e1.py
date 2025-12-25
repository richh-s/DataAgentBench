code = """import json
import pandas as pd

swift_repos_tuple = locals()['var_function-call-15496077545562064206']

# Construct the IN clause for the SQL query
repo_names_sql_list = ', '.join([f"'{repo}'" for repo in swift_repos_tuple])

# Prepare the SQL query to get non-binary Swift files and count their occurrences
query = f"SELECT id, sample_repo_name, COUNT(id) AS copy_count FROM contents WHERE sample_repo_name IN ({repo_names_sql_list}) AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY copy_count DESC LIMIT 1;"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-32885752495782732': 'file_storage/function-call-32885752495782732.json', 'var_function-call-17315922237145365346': 'file_storage/function-call-17315922237145365346.json', 'var_function-call-15496077545562064206': 'file_storage/function-call-15496077545562064206.json'}

exec(code, env_args)
