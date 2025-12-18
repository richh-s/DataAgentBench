code = """import json

repo_names_str = json.loads(locals()['var_function-call-7122382666064980931'])

# Construct the SQL query by concatenating string literals to avoid issues with f-strings and inner single quotes
query = "SELECT COUNT(*) FROM commits WHERE repo_name IN (" + repo_names_str + ") " \
        "AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (" \
        "SUBSTRING(LOWER(message), 1, 5) = 'merge' OR " \
        "SUBSTRING(LOWER(message), 1, 6) = 'update' OR " \
        "SUBSTRING(LOWER(message), 1, 4) = 'test');"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-13059399985949405893': 'file_storage/function-call-13059399985949405893.json', 'var_function-call-7122382666064980931': 'file_storage/function-call-7122382666064980931.json'}

exec(code, env_args)
