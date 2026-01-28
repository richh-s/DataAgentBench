code = """import json

# Access the stored results using the correct keys
nasdaq_cap_result = locals()['var_functions.query_db:0']
all_tables_result = locals()['var_functions.list_db:6']

# Load the JSON data
with open(nasdaq_cap_result, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

with open(all_tables_result, 'r') as f:
    all_tables = json.load(f)

# Extract symbols
nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

# Find intersection (stocks that have data in stocktrade_database)
available_symbols = [sym for sym in nasdaq_cap_symbols if sym in all_tables]

print(f"Total NASDAQ Capital Market stocks: {len(nasdaq_cap_symbols)}")
print(f"Available in stocktrade_database: {len(available_symbols)}")
print(f"Sample available symbols: {available_symbols[:10]}")

# Create company name mapping
company_names = {}
for stock in nasdaq_cap_stocks:
    company_names[stock['Symbol']] = stock.get('Company Description', '').split(' specializes')[0].split(' is')[0].split(' operates')[0].strip()

result = {
    'available_symbols': available_symbols,
    'company_names': company_names,
    'count_available': len(available_symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
