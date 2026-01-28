code = """import json

# Read NYSE Arca ETF symbols
arca_file = var_functions.query_db:0
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)
arca_symbols = [item['Symbol'] for item in arca_etfs]

# Read all available symbols from stocktrade_database
all_symbols_file = var_functions.list_db:8
with open(all_symbols_file, 'r') as f:
    all_symbols = json.load(f)

# Find intersection (NYSE Arca ETFs that have price data)
available_arca_etfs = [sym for sym in arca_symbols if sym in all_symbols]

print('__RESULT__:')
print(json.dumps({
    'total_arca_etfs': len(arca_symbols),
    'total_available_symbols': len(all_symbols),
    'available_arca_etfs': len(available_arca_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 2753}

exec(code, env_args)
