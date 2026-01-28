code = """import json

# Get company data and symbols
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

symbols = [c['Symbol'] for c in companies_data]
company_names = {c['Symbol']: c['Company Description'] for c in companies_data}

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'first_10_symbols': symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:16': {'nasdaq_count': 86, 'available_count': 86, 'missing_count': 0, 'sample_available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'sample_missing': []}, 'var_functions.execute_python:18': {'message': 'Ready to process 86 stocks', 'stock_count': 86}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
