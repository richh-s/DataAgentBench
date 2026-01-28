code = """import json

# Check what's in locals
all_vars = list(locals().keys())
query_vars = [k for k in all_vars if 'query_db' in k]

print('__RESULT__:')
print(json.dumps({
    'query_vars': query_vars,
    'all_vars_count': len(all_vars)
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
