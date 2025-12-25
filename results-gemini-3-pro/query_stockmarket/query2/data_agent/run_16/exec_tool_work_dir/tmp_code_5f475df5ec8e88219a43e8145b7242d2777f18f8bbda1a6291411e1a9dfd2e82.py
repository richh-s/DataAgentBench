code = """import json

# Load ETF symbols
with open('var_function-call-17042838615002828598.json', 'r') as f:
    etf_data = json.load(f)
etf_symbols = set([item['Symbol'] for item in etf_data])

# Load table list
with open('var_function-call-1654927262755686554.json', 'r') as f:
    tables = json.load(f)
table_set = set(tables)

# Find intersection
valid_etfs = list(etf_symbols.intersection(table_set))

print("__RESULT__:")
print(json.dumps(valid_etfs))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json'}

exec(code, env_args)
