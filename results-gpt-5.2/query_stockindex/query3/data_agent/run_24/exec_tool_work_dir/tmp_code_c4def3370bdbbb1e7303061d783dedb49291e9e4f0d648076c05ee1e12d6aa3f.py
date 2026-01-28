code = """import json
recs = var_call_EsljeS5tCjdV9VAow3HwGCyQ
for r in recs:
    if r['Index']=='IXIC':
        r['country']='United States'
    elif r['Index']=='GDAXI':
        r['country']='Germany'
    elif r['Index']=='TWII':
        r['country']='Taiwan'
    elif r['Index']=='NSEI':
        r['country']='India'

lines = []
for i, r in enumerate(recs, start=1):
    lines.append(str(i)+'. '+r['Index']+' - '+r['country']+' - ~'+('{:.2f}'.format(r['multiple']))+'x')

ans = 'Top 5 indices by $1/month DCA return since 2000 (month-end CloseUSD):\n' + '\n'.join(lines)
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_KLQHika56qcFPW44Mp3qMrFp': ['index_info'], 'var_call_kFUOdi0y8ql8euw7U9rBsd87': ['index_trade'], 'var_call_tetSxc6SzLAuLv9kEpzVCL69': 'file_storage/call_tetSxc6SzLAuLv9kEpzVCL69.json', 'var_call_EsljeS5tCjdV9VAow3HwGCyQ': [{'Index': 'IXIC', 'multiple': 4.816205036184268, 'months': 257, 'last_month': '2021-05-01 00:00:00', 'country': 'Unknown'}, {'Index': 'NSEI', 'multiple': 2.3564091777426452, 'months': 165, 'last_month': '2021-05-01 00:00:00', 'country': 'Unknown'}, {'Index': 'GDAXI', 'multiple': 2.3537005565588847, 'months': 257, 'last_month': '2021-05-01 00:00:00', 'country': 'Unknown'}, {'Index': '399001.SZ', 'multiple': 2.3383811889670953, 'months': 258, 'last_month': '2021-06-01 00:00:00', 'country': 'China'}, {'Index': 'TWII', 'multiple': 2.2447368452852596, 'months': 257, 'last_month': '2021-05-01 00:00:00', 'country': 'Unknown'}]}

exec(code, env_args)
