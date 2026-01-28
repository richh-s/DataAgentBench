code = """import json

# Get the list of symbols to process
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

symbols = [c['Symbol'] for c in companies_data]
company_names = {c['Symbol']: c['Company Description'] for c in companies_data}

# Let's test with the first symbol to understand the data structure
first_symbol = symbols[0]
result_data = locals()['var_functions.query_db:20']
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        result_data = json.load(f)

# Count days where range > 20% of low
high_volatility_days = 0
for day in result_data:
    high = float(day['High'])
    low = float(day['Low'])
    if low > 0:  # avoid division by zero
        range_pct = (high - low) / low
        if range_pct > 0.20:
            high_volatility_days += 1

print('__RESULT__:')
print(json.dumps({
    'symbol': first_symbol,
    'company_name': company_names[first_symbol][:50] + '...',
    'total_2019_days': len(result_data),
    'high_volatility_days': high_volatility_days
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:16': {'nasdaq_count': 86, 'available_count': 86, 'missing_count': 0, 'sample_available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'sample_missing': []}, 'var_functions.execute_python:18': {'message': 'Ready to process 86 stocks', 'stock_count': 86}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_symbols': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
