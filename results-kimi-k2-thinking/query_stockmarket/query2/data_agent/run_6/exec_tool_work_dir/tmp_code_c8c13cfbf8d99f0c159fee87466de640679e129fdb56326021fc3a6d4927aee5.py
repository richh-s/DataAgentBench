code = """import json

# Read the full list of NYSE Arca ETFs from the file
symbols_file = locals()['var_functions.query_db:0']
with open(symbols_file, 'r') as f:
    symbols_data = json.load(f)

# Extract just the symbols
symbols = [item['Symbol'] for item in symbols_data]

print("__RESULT__:")
print(json.dumps({
    "count": len(symbols),
    "symbols": symbols[:20],  # Show first 20 as preview
    "total_symbols": len(symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json'}

exec(code, env_args)
