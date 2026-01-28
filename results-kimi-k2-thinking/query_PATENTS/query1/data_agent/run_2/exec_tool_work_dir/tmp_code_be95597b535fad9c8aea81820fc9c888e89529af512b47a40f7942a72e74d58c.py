code = """import json
result_key = 'var_functions.query_db:2'
print('Available variables:', [k for k in locals().keys() if 'query' in str(k).lower()])
print('Target variable existence:', result_key in locals())
if result_key in locals():
    result_value = locals()[result_key]
    print('Type:', type(result_value))
    print('Value:', str(result_value)[:500])
else:
    print('Variable not found')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
