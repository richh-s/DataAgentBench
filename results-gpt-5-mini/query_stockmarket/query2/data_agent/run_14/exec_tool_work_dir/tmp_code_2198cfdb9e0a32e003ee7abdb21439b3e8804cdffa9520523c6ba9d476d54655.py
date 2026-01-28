code = """import json
p1 = var_call_742tOB6D3hBc8NEwfWPDvAKw
p2 = var_call_1SUoYEWvXREyq9D4xOEDzXpl
with open(p1,'r') as f:
    data1 = json.load(f)
with open(p2,'r') as f:
    data2 = json.load(f)
symbols_info = {d['Symbol'] for d in data1}
tables = set(data2)
common = sorted([s for s in symbols_info if s in tables])
parts = []
DQ = chr(34)
for t in common:
    parts.append("SELECT '{t}' AS Symbol FROM {dq}{t}{dq} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND {dq}Adj Close{dq} > 200 LIMIT 1".format(t=t,dq=DQ))
if parts:
    sql = " UNION ALL ".join(parts) + ";"
else:
    sql = "SELECT NULL WHERE 0;"
out = {'common_count': len(common), 'sql': sql}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_742tOB6D3hBc8NEwfWPDvAKw': 'file_storage/call_742tOB6D3hBc8NEwfWPDvAKw.json', 'var_call_1SUoYEWvXREyq9D4xOEDzXpl': 'file_storage/call_1SUoYEWvXREyq9D4xOEDzXpl.json'}

exec(code, env_args)
