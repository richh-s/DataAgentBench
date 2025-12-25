code = """import json

# Load list
with open(locals()['var_function-call-7696497825496925581'], 'r') as f:
    valid_etfs = json.load(f)

queries = []
dq = chr(34) # double quote

# Create smaller batches
batch_size = 100
for i in range(0, len(valid_etfs), batch_size):
    batch = valid_etfs[i:i+batch_size]
    parts = []
    for sym in batch:
        # SELECT 'SYM' as Symbol, MAX("Adj Close") as mp FROM "SYM" WHERE ...
        sql = "SELECT '" + sym + "' as Symbol, MAX(" + dq + "Adj Close" + dq + ") as mp FROM " + dq + sym + dq + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        parts.append(sql)
    
    full = "SELECT Symbol FROM (" + " UNION ALL ".join(parts) + ") WHERE mp > 200"
    queries.append(full)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-11251300445025460794': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-3995568477858160008': 'file_storage/function-call-3995568477858160008.json', 'var_function-call-16997364755516220008': 'file_storage/function-call-16997364755516220008.json', 'var_function-call-7696497825496925581': 'file_storage/function-call-7696497825496925581.json', 'var_function-call-14061231607560525758': 1435}

exec(code, env_args)
