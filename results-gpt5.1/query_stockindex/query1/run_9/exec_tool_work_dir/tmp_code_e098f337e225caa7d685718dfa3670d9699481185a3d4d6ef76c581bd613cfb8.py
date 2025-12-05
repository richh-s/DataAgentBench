code = """import json, pandas as pd

path = var_call_rXPmcyrIQb2DsoXNhKZLM1Ae
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

vol = (df['High'] - df['Low']) / df['Open']
df['vol'] = vol

asian_indices = ['N225','HSI','000001.SS','399001.SZ','399006.SZ','^BSESN','^NSEI','^KS11','^TWII']
res = df[df['Index'].isin(asian_indices)].groupby('Index')['vol'].mean().sort_values(ascending=False)

result = res.to_dict()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iyAo9zn2NtVzcIDFCga7VZkK': ['index_info'], 'var_call_Uxuosk1iP9R2YRUzwpqvIdH6': ['index_trade'], 'var_call_NbE0wzkTdrM2Xr4AEXFOJdz6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_rXPmcyrIQb2DsoXNhKZLM1Ae': 'file_storage/call_rXPmcyrIQb2DsoXNhKZLM1Ae.json'}

exec(code, env_args)
