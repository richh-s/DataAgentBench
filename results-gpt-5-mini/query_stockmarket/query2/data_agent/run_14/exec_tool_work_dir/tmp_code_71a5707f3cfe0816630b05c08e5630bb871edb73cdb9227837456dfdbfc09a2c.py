code = """import json
path1 = var_call_742tOB6D3hBc8NEwfWPDvAKw
path2 = var_call_1SUoYEWvXREyq9D4xOEDzXpl
with open(path1, 'r') as f:
    data1 = json.load(f)
with open(path2, 'r') as f:
    data2 = json.load(f)
symbols_info = {d['Symbol'] for d in data1}
tables = set(data2)
tickers = sorted([s for s in symbols_info if s in tables])
sql_parts = []
for t in tickers:
    part = f"SELECT '{t}' AS Symbol FROM \"{t}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    sql_parts.append(part)
if sql_parts:
    sql = " UNION ALL ".join(sql_parts) + ";"
else:
    sql = "SELECT NULL WHERE 0;"
out = {'tickers_count': len(tickers), 'tickers_sql': sql}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_742tOB6D3hBc8NEwfWPDvAKw': 'file_storage/call_742tOB6D3hBc8NEwfWPDvAKw.json', 'var_call_1SUoYEWvXREyq9D4xOEDzXpl': 'file_storage/call_1SUoYEWvXREyq9D4xOEDzXpl.json'}

exec(code, env_args)
