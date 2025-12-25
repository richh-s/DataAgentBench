code = """import json

with open(locals()['var_function-call-8629880559091051052'], 'r') as f:
    stock_info = json.load(f)
with open(locals()['var_function-call-8629880559091050687'], 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
target_stocks = [s for s in stock_info if s['Symbol'] in tables_set]

queries = []
for stock in target_stocks:
    sym = stock['Symbol']
    # Use .format()
    q = "SELECT '{0}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{0}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries)
stock_map = {s['Symbol']: s['Company Description'] for s in target_stocks}

print("__RESULT__:")
print(json.dumps({"query": full_query, "stock_map": stock_map}))"""

env_args = {'var_function-call-8629880559091051052': 'file_storage/function-call-8629880559091051052.json', 'var_function-call-8629880559091050687': 'file_storage/function-call-8629880559091050687.json', 'var_function-call-1791396151003041946': 'file_storage/function-call-1791396151003041946.json'}

exec(code, env_args)
