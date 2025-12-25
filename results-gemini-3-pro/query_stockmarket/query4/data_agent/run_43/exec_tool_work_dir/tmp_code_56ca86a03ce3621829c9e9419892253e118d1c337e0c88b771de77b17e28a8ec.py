code = """import json

# Load stockinfo results
with open(locals()['var_function-call-9713228108888965980'], 'r') as f:
    stock_info_list = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-4176542361702259114'], 'r') as f:
    table_list = json.load(f)

# Create a set of available tables
available_tables = set(table_list)

# Filter stock info
candidates = []
for entry in stock_info_list:
    sym = entry['Symbol']
    if sym in available_tables:
        candidates.append(entry)

print("__RESULT__:")
print(len(candidates))"""

env_args = {'var_function-call-9713228108888965980': 'file_storage/function-call-9713228108888965980.json', 'var_function-call-4176542361702259114': 'file_storage/function-call-4176542361702259114.json'}

exec(code, env_args)
