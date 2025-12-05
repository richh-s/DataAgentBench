code = """import json, pandas as pd
from datetime import datetime

path = var_call_YHNGozXb50PTHGxiDMyMV69X
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GSPTSE': 'Toronto Stock Exchange'
}

na_df = df[df['Index'].isin(north_american.keys())]

na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Izkl90uAlJyZ6f7Ei7523uG8': ['index_info'], 'var_call_1pE9c0GSqKpUb7jflGjrQN6t': ['index_trade'], 'var_call_pANPldicO1tZLFd1nfjWF1ts': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_TCP2X5TqcrUeaWPR6JlKmJm0': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_YHNGozXb50PTHGxiDMyMV69X': 'file_storage/call_YHNGozXb50PTHGxiDMyMV69X.json'}

exec(code, env_args)
