code = """import json

# Get the full list of ETF symbols from NYSE Arca
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_symbols_data = json.load(f)

etf_symbols = [item['Symbol'] for item in etf_symbols_data]

print('__RESULT__:')
print(json.dumps({
    'count': len(etf_symbols),
    'symbols': etf_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': []}

exec(code, env_args)
