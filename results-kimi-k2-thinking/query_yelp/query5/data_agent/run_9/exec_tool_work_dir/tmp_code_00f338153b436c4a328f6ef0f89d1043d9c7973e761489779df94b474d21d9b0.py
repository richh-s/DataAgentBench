code = """import json

# Access the stored result
result_var = locals()['var_functions.query_db:2']

# Load the data
if isinstance(result_var, str) and result_var.endswith('.json'):
    # It's a file path
    with open(result_var, 'r') as f:
        businesses = json.load(f)
else:
    # It's direct data
    businesses = result_var

print('__RESULT__:')
print(json.dumps({
    'type': str(type(result_var)),
    'is_string': isinstance(result_var, str),
    'sample': str(result_var)[:200] if isinstance(result_var, str) else result_var[:2]
}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
