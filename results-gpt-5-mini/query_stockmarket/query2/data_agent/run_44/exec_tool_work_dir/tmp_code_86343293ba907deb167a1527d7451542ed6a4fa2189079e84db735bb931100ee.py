code = """import json
path = var_call_WANDjwyQpxA5f7FLbLXO1IR8
with open(path) as f:
    symbols = json.load(f)
selects = []
for sym in symbols:
    selects.append(f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
inner = "\nUNION ALL\n".join(selects)
sql = "SELECT Symbol, max_adj FROM (\n" + inner + "\n) AS t WHERE max_adj > 200 ORDER BY Symbol;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_RzWEhQLhTSkVNtKtCb8VjS3j': 'file_storage/call_RzWEhQLhTSkVNtKtCb8VjS3j.json', 'var_call_WANDjwyQpxA5f7FLbLXO1IR8': 'file_storage/call_WANDjwyQpxA5f7FLbLXO1IR8.json'}

exec(code, env_args)
