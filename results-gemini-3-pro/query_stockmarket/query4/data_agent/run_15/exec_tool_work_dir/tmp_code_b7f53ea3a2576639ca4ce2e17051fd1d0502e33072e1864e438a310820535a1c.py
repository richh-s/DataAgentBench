code = """import json

# Load stock info
with open(locals()['var_function-call-8629880559091051052'], 'r') as f:
    stock_info = json.load(f)

# Load table list
with open(locals()['var_function-call-8629880559091050687'], 'r') as f:
    tables = json.load(f)

tables_set = set(tables)

target_stocks = []
for item in stock_info:
    if item['Symbol'] in tables_set:
        target_stocks.append(item)

queries = []
for stock in target_stocks:
    sym = stock['Symbol']
    # Ensure proper spacing and quoting
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"query": full_query, "stock_map": {s['Symbol']: s['Company Description'] for s in target_stocks}}))"""

env_args = {'var_function-call-8629880559091051052': 'file_storage/function-call-8629880559091051052.json', 'var_function-call-8629880559091050687': 'file_storage/function-call-8629880559091050687.json'}

exec(code, env_args)
