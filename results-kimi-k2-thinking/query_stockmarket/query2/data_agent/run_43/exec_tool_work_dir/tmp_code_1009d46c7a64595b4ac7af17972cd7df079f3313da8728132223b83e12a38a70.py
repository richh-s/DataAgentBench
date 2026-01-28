code = """import json

# Read the full result from the json file
with open('var_functions.query_db:0', 'r') as f:
    etf_symbols = json.load(f)

# Extract just the symbols
symbols = [item['Symbol'] for item in etf_symbols]
print(f'__RESULT__:{symbols}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
