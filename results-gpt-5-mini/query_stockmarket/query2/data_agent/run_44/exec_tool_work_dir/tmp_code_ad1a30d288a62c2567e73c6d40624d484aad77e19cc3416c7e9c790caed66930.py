code = """import json
path = var_call_RzWEhQLhTSkVNtKtCb8VjS3j
with open(path, 'r') as f:
    data = json.load(f)
symbols = [row['Symbol'] for row in data]
selects = []
for sym in symbols:
    selects.append(f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
sql = " UNION ALL ".join(selects) + ";"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_RzWEhQLhTSkVNtKtCb8VjS3j': 'file_storage/call_RzWEhQLhTSkVNtKtCb8VjS3j.json'}

exec(code, env_args)
