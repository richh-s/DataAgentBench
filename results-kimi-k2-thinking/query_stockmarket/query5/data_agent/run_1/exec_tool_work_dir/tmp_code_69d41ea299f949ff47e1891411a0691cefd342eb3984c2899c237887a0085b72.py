code = """import json

# Get the list of all tables from stocktrade_database
all_tables = locals()['var_functions.list_db:8']
if isinstance(all_tables, str):
    with open(all_tables, 'r') as f:
        all_tables = json.load(f)

# Get NASDAQ Capital Market stocks
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

nasdaq_symbols = [c['Symbol'] for c in companies_data]
company_names = {c['Symbol']: c['Company Description'] for c in companies_data}

# Find intersection (which NASDAQ Capital Market stocks have data)
available_symbols = []
missing_symbols = []
for symbol in nasdaq_symbols:
    if symbol in all_tables:
        available_symbols.append(symbol)
    else:
        missing_symbols.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'nasdaq_count': len(nasdaq_symbols),
    'available_count': len(available_symbols),
    'missing_count': len(missing_symbols),
    'sample_available': available_symbols[:10],
    'sample_missing': missing_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}}

exec(code, env_args)
