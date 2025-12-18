code = """import json

# Read the JSON file from the path stored in var_function-call-13876236631064318048
with open(locals()['var_function-call-13876236631064318048'], 'r') as f:
    parsed_data = json.load(f)

repo_names_str = parsed_data['repo_names_str']

# Construct the full SQL query
# Note: DuckDB has a limit on the length of the IN clause. If repo_names_str is extremely long,
# this query might fail. For this problem, we'll assume it's acceptable.
sql_query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({repo_names_str});"

print("__RESULT__:")
print(json.dumps({"sql_query": sql_query}))"""

env_args = {'var_function-call-14350241680965922799': 'file_storage/function-call-14350241680965922799.json', 'var_function-call-13876236631064318048': 'file_storage/function-call-13876236631064318048.json'}

exec(code, env_args)
