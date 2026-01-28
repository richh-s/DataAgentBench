code = """import json

# Get NYSE ARCA ETFs
nyse_arca_path = locals()['var_functions.query_db:0']
with open(nyse_arca_path, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Get all tables in stocktrade database
stocktrade_tables_path = locals()['var_functions.list_db:12']
with open(stocktrade_tables_path, 'r') as f:
    all_tables = json.load(f)

# Create a set of table names for fast lookup
table_set = set(all_tables)

# Check which NYSE Arca ETFs actually have data tables
nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]
existing_etfs = []
missing_etfs = []

for symbol in nyse_arca_symbols:
    if symbol in table_set:
        existing_etfs.append(symbol)
    else:
        missing_etfs.append(symbol)

result = {
    "total_nyse_arca_etfs": len(nyse_arca_symbols),
    "etfs_with_data": len(existing_etfs),
    "etfs_without_data": len(missing_etfs),
    "existing_sample": existing_etfs[:10],
    "missing_sample": missing_etfs[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)
