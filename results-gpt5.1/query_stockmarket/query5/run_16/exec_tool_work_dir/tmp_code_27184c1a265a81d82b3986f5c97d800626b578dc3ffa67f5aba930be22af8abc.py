code = """import json, pandas as pd
symbols = json.load(open(var_call_KMstEyhHZhZJcjYithFTGyrK))
cap_symbols = set([s for s in symbols])
rows = json.load(open(var_call_4raVig98rhFcuWBqLIEg4JLn))
df = pd.DataFrame(rows)
df2 = df[df['Symbol'].isin(cap_symbols)].copy()
result = df2['Symbol'].tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KMstEyhHZhZJcjYithFTGyrK': 'file_storage/call_KMstEyhHZhZJcjYithFTGyrK.json', 'var_call_4raVig98rhFcuWBqLIEg4JLn': 'file_storage/call_4raVig98rhFcuWBqLIEg4JLn.json'}

exec(code, env_args)
