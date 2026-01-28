code = """# Read the query result from the file
import json
with open('file_storage/functions.query_db:0.json', 'r') as f:
    stockinfo_result = json.load(f)

print(f"Number of NYSE non-ETF stocks: {len(stockinfo_result)}")

# Extract symbols and create a mapping from symbol to company name
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_result}
symbols = list(symbol_to_company.keys())

print(f"First 10 symbols: {symbols[:10]}")

# Store result in a JSON-serializable format
output = {
    'symbol_to_company': symbol_to_company,
    'symbols': symbols,
    'count': len(symbols)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
