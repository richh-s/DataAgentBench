code = """import json

# Read the full stockinfo result from the file
with open('file_storage/functions.query_db:0.json', 'r') as f:
    stockinfo_data = json.load(f)

print("Total NYSE non-ETF stocks found:", len(stockinfo_data))
print("First 5 entries:")
for i in range(5):
    item = stockinfo_data[i]
    print("  " + item['Symbol'] + ": " + item['Company Description'][:50] + "...")

# Create symbol to company name mapping
symbol_to_company = {}
for item in stockinfo_data:
    symbol_to_company[item['Symbol']] = item['Company Description']

symbols = list(symbol_to_company.keys())

print("\nTotal symbols extracted:", len(symbols))
print("Sample symbols:", symbols[:10])

result = {
    'count': len(symbols),
    'sample_symbols': symbols[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
