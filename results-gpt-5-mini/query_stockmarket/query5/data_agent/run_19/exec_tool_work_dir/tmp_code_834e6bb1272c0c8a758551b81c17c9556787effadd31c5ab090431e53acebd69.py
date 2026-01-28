code = """import json
# Load stored results
with open(var_call_mCZX40n6pNV9BgHm9Uf5whVa, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_X1mq3L2N4XZjiqZMtAqHx3up, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
available = [s for s in symbols if s in tables]

subqueries = []
for s in available:
    sq = ("SELECT '" + s + "' AS Symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt"
          + " FROM \"" + s + "\""
          + " WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31'")
    subqueries.append(sq)

if not subqueries:
    final_sql = ''
else:
    final_sql = 'SELECT Symbol, cnt FROM (\n' + '\nUNION ALL\n'.join(subqueries) + '\n) ORDER BY cnt DESC LIMIT 5;'

print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_mCZX40n6pNV9BgHm9Uf5whVa': 'file_storage/call_mCZX40n6pNV9BgHm9Uf5whVa.json', 'var_call_X1mq3L2N4XZjiqZMtAqHx3up': 'file_storage/call_X1mq3L2N4XZjiqZMtAqHx3up.json'}

exec(code, env_args)
