code = """import json

# Access results from local variables
stockinfo_data = locals()["var_functions.query_db:2"]
stocktables_data = locals()["var_functions.list_db:5"]

# Process the data
if isinstance(stockinfo_data, str):
    # It's a file path
    with open(stockinfo_data, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = stockinfo_data

if isinstance(stocktables_data, str):
    # It's a file path
    with open(stocktables_data, 'r') as f:
        stocktrade_symbols = json.load(f)
else:
    stocktrade_symbols = stocktables_data

# Get the intersection
nyse_arca_set = set([item['Symbol'] for item in nyse_arca_etfs])
stocktrade_set = set(stocktrade_symbols)
common = nyse_arca_set.intersection(stocktrade_set)

# Store common symbols for later use
with open('/tmp/common_symbols.json', 'w') as f:
    json.dump(list(common), f)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs_count': len(nyse_arca_set),
    'stocktrade_symbols_count': len(stocktrade_set),
    'common_symbols_count': len(common),
    'common_symbols_list': sorted(list(common))
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}}

exec(code, env_args)
