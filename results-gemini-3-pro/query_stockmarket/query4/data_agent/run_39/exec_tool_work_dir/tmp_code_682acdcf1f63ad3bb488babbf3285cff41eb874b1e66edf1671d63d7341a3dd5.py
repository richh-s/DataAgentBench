code = """import json

# Load data
with open(locals()['var_function-call-3260052921380199476'], 'r') as f:
    stock_info_list = json.load(f)
with open(locals()['var_function-call-14500424422696232758'], 'r') as f:
    trade_tables = json.load(f)

trade_tables_set = set(trade_tables)
valid_stocks = [s for s in stock_info_list if s['Symbol'] in trade_tables_set]

batch_size = 50
queries = []

for i in range(0, len(valid_stocks), batch_size):
    batch = valid_stocks[i:i+batch_size]
    subqueries = []
    for stock in batch:
        sym = stock['Symbol']
        # Shortened query for DuckDB
        # Use cast if SUM(bool) isn't certain, but DuckDB usually supports it. To be safe: SUM((Close>Open)::INT)
        # Actually SUM(Close>Open) works in DuckDB.
        q = "SELECT '{}' s, SUM((Close>Open)::INT) u, SUM((Close<Open)::INT) d FROM \"{}\" WHERE Date LIKE '2017%'".format(sym, sym)
        subqueries.append(q)
    queries.append(" UNION ALL ".join(subqueries))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3260052921380199476': 'file_storage/function-call-3260052921380199476.json', 'var_function-call-14500424422696232758': 'file_storage/function-call-14500424422696232758.json', 'var_function-call-15886093259379470048': 234, 'var_function-call-10586169302050306431': 'file_storage/function-call-10586169302050306431.json', 'var_function-call-7023851435820604844': 'file_storage/function-call-7023851435820604844.json', 'var_function-call-12694761523575049078': 'file_storage/function-call-12694761523575049078.json'}

exec(code, env_args)
