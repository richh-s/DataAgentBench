code = """import json

# Access the file paths from the variables provided by the system
path_stockinfo = locals()['var_function-call-1835962571305796969']
path_trade_tables = locals()['var_function-call-1835962571305799198']

# Load the data
with open(path_stockinfo, 'r') as f:
    stockinfo_list = json.load(f)

with open(path_trade_tables, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol'] for item in stockinfo_list}
trade_table_set = set(trade_tables)

# Intersection
valid_symbols = list(nasdaq_capital_symbols.intersection(trade_table_set))

# Generate SQL query
sqls = []
for sym in valid_symbols:
    sqls.append(f"SELECT '{sym}' as Symbol, COUNT(*) as cnt FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")

if not sqls:
    full_query = ""
else:
    full_query = " UNION ALL ".join(sqls)
    full_query = full_query + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": full_query, "valid_symbols_count": len(valid_symbols)}))"""

env_args = {'var_function-call-1835962571305796969': 'file_storage/function-call-1835962571305796969.json', 'var_function-call-1835962571305799198': 'file_storage/function-call-1835962571305799198.json'}

exec(code, env_args)
