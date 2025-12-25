code = """import json

# Retrieve the repo_names_str from the previous step by loading the JSON string.
repo_names_str = json.loads(locals()['var_function-call-7122382666064980931'])

# Construct the SQL query using a triple-quoted string for the template and then format it.
# This avoids f-string parsing issues with nested quotes.
sql_query_template = """SELECT COUNT(*) FROM commits WHERE repo_name IN ({}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (SUBSTRING(LOWER(message), 1, 5) = 'merge' OR SUBSTRING(LOWER(message), 1, 6) = 'update' OR SUBSTRING(LOWER(message), 1, 4) = 'test');"""

final_sql_query = sql_query_template.format(repo_names_str)

print("__RESULT__:")
print(json.dumps(final_sql_query))"""

env_args = {'var_function-call-13059399985949405893': 'file_storage/function-call-13059399985949405893.json', 'var_function-call-7122382666064980931': 'file_storage/function-call-7122382666064980931.json'}

exec(code, env_args)
