code = """import json, os
# Check what variable names are available in locals()
available_vars = [k for k in locals().keys() if 'query_db' in k]
print('__RESULT__:')
print(json.dumps({'available_vars': available_vars}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
