code = """import json

# Load the data from the previous query
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

# Extract symbols
symbols = [c['Symbol'] for c in companies_data]
company_names = {c['Symbol']: c['Company Description'] for c in companies_data}

print('__RESULT__:')
print(json.dumps({'symbol_count': len(symbols), 'sample_symbols': symbols[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
