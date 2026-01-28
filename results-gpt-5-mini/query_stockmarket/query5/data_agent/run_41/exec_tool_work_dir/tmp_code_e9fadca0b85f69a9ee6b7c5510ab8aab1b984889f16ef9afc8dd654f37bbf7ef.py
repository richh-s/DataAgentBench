code = """import json
p1 = var_call_glwAqwUanNo8ExlokGyMH5xr
p2 = var_call_b8L0GzZtBYwGmNoVw96WDvnt

a = json.load(open(p1, 'r'))
b = json.load(open(p2, 'r'))

mapping = {item['Symbol']: item.get('Company Description','') for item in a}
tables = set(b)

symbols = [s for s in mapping.keys() if s in tables]

parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND ((\"High\" - \"Low\") / NULLIF(\"Low\",0)) > 0.2"
    parts.append(part)

if parts:
    sql = "SELECT Symbol, cnt FROM (" + " UNION ALL ".join(parts) + ") ORDER BY cnt DESC LIMIT 5;"
else:
    sql = "SELECT '' AS Symbol, 0 AS cnt LIMIT 0;"

out = {'sql': sql, 'symbols_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_glwAqwUanNo8ExlokGyMH5xr': 'file_storage/call_glwAqwUanNo8ExlokGyMH5xr.json', 'var_call_b8L0GzZtBYwGmNoVw96WDvnt': 'file_storage/call_b8L0GzZtBYwGmNoVw96WDvnt.json', 'var_call_3rCgDdperyl00Y2GTbxKWHEa': 'file_storage/call_3rCgDdperyl00Y2GTbxKWHEa.json', 'var_call_Phj0Ocjc3o8Ydg7irHG2GHq1': {'symbols_considered_count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
