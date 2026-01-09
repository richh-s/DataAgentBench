code = """import json
path = var_call_o84Oh8SkIPFhXx6zUTdO5ZJn
with open(path,'r') as f:
    etfs=json.load(f)
syms=[r['Symbol'] for r in etfs]
chunks=[syms[i:i+200] for i in range(0,len(syms),200)]
print('__RESULT__:')
print(json.dumps({'n':len(syms),'chunks':len(chunks),'chunk0':chunks[0][:5]}))"""

env_args = {'var_call_Sk4bpIXrh9p4aw5g9DSpoMFB': ['stockinfo'], 'var_call_oEphkAuLQrFiLRZIfAo1H2KM': 'file_storage/call_oEphkAuLQrFiLRZIfAo1H2KM.json', 'var_call_o84Oh8SkIPFhXx6zUTdO5ZJn': 'file_storage/call_o84Oh8SkIPFhXx6zUTdO5ZJn.json', 'var_call_8TdNBLZQYSpkT4nsMfgeBHfL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_eak9UtAw8lTIkC8AhTKqi1M3': [{'Adj Close': '26.299287796020508'}], 'var_call_z4bXQxd0oM1AGn49DICAiPhJ': {'count': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
