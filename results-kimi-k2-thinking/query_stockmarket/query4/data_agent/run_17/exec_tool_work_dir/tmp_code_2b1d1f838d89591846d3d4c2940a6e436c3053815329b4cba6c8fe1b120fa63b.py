code = """import json

# Read the query result from storage
with open('var_functions.query_db:2', 'r') as f:
    symbols = json.load(f)

print(f"Total symbols: {len(symbols)}")
print("Sample symbols:", symbols[:5])

# Create list of symbols to check
sym_list = [s['Symbol'] for s in symbols]
print(f"First 10 symbols: {sym_list[:10]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
