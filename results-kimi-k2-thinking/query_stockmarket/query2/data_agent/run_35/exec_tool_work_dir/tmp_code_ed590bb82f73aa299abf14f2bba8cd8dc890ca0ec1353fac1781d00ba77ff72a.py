code = """import json

# Read the result from the first query
with open('var_functions.query_db:0', 'r') as f:
    etf_symbols = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'count': len(etf_symbols),
    'sample': etf_symbols[:10],
    'first_record': etf_symbols[0] if etf_symbols else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
