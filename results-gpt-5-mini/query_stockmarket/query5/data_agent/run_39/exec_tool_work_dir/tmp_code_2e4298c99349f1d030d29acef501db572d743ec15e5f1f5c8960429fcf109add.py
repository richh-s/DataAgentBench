code = """import json
# Load previous tool results from storage keys
p1 = var_call_byEaaWSTgoQQoUxT58JNmMDG
p2 = var_call_iMmykkJX0jvhYsNbCMNy2SJt

# p1 and p2 are file paths (strings) because results were large
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo (list of dicts)
symbols_info = [r['Symbol'] for r in stockinfo]
# trade_tables is a list of table names
trade_set = set(trade_tables)

# Compute intersection
symbols = [s for s in symbols_info if s in trade_set]

# Build queries
queries = []
for s in symbols:
    q = f'SELECT COUNT(*) AS cnt FROM "{s}" WHERE Date >= \"2019-01-01\" AND Date <= \"2019-12-31\" AND High > 1.2*Low;'
    queries.append({"symbol": s, "query": q})

result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_byEaaWSTgoQQoUxT58JNmMDG': 'file_storage/call_byEaaWSTgoQQoUxT58JNmMDG.json', 'var_call_iMmykkJX0jvhYsNbCMNy2SJt': 'file_storage/call_iMmykkJX0jvhYsNbCMNy2SJt.json'}

exec(code, env_args)
