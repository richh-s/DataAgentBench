code = """import json
path = var_call_o84Oh8SkIPFhXx6zUTdO5ZJn
with open(path,'r') as f:
    etfs=json.load(f)
syms=[r['Symbol'] for r in etfs]
# filter out symbols that might break SQL identifier quoting
bad=[]
good=[]
for s in syms:
    if '"' in s or '\\' in s or s.strip()!=s:
        bad.append(s)
    else:
        good.append(s)
print('__RESULT__:')
print(json.dumps({'good':len(good),'bad':len(bad),'bad_list':bad[:20]}))"""

env_args = {'var_call_Sk4bpIXrh9p4aw5g9DSpoMFB': ['stockinfo'], 'var_call_oEphkAuLQrFiLRZIfAo1H2KM': 'file_storage/call_oEphkAuLQrFiLRZIfAo1H2KM.json', 'var_call_o84Oh8SkIPFhXx6zUTdO5ZJn': 'file_storage/call_o84Oh8SkIPFhXx6zUTdO5ZJn.json', 'var_call_8TdNBLZQYSpkT4nsMfgeBHfL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_eak9UtAw8lTIkC8AhTKqi1M3': [{'Adj Close': '26.299287796020508'}], 'var_call_z4bXQxd0oM1AGn49DICAiPhJ': {'count': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_CRkwd4GGKxxl0lhlorEAnVvy': {'n': 1435, 'chunks': 8, 'chunk0': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}}

exec(code, env_args)
