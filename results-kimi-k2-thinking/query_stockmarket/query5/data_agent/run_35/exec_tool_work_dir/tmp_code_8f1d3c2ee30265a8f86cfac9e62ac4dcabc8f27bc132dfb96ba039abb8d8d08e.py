code = """import json

# The result is stored as a file path, let's read it
file_path = locals()['var_functions.query_db:0']
print(f"File path: {file_path}")

with open(file_path, 'r') as f:
    companies = json.load(f)

symbols = [company['Symbol'] for company in companies]
print(f"Total NASDAQ Capital Market companies: {len(symbols)}")
print(f"First 10 symbols: {symbols[:10]}")

# Create a mapping of symbol to company description
symbol_to_desc = {company['Symbol']: company['Company Description'] for company in companies}

# Store this info in a format we can use later
result = {
    "symbols": symbols,
    "symbol_to_desc": symbol_to_desc
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
