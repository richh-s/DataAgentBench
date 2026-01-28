code = """import json
# Check what's in storage
available_vars = [k for k in locals().keys() if k.startswith('var_')]
result = {
    'available_variables': available_vars
}
if 'var_functions.query_db:2' in locals():
    result['query_db_2'] = str(locals()['var_functions.query_db:2'])
if 'var_functions.query_db:8' in locals():
    result['query_db_8'] = str(locals()['var_functions.query_db:8'])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
