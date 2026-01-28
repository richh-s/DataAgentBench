code = """import json

# Access the result from the first query using locals()
etf_symbols = locals()['var_functions.query_db:0']

print('__RESULT__:')
print(json.dumps({
    'count': len(etf_symbols),
    'sample': etf_symbols[:10],
    'first_record': etf_symbols[0] if etf_symbols else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
