code = """import json
q = 'SELECT \'{}\' AS symbol, MAX("Adj Close") AS max_adj_close_2015 FROM "{}" WHERE "Date" >= \'2015-01-01\' AND "Date" < \'2016-01-01\''.format('AAAU','AAAU')
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_qJiDwOwNX2pGcodn9dgo9XsI': ['stockinfo'], 'var_call_nOWlEQHUrbqOHXmVXSYbHeRt': 'file_storage/call_nOWlEQHUrbqOHXmVXSYbHeRt.json', 'var_call_7z5eVmmDQejMlywaWhpIlzRp': 'file_storage/call_7z5eVmmDQejMlywaWhpIlzRp.json', 'var_call_dn1SREokdWU5iEWahEGze1Dk': [{'name': 'AAAU'}], 'var_call_zHRHYg4x8sp4xS2rmb6nx51u': [{'max_adj': 'nan'}], 'var_call_CXknQMbvUdsPBFxTwE4Xf8UA': 'import json\npath = var_call_nOWlEQHUrbqOHXmVXSYbHeRt\nwith open(path,\'r\') as f:\n    etfs = json.load(f)\n\nqueries=[]\nfor r in etfs:\n    t=r[\'Symbol\']\n    if \'"\' in t:\n        continue\n    queries.append("SELECT \'{}\' AS symbol, MAX("Adj Close") AS max_adj_close_2015 FROM "{}" WHERE "Date" >= \'2015-01-01\' AND "Date" < \'2016-01-01\'".format(t,t))\n\nunion_sql=\' UNION ALL \'.join(queries)\nprint(union_sql[:200])\n', 'var_call_W5lpHdi4qC8qHLW3bkLOqxeA': '2015-01-01'}

exec(code, env_args)
