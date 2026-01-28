code = """import json, pandas as pd

df = pd.DataFrame(var_call_Ymu2cjjmufA5wnbsxvy5eNHq)
df['up_days'] = df['up_days'].astype(float)
df['down_days'] = df['down_days'].astype(float)
# North America indices in this dataset
na = df[df['index_symbol'].isin(['NYA','IXIC','GSPTSE'])].copy()
res = na[na['up_days'] > na['down_days']].sort_values('index_symbol')['index_symbol'].tolist()
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_I9axcLS8IucDo0deSstEVyJ0': ['index_info'], 'var_call_Qo8o90J8Nb3xl5cSOU31XWh7': ['index_trade'], 'var_call_M0nnFqBPPFUkksXT1OnJAmhN': [], 'var_call_BE99Is3ibcLQD61EKtZby2I4': [{'Date': 'September 30, 2020 at 12:00 AM', 'n': '4'}, {'Date': 'September 30, 2019 at 12:00 AM', 'n': '5'}, {'Date': 'September 30, 2016 at 12:00 AM', 'n': '4'}, {'Date': 'September 30, 2015 at 12:00 AM', 'n': '5'}, {'Date': 'September 30, 2014 at 12:00 AM', 'n': '6'}, {'Date': 'September 30, 2013 at 12:00 AM', 'n': '4'}, {'Date': 'September 30, 2011 at 12:00 AM', 'n': '4'}, {'Date': 'September 30, 2010 at 12:00 AM', 'n': '5'}, {'Date': 'September 30, 2009 at 12:00 AM', 'n': '3'}, {'Date': 'September 30, 2008 at 12:00 AM', 'n': '1'}], 'var_call_Ymu2cjjmufA5wnbsxvy5eNHq': [{'index_symbol': 'J203.JO', 'up_days': '47.0', 'down_days': '37.0'}, {'index_symbol': 'N225', 'up_days': '46.0', 'down_days': '46.0'}, {'index_symbol': 'GSPTSE', 'up_days': '34.0', 'down_days': '48.0'}, {'index_symbol': 'NSEI', 'up_days': '36.0', 'down_days': '36.0'}, {'index_symbol': 'GDAXI', 'up_days': '23.0', 'down_days': '37.0'}, {'index_symbol': 'IXIC', 'up_days': '36.0', 'down_days': '49.0'}, {'index_symbol': '000001.SS', 'up_days': '34.0', 'down_days': '44.0'}, {'index_symbol': 'SSMI', 'up_days': '34.0', 'down_days': '44.0'}, {'index_symbol': 'TWII', 'up_days': '53.0', 'down_days': '31.0'}, {'index_symbol': 'NYA', 'up_days': '39.0', 'down_days': '27.0'}, {'index_symbol': 'N100', 'up_days': '40.0', 'down_days': '45.0'}, {'index_symbol': '399001.SZ', 'up_days': '36.0', 'down_days': '47.0'}, {'index_symbol': 'HSI', 'up_days': '39.0', 'down_days': '46.0'}]}

exec(code, env_args)
