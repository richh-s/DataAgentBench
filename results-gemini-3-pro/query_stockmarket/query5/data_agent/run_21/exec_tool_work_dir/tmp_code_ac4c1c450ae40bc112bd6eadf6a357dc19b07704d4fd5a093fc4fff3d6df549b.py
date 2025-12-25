code = """import json

# Load the result from stockinfo_database
with open(locals()['var_function-call-2999058475558920348'], 'r') as f:
    stockinfo_data = json.load(f)

# Load the result from stocktrade_database list_db
with open(locals()['var_function-call-14692438593092107821'], 'r') as f:
    table_list = json.load(f)

# Extract symbols from stockinfo
# The result from query_db is a list of dicts: [{"Symbol": "...", "Company Description": "..."}]
nasdaq_cm_symbols = [item['Symbol'] for item in stockinfo_data]

# Find intersection
valid_symbols = [s for s in nasdaq_cm_symbols if s in table_list]

print(f"Total NASDAQ Capital Market symbols found: {len(nasdaq_cm_symbols)}")
print(f"Symbols with available trade data: {len(valid_symbols)}")
print(f"First 10 valid symbols: {valid_symbols[:10]}")

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-2999058475558920348': 'file_storage/function-call-2999058475558920348.json', 'var_function-call-14692438593092107821': 'file_storage/function-call-14692438593092107821.json'}

exec(code, env_args)
