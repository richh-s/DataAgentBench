code = """import json

# Load symbol list from stockinfo query
with open('var_function-call-13686535493729829546.json', 'r') as f:
    stock_data = json.load(f)

# Extract symbols
target_symbols = set(item['Symbol'] for item in stock_data)

# Load table list from stocktrade database
with open('var_function-call-7722253651347684026.json', 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)

# Intersection
valid_symbols = list(target_symbols.intersection(table_set))
valid_symbols.sort()

print("__RESULT__:")
print(len(valid_symbols))"""

env_args = {'var_function-call-7676302026983721262': 'file_storage/function-call-7676302026983721262.json', 'var_function-call-13686535493729829546': 'file_storage/function-call-13686535493729829546.json', 'var_function-call-7722253651347684026': 'file_storage/function-call-7722253651347684026.json'}

exec(code, env_args)
