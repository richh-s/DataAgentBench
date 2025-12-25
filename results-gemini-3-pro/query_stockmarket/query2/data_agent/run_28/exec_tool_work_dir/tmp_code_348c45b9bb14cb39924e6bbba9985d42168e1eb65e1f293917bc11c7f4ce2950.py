code = """import json

# Access the file paths from the variables
path_stockinfo = locals()['var_function-call-11805765579617057108']
path_tables = locals()['var_function-call-18208316545680584426']

with open(path_stockinfo, 'r') as f:
    stockinfo_data = json.load(f)

etf_symbols = set(item['Symbol'] for item in stockinfo_data)

with open(path_tables, 'r') as f:
    table_names = json.load(f)

available_tables = set(table_names)
valid_symbols = list(etf_symbols.intersection(available_tables))
valid_symbols.sort()

# Generate SQL query
queries = []
for sym in valid_symbols:
    # Construct query: SELECT 'SYM' as Symbol FROM "SYM" WHERE ...
    # We use .format to avoid quote confusion
    q = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sym)
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"valid_symbols_count": len(valid_symbols), "query": final_query}))"""

env_args = {'var_function-call-11805765579617057108': 'file_storage/function-call-11805765579617057108.json', 'var_function-call-18208316545680584426': 'file_storage/function-call-18208316545680584426.json'}

exec(code, env_args)
