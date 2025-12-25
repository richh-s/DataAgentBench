code = """import json

# Get file paths from local variables
path_stockinfo = locals()['var_function-call-15016460926965200659']
path_tables = locals()['var_function-call-570738584850609366']

# Load stockinfo result
with open(path_stockinfo, 'r') as f:
    stockinfo_data = json.load(f)
    
# Extract symbols from stockinfo (Market Category S)
target_symbols = set([item['Symbol'] for item in stockinfo_data])

# Load stocktrade tables
with open(path_tables, 'r') as f:
    trade_tables = json.load(f)

# Intersection
valid_symbols = [s for s in trade_tables if s in target_symbols]

# Generate SQL query
sqls = []
for sym in valid_symbols:
    sqls.append(f"SELECT '{sym}' as Symbol, COUNT(*) as cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low")

if not sqls:
    final_query = "SELECT 'No Data' as Symbol, 0 as cnt"
else:
    final_query = " UNION ALL ".join(sqls) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": final_query, "count": len(valid_symbols)}))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json'}

exec(code, env_args)
