code = """import json
path = var_call_nOWlEQHUrbqOHXmVXSYbHeRt
with open(path,'r') as f:
    etfs = json.load(f)

queries=[]
for r in etfs:
    t=r['Symbol']
    if '"' in t:
        continue
    queries.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'".format(t,t))

union_sql=' UNION ALL '.join(queries)
print('__RESULT__:')
print(json.dumps({'sql': union_sql, 'n': len(queries)}))"""

env_args = {'var_call_qJiDwOwNX2pGcodn9dgo9XsI': ['stockinfo'], 'var_call_nOWlEQHUrbqOHXmVXSYbHeRt': 'file_storage/call_nOWlEQHUrbqOHXmVXSYbHeRt.json', 'var_call_7z5eVmmDQejMlywaWhpIlzRp': 'file_storage/call_7z5eVmmDQejMlywaWhpIlzRp.json'}

exec(code, env_args)
