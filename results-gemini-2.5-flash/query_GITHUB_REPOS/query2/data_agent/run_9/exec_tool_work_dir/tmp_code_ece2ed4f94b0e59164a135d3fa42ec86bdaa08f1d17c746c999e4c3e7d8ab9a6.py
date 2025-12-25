code = """import json

# Assuming var_function-call-13876236631064318048 contains the JSON string output from the previous execute_python call
parsed_data = json.loads(locals()['var_function-call-13876236631064318048'])
repo_names_str = parsed_data['repo_names_str']

# Construct the full SQL query
sql_query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE sample_repo_name IN ({repo_names_str});"

print("__RESULT__:")
print(json.dumps({"sql_query": sql_query}))"""

env_args = {'var_function-call-14350241680965922799': 'file_storage/function-call-14350241680965922799.json', 'var_function-call-13876236631064318048': 'file_storage/function-call-13876236631064318048.json'}

exec(code, env_args)
