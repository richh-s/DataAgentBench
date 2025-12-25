code = """import json

# Load data
with open(locals()['var_function-call-3260052921380199476'], 'r') as f:
    stock_info_list = json.load(f)
with open(locals()['var_function-call-14500424422696232758'], 'r') as f:
    trade_tables = json.load(f)

trade_tables_set = set(trade_tables)
valid_stocks = [s for s in stock_info_list if s['Symbol'] in trade_tables_set]

subqueries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    # Use triple single quotes to handle mixing quotes easily
    q = '''SELECT '{}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "{}" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' '''.format(sym, sym)
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-3260052921380199476': 'file_storage/function-call-3260052921380199476.json', 'var_function-call-14500424422696232758': 'file_storage/function-call-14500424422696232758.json', 'var_function-call-15886093259379470048': 234}

exec(code, env_args)
