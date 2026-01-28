code = """import json

# Access the stored result
etf_symbols = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(json.dumps({'type': str(type(etf_symbols)), 'length': len(etf_symbols)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
