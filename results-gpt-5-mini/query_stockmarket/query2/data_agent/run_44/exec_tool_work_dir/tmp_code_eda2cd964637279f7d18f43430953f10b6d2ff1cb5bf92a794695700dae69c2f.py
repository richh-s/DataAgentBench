code = """import json
# var_call_RzWEhQLhTSkVNtKtCb8VjS3j is provided by previous query_db call
data = var_call_RzWEhQLhTSkVNtKtCb8VjS3j
symbols = [row['Symbol'] for row in data]
# Build a UNION ALL SQL that computes max Adj Close in 2015 for each table
selects = []
for sym in symbols:
    # quote symbol as identifier
    sel = f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    selects.append(sel)
sql = " UNION ALL ".join(selects) + ";"
# Print result in required format
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_RzWEhQLhTSkVNtKtCb8VjS3j': 'file_storage/call_RzWEhQLhTSkVNtKtCb8VjS3j.json'}

exec(code, env_args)
