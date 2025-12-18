code = """import json

# Retrieve the repo_names_in_clause from the previous step's output file
with open(locals()['var_function-call-9299308723010782702'], 'r') as f:
    repo_names_in_clause = json.load(f)

# Construct the SQL query using string concatenation to avoid multiline string literal issues
sql_query = "SELECT COUNT(*) FROM commits WHERE repo_name IN (" + repo_names_in_clause + ") AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%';"

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-17512995714229407507': 'file_storage/function-call-17512995714229407507.json', 'var_function-call-9299308723010782702': 'file_storage/function-call-9299308723010782702.json', 'var_function-call-13659755516944027445': 'file_storage/function-call-13659755516944027445.json'}

exec(code, env_args)
