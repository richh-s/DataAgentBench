code = """import json
import os

# Read the full stockinfo data
stockinfo_path = locals()['var_functions.query_db:2']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

print(f"Total NYSE non-ETF symbols found: {len(stockinfo_data)}")
print("Sample symbols:", [s['Symbol'] for s in stockinfo_data[:10]])

# Load only the symbol and company description for efficiency
symbols_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
print(f"Loaded {len(symbols_companies)} symbols with company names")

# Store the cleaned data for next steps
result = {
    'total_symbols': len(symbols_companies),
    'sample_symbols': list(symbols_companies.items())[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
