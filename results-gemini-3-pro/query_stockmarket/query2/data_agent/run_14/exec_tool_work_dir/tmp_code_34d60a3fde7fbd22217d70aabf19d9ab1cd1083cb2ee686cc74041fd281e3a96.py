code = """import json

# Load relevant symbols
with open(locals()['var_function-call-795890950430017818'], 'r') as f:
    symbols = json.load(f)

# Create batches
batch_size = 400
batches = [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]

queries = []
for batch in batches:
    parts = []
    for sym in batch:
        # Use double quotes for table names as they are tickers (might have special chars or case)
        # Check Date format. DuckDB usually handles 'YYYY-MM-DD'.
        # The prompt says Date is str.
        # "Date LIKE '2015%'" is safe for string dates starting with YYYY.
        part = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1"
        parts.append(part)
    query = " UNION ALL ".join(parts)
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3949593977033921261': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12916805806640155023': 'file_storage/function-call-12916805806640155023.json', 'var_function-call-118847342532788354': 'file_storage/function-call-118847342532788354.json', 'var_function-call-795890950430017818': 'file_storage/function-call-795890950430017818.json', 'var_function-call-14536564358681273316': 1435}

exec(code, env_args)
