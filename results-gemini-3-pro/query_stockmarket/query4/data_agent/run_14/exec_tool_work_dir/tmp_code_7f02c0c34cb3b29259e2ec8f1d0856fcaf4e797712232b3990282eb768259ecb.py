code = """import json

# Load stockinfo results
with open(locals()['var_function-call-2664401347096856404'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-14718190706972975468'], 'r') as f:
    trade_tables = json.load(f)

# Filter stocks
# Criteria: ETF='N', Listing Exchange='N' (already filtered in stockinfo query), and symbol exists in trade_tables
valid_symbols = []
# Create a set for faster lookup
trade_table_set = set(trade_tables)

symbol_map = {} # Store description for later

for item in stock_info:
    sym = item['Symbol']
    if sym in trade_table_set:
        valid_symbols.append(sym)
        symbol_map[sym] = item['Company Description']

# Construct the SQL query
# We need to find stocks with more up days than down days in 2017.
# We want the top 5. Ranking criteria: usually "top" implies the magnitude of the difference (Up - Down) or just count of Up days.
# Given "more up days than down days", (Up - Down) is a good metric.
# Let's select symbol, up_days, down_days
# Since there might be many symbols, we need to be careful with query length.
# DuckDB can handle large queries, but let's check how many symbols we have.

print(f"DEBUG: Found {len(valid_symbols)} valid symbols.")

# If there are too many, we might need to batch or limit. 
# But let's try to construct the query.
sqls = []
for sym in valid_symbols:
    # Use double quotes for table names to handle case sensitivity or special chars if any
    sqls.append(f"""SELECT '{sym}' as symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) as down_days FROM "{sym}" WHERE "Date" >= '2017-01-01' AND "Date" <= '2017-12-31'""")

full_query = " UNION ALL ".join(sqls)
final_query = f"""SELECT symbol, up_days, down_days, (up_days - down_days) as diff FROM ({full_query}) WHERE up_days > down_days ORDER BY diff DESC LIMIT 5"""

print("__RESULT__:")
print(json.dumps({"query": final_query, "symbol_map": symbol_map}))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json'}

exec(code, env_args)
