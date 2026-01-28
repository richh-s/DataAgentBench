code = """import json, os

# Access the stored result using locals() since it has a colon in the name
result_var = locals()['var_functions.query_db:0']

# Read the full data if it's a file path
if isinstance(result_var, str) and result_var.endswith('.json'):
    with open(result_var, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = result_var

# Extract symbols and company names
symbol_to_company = {}
for item in stockinfo_data:
    symbol = item.get('Symbol')
    company = item.get('Company Description', '')
    if symbol and company:
        symbol_to_company[symbol] = company

print('__RESULT__:')
print(json.dumps({'total_stocks': len(symbol_to_company), 'sample': list(symbol_to_company.items())[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN']}

exec(code, env_args)
