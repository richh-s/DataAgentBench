code = """import json
path = var_call_WANDjwyQpxA5f7FLbLXO1IR8
with open(path) as f:
    symbols = json.load(f)
chunks = []
for sym in symbols:
    chunks.append("SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym, sym))
sql = " \nUNION ALL\n ".join(chunks)
sql = "SELECT Symbol, max_adj FROM (\n" + sql + "\n) AS t WHERE max_adj > 200 ORDER BY Symbol;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_RzWEhQLhTSkVNtKtCb8VjS3j': 'file_storage/call_RzWEhQLhTSkVNtKtCb8VjS3j.json', 'var_call_WANDjwyQpxA5f7FLbLXO1IR8': 'file_storage/call_WANDjwyQpxA5f7FLbLXO1IR8.json'}

exec(code, env_args)
