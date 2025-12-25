code = """import json
in_clause_values = json.loads(locals()['var_function-call-14239026419335040227'])

# The in_clause_values variable holds a string representation of tuples.
# We need to pass this string directly into the SQL query.

print('__RESULT__:')
print(json.dumps(in_clause_values))"""

env_args = {'var_function-call-12206847146719381538': 'file_storage/function-call-12206847146719381538.json', 'var_function-call-14239026419335040227': 'file_storage/function-call-14239026419335040227.json'}

exec(code, env_args)
