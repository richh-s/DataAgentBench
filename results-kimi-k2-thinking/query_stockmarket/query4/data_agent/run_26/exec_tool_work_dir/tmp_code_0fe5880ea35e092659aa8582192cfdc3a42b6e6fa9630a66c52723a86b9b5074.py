code = """# Load the stockinfo query result
import json
with open('var_functions.query_db:0', 'r') as f:
    stockinfo_result = json.load(f)

print(f"Number of NYSE non-ETF stocks: {len(stockinfo_result)}")
print("First few entries:", stockinfo_result[:5])

# Extract symbols and create a mapping from symbol to company name
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_result}
symbols = list(symbol_to_company.keys())

# Print the first few symbols for verification
print("First 10 symbols:", symbols[:10])

# Prepare output for the next step
result = {
    'symbol_to_company': symbol_to_company,
    'symbols': symbols
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
