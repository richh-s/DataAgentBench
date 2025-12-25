code = """import json

# Access variables
key1 = 'var_function-call-15483899617551082624'
key2 = 'var_function-call-17197364182680462886'

path_etfs = locals()[key1]
path_tables = locals()[key2]

with open(path_etfs, 'r') as f:
    etf_list = json.load(f)

etf_symbols = [item['Symbol'] for item in etf_list]

with open(path_tables, 'r') as f:
    table_list = json.load(f)

valid_etfs = sorted(list(set(etf_symbols).intersection(set(table_list))))

# Just print the count and first few to debug
print("__RESULT__:")
print(json.dumps({"count": len(valid_etfs), "preview": valid_etfs[:10]}))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json'}

exec(code, env_args)
