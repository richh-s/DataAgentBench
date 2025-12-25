code = """import json, pandas as pd, os

path = var_call_fXFPXQ9mpD0BDCr7tmVGYJOS
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open', 'Close']:
    df[col] = df[col].astype(float)

# classify days
df['up'] = df['Close'] > df['Open']
df['down'] = df['Close'] < df['Open']

summary = df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_awOmrdHsFnxa0csODqgLT69s': ['index_info'], 'var_call_HsK1bHh46O8IwSpt3dAzUQMi': ['index_trade'], 'var_call_PRAegR23dgtN13kdttmx7Y1L': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_lewhYE2hI67mijEVJNUF0jWY': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}], 'var_call_BhXWeqdyJY4u731sHAPTsSWl': ['NYA', 'IXIC', 'GSPTSE'], 'var_call_fXFPXQ9mpD0BDCr7tmVGYJOS': 'file_storage/call_fXFPXQ9mpD0BDCr7tmVGYJOS.json'}

exec(code, env_args)
