code = """import json
with open(var_call_mCZX40n6pNV9BgHm9Uf5whVa, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_X1mq3L2N4XZjiqZMtAqHx3up, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
available = [s for s in symbols if s in tables]

sql_parts = []
for s in available:
    qsym = repr(s)
    part = "SELECT {qsym} AS Symbol, SUM(CASE WHEN (High - Low) > 0.2 * Low THEN 1 ELSE 0 END) AS cnt FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'".format(qsym=qsym, tbl=s)
    sql_parts.append(part)

if sql_parts:
    final_sql = 'SELECT Symbol, cnt FROM (\n' + '\nUNION ALL\n'.join(sql_parts) + '\n) ORDER BY cnt DESC LIMIT 5;'
else:
    final_sql = ''

print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_mCZX40n6pNV9BgHm9Uf5whVa': 'file_storage/call_mCZX40n6pNV9BgHm9Uf5whVa.json', 'var_call_X1mq3L2N4XZjiqZMtAqHx3up': 'file_storage/call_X1mq3L2N4XZjiqZMtAqHx3up.json'}

exec(code, env_args)
