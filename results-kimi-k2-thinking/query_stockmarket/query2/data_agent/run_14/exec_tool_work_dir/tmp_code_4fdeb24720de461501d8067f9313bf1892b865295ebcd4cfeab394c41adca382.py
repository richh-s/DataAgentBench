code = """import json

# Get file paths from storage
arca_file = locals()['var_functions.query_db:0']
symbols_file = locals()['var_functions.list_db:8']

# Read NYSE Arca ETF symbols
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)
arca_symbols = [item['Symbol'] for item in arca_etfs]

# Read all available symbols from stocktrade_database
with open(symbols_file, 'r') as f:
    all_symbols = json.load(f)

# Find intersection
available_arca_etfs = [sym for sym in arca_symbols if sym in all_symbols]

result = {
    'total_arca_etfs': len(arca_symbols),
    'total_available_symbols': len(all_symbols),
    'available_arca_etfs': len(available_arca_etfs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 2753}

exec(code, env_args)
