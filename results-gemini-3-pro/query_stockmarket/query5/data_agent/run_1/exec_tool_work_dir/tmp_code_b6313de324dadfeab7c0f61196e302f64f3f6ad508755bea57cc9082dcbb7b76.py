code = """import json

# Access paths
path_info = locals()['var_function-call-9978005257229487382']
path_tables = locals()['var_function-call-9978005257229485951']

# Load
with open(path_info, 'r') as f:
    stock_info = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

table_set = set(tables)

# Filter
valid_symbols = []
for item in stock_info:
    if item['Symbol'] in table_set:
        valid_symbols.append(item['Symbol'])

# Print list
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-9978005257229487382': 'file_storage/function-call-9978005257229487382.json', 'var_function-call-9978005257229485951': 'file_storage/function-call-9978005257229485951.json', 'var_function-call-14222819161857472104': 'file_storage/function-call-14222819161857472104.json'}

exec(code, env_args)
