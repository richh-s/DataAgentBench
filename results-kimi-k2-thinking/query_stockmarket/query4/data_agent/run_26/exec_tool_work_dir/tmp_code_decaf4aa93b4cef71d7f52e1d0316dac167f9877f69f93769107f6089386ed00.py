code = """import json
import os

# Load the NYSE stock data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
valid_symbols = list(symbol_to_company.keys())

print(f"Total NYSE non-ETF stocks: {len(valid_symbols)}")
print("Sample symbols:", valid_symbols[:10])

# Process stocks in batches to avoid overwhelming the system
# For now, let's just set up the structure and test with a few stocks

result = {
    'total_stocks': len(valid_symbols),
    'sample_symbols': valid_symbols[:10],
    'symbol_to_company_sample': {k: symbol_to_company[k] for k in list(symbol_to_company.keys())[:3]}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_nyse_symbols': 234, 'available_tables': 234, 'sample_symbols': ['MTD', 'PAG', 'SMP', 'ESS', 'MKC']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
