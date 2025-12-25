code = """import json

# Load stockinfo
# The previous result is in var_function-call-2745503811113855905
# It's a file path
with open(locals()['var_function-call-2745503811113855905'], 'r') as f:
    stock_info = json.load(f)

# Load table list
# The previous result is in var_function-call-15628124183444077375
with open(locals()['var_function-call-15628124183444077375'], 'r') as f:
    table_list = json.load(f)
    
# Filter stocks
# Criteria: Listing Exchange = 'N', ETF = 'N'
# We also need to make sure the table exists in stocktrade_database
# Note: Table names match Symbol
target_stocks = []
table_set = set(table_list)

stock_name_map = {}

for s in stock_info:
    sym = s.get('Symbol')
    if s.get('Listing Exchange') == 'N' and s.get('ETF') == 'N':
        if sym in table_set:
            target_stocks.append(sym)
            stock_name_map[sym] = s.get('Company Description')

# Construct SQL query
# We need to find top 5 with more up days than down days.
# We will select Symbol, UpDays, DownDays for all target stocks.
# Then we process the result in Python.

queries = []
for sym in target_stocks:
    # Use double quotes for table names to be safe (though symbols usually don't have spaces, some might have special chars?)
    # DuckDB handles double quotes for identifiers.
    q = f"SELECT '{sym}' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM \"{sym}\" WHERE Date LIKE '2017%'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print(f"Num target stocks: {len(target_stocks)}")
print(f"Query length: {len(final_query)}")

# If query is too long, we might need to strategy. 
# But let's assume it fits if it's not massive. 
# 160 stocks * ~150 chars = 24000 chars. That's fine.

print("__RESULT__:")
print(json.dumps({"query": final_query, "stock_name_map": stock_name_map}))"""

env_args = {'var_function-call-2745503811113855905': 'file_storage/function-call-2745503811113855905.json', 'var_function-call-15628124183444077375': 'file_storage/function-call-15628124183444077375.json'}

exec(code, env_args)
