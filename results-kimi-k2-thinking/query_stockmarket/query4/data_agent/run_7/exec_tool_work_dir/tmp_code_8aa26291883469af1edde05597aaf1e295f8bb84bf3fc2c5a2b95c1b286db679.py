code = """import json, os

# Access the stored result from the query
result_path = var_functions.query_db:0

# Read the full data if it's a file path
if isinstance(result_path, str) and result_path.endswith('.json'):
    with open(result_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = result_path

# Extract symbols and company names
symbol_to_company = {}
for item in stockinfo_data:
    symbol = item.get('Symbol')
    company = item.get('Company Description', '')
    if symbol and company:
        symbol_to_company[symbol] = company

print('__RESULT__:')
print(json.dumps({'total_stocks': len(symbol_to_company), 'sample': list(symbol_to_company.items())[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN']}

exec(code, env_args)
