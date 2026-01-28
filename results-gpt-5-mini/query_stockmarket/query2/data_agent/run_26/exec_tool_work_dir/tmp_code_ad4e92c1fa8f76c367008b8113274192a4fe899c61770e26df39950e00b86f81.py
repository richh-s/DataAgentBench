code = """import json
# read storage-provided variables which contain file paths
p1 = var_call_EeBDIfF6nIPvT4Tn05bSTLUt
p2 = var_call_BhqADYroukDRFFl1xBNUru7t
with open(p1, 'r') as f:
    arca_list = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)
# arca_list is list of dicts with Symbol key
arca_symbols = [d['Symbol'] for d in arca_list]
# trade_tables is list of table names (strings)
# compute intersection
trade_set = set(trade_tables)
candidates = sorted([s for s in arca_symbols if s in trade_set])
# construct SQL query that checks for any Adj Close > 200 in 2015 for each symbol
queries = []
for s in candidates:
    # safe identifier quoting: double quotes around table name and column names
    q = f"SELECT '{s}' as Symbol FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)
if queries:
    full_query = '\nUNION ALL\n'.join(queries) + ';'
else:
    full_query = ''
out = {"num_candidates": len(candidates), "candidates": candidates, "query": full_query}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_EeBDIfF6nIPvT4Tn05bSTLUt': 'file_storage/call_EeBDIfF6nIPvT4Tn05bSTLUt.json', 'var_call_BhqADYroukDRFFl1xBNUru7t': 'file_storage/call_BhqADYroukDRFFl1xBNUru7t.json'}

exec(code, env_args)
