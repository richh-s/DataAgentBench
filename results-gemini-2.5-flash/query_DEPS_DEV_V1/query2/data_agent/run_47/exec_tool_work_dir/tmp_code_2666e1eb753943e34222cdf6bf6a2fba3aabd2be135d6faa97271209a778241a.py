code = """import json

# The in_clause_values variable holds a string representation of tuples.
# We need to pass this string directly into the SQL query.
in_clause = locals()['var_function-call-5813020761262683926']

print('__RESULT__:')
print(json.dumps(in_clause))"""

env_args = {'var_function-call-12206847146719381538': 'file_storage/function-call-12206847146719381538.json', 'var_function-call-14239026419335040227': 'file_storage/function-call-14239026419335040227.json', 'var_function-call-1909453510624210863': 'file_storage/function-call-1909453510624210863.json', 'var_function-call-5813020761262683926': 'file_storage/function-call-5813020761262683926.json'}

exec(code, env_args)
