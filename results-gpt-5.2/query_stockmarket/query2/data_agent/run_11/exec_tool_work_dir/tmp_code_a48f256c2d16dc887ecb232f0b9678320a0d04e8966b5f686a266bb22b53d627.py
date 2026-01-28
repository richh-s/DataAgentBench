code = """import json
s='''import json
path = var_call_nOWlEQHUrbqOHXmVXSYbHeRt
with open(path,'r') as f:
    etfs = json.load(f)

queries=[]
for r in etfs:
    t=r['Symbol']
    if '"' in t:
        continue
    queries.append("SELECT '{}' AS symbol, MAX(\\\"Adj Close\\\") AS max_adj_close_2015 FROM \\\"{}\\\" WHERE \\\"Date\\\" >= '2015-01-01' AND \\\"Date\\\" < '2016-01-01'".format(t,t))

union_sql=' UNION ALL '.join(queries)
print(union_sql[:200])
'''
# just output this string for debugging
print('__RESULT__:')
print(json.dumps(s))"""

env_args = {'var_call_qJiDwOwNX2pGcodn9dgo9XsI': ['stockinfo'], 'var_call_nOWlEQHUrbqOHXmVXSYbHeRt': 'file_storage/call_nOWlEQHUrbqOHXmVXSYbHeRt.json', 'var_call_7z5eVmmDQejMlywaWhpIlzRp': 'file_storage/call_7z5eVmmDQejMlywaWhpIlzRp.json', 'var_call_dn1SREokdWU5iEWahEGze1Dk': [{'name': 'AAAU'}], 'var_call_zHRHYg4x8sp4xS2rmb6nx51u': [{'max_adj': 'nan'}]}

exec(code, env_args)
