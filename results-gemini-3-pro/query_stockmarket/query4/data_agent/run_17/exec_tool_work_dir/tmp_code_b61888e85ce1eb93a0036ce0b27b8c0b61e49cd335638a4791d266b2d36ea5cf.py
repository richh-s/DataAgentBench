code = """import json
stockinfo = locals()['var_function-call-2420597473229265013']
if isinstance(stockinfo, str):
    with open(stockinfo, 'r') as f:
        data = json.load(f)
else:
    data = stockinfo

print(f"Total NYSE non-ETF symbols: {len(data)}")

# Also filter the table list
table_list = locals()['var_function-call-310547401484517096']
if isinstance(table_list, str):
    with open(table_list, 'r') as f:
        tables = json.load(f)
else:
    tables = table_list

# Intersect
symbols = set(d['Symbol'] for d in data)
valid_tables = [t for t in tables if t in symbols]
print(f"Valid tables in stocktrade_database: {len(valid_tables)}")

# Print first 20 valid tables to see
print(f"First 20 valid tables: {valid_tables[:20]}")

print("__RESULT__:")
print(json.dumps({"count": len(valid_tables), "sample": valid_tables[:20]}))"""

env_args = {'var_function-call-2420597473229265013': 'file_storage/function-call-2420597473229265013.json', 'var_function-call-310547401484517096': 'file_storage/function-call-310547401484517096.json'}

exec(code, env_args)
