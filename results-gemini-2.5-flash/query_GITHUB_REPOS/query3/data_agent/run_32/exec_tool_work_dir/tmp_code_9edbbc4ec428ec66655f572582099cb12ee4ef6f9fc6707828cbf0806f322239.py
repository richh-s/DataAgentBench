code = """import json
with open(locals()['var_function-call-17512995714229407507'], 'r') as f:
    repo_names_data = json.load(f)
repo_names = [repo['repo_name'] for repo in repo_names_data]

# Escape single quotes in repo_names and wrap each in single quotes for the IN clause
repo_names_in_clause = ", ".join([f"'{name.replace("'", "''")}'" for name in repo_names])

# Construct the SQL query without using triple double quotes for the string literal
sql_query_lines = [
    "SELECT COUNT(*)",
    "FROM commits",
    f"WHERE repo_name IN ({repo_names_in_clause})",
    "  AND message IS NOT NULL",
    "  AND LENGTH(message) < 1000",
    "  AND LOWER(message) NOT LIKE 'merge%'",
    "  AND LOWER(message) NOT LIKE 'update%'",
    "  AND LOWER(message) NOT LIKE 'test%';"
]
sql_query = '\n'.join(sql_query_lines)

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-17512995714229407507': 'file_storage/function-call-17512995714229407507.json'}

exec(code, env_args)
