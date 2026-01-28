code = """import json
# Load the large results from previous tool calls (paths are provided in the variables)
with open(var_call_B94K0khwE25FYcdJAC9uOdh6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_NQ5Ham37xJsRiDqZHYYtyUqb, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo
symbols_info = [rec['Symbol'] for rec in stockinfo]
# trade_tables is a list of table names
trade_set = set(trade_tables)

# Intersection
common_symbols = [s for s in symbols_info if s in trade_set]
# Sort for deterministic order
common_symbols.sort()

# Build a UNION ALL SQL query that computes up and down counts for each symbol for 2017
selects = []
for s in common_symbols:
    # Safe table and column quoting
    part = (
        "SELECT '{sym}' AS sym, "
        "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, "
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down "
        "FROM \"{sym}\" "
        "WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    ).format(sym=s)
    selects.append(part)

# Combine
full_query = "SELECT sym, up, down FROM (\n" + "\nUNION ALL\n".join(selects) + "\n) AS t ORDER BY (up - down) DESC;"

output = json.dumps(full_query)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_B94K0khwE25FYcdJAC9uOdh6': 'file_storage/call_B94K0khwE25FYcdJAC9uOdh6.json', 'var_call_NQ5Ham37xJsRiDqZHYYtyUqb': 'file_storage/call_NQ5Ham37xJsRiDqZHYYtyUqb.json'}

exec(code, env_args)
