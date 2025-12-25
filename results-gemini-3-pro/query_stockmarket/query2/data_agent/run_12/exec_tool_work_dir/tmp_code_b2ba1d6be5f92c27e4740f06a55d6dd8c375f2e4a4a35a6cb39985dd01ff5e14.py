code = """import json

# Load stockinfo result
with open(locals()['var_function-call-13379061347181110174'], 'r') as f:
    etf_list = json.load(f)

# Extract ETF symbols
etf_symbols = set(item['Symbol'] for item in etf_list)

# Load stocktrade tables
with open(locals()['var_function-call-6559325847238713717'], 'r') as f:
    trade_tables = set(json.load(f))

# Intersect
valid_symbols = sorted(list(etf_symbols.intersection(trade_tables)))

print(f"Total valid ETFs: {len(valid_symbols)}")

# Generate SQL query
# To avoid huge query, let's see how many. 
# If len is small (< 500), one query. If large, maybe split.
# DuckDB can handle large queries usually.

queries = []
chunk_size = 100 # Safe chunk size for UNION ALL
current_chunk = []

for sym in valid_symbols:
    # Use quoted identifier for table name just in case
    q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    current_chunk.append(q)
    
    if len(current_chunk) >= chunk_size:
        queries.append(" UNION ALL ".join(current_chunk))
        current_chunk = []

if current_chunk:
    queries.append(" UNION ALL ".join(current_chunk))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "queries": queries}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json'}

exec(code, env_args)
