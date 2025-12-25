code = """import json, pandas as pd, os
path = var_call_iIZJ6nFz7syx4KgvgFHjtuYG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col])

# classify up/down days
df['up'] = df['Close'] > df['Open']
df['down'] = df['Close'] < df['Open']

summary = df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']
result = summary.to_dict(orient='records')
result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_x2J1maGvwR1RBEXL5d514ZG9': ['index_info'], 'var_call_nZbUeazIctbVaQSzmbzdii1z': ['index_trade'], 'var_call_5MSaJlt8QvO5rU4zPqAq2JVP': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_XuZ6WUfK8T0QMlqDid5eRNC4': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_5SV8HpOMWOJ4mExEbKCq3BIY': ['NYA', 'IXIC', 'GSPTSE'], 'var_call_iIZJ6nFz7syx4KgvgFHjtuYG': 'file_storage/call_iIZJ6nFz7syx4KgvgFHjtuYG.json'}

exec(code, env_args)
