code = """import json

# Load the large results from files
with open('var_function-call-1835962571305796969.json', 'r') as f:
    stockinfo_list = json.load(f)

with open('var_function-call-1835962571305799198.json', 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol'] for item in stockinfo_list}
trade_table_set = set(trade_tables)

# Intersection
valid_symbols = list(nasdaq_capital_symbols.intersection(trade_table_set))

print(f"Total NASDAQ Capital Market symbols: {len(nasdaq_capital_symbols)}")
print(f"Total Trade tables: {len(trade_table_set)}")
print(f"Intersection count: {len(valid_symbols)}")

# Generate SQL query
# We need to be careful about the query length.
# Let's try to generate it for all valid symbols.

sqls = []
for sym in valid_symbols:
    # Double quote table name if needed, but usually simple tickers are fine. 
    # Better safe: wrap in double quotes.
    sqls.append(f"SELECT '{sym}' as Symbol, COUNT(*) as cnt FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")

full_query = " UNION ALL ".join(sqls)
full_query = full_query + " ORDER BY cnt DESC LIMIT 5"

print(f"Query length: {len(full_query)}")

# Store the query in a variable or file if needed, but here I will just output it or a part of it.
# Actually, I need to pass this query to the next tool.
# If it's too large, I'll split it.
# 550 * 120 chars approx = 66000. 66KB is likely fine.

print("__RESULT__:")
print(json.dumps({"query": full_query, "valid_symbols_count": len(valid_symbols)}))"""

env_args = {'var_function-call-1835962571305796969': 'file_storage/function-call-1835962571305796969.json', 'var_function-call-1835962571305799198': 'file_storage/function-call-1835962571305799198.json'}

exec(code, env_args)
