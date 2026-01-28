code = """import json

# Read the result from the first query
with open(var_functions.query_db:0, 'r') as f:
    etf_symbols = json.load(f)

print(f"Total NYSE Arca ETFs found: {len(etf_symbols)}")
print("First 10 symbols:", etf_symbols[:10])

# Let's also check the structure
print("Sample record:", etf_symbols[0] if etf_symbols else "No data")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
