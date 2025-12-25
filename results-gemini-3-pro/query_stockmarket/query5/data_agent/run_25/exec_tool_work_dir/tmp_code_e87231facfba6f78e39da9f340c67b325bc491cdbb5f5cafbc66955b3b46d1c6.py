code = """import json
import pandas as pd

# Load stockinfo result
with open('var_function-call-15016460926965200659.json', 'r') as f:
    stockinfo_data = json.load(f)
    
# Extract symbols from stockinfo (Market Category S)
target_symbols = set([item['Symbol'] for item in stockinfo_data])

# Load stocktrade tables
with open('var_function-call-570738584850609366.json', 'r') as f:
    trade_tables = json.load(f)

# Intersection
valid_symbols = [s for s in trade_tables if s in target_symbols]

print(f"Total target symbols: {len(target_symbols)}")
print(f"Total trade tables: {len(trade_tables)}")
print(f"Intersection count: {len(valid_symbols)}")

# Generate SQL query
# "SELECT '<SYM>' as Symbol, COUNT(*) as cnt FROM <SYM> WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.2 * Low"
# Combine with UNION ALL

sqls = []
for sym in valid_symbols:
    # Ensure symbol is safe for SQL (though these are just tickers)
    sqls.append(f"SELECT '{sym}' as Symbol, COUNT(*) as cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low")

final_query = " UNION ALL ".join(sqls) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": final_query, "count": len(valid_symbols)}))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json'}

exec(code, env_args)
