code = """import json

# Re-read data
stockinfo_path = locals()['var_function-call-2420597473229265013']
with open(stockinfo_path, 'r') as f:
    stock_data = json.load(f)

table_list_path = locals()['var_function-call-310547401484517096']
with open(table_list_path, 'r') as f:
    table_data = json.load(f)

stock_symbols = set(d['Symbol'] for d in stock_data)
valid_symbols = sorted([t for t in table_data if t in stock_symbols]) # Sort to be deterministic

# Batch 0: 0 to 50
batch = valid_symbols[0:50]

queries = []
for sym in batch:
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \"" + sym + "\" WHERE Date LIKE '2017-%'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2420597473229265013': 'file_storage/function-call-2420597473229265013.json', 'var_function-call-310547401484517096': 'file_storage/function-call-310547401484517096.json', 'var_function-call-13496402127410082925': {'count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_function-call-8579205056495132833': [{'Date': '2019-10-24'}], 'var_function-call-8911893808171148505': 'file_storage/function-call-8911893808171148505.json'}

exec(code, env_args)
