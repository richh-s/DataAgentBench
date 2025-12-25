code = """import json, pandas as pd
path = var_call_2tSNzB8Shi6bcNvjZWl36pP1
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

north_american_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(north_american_indices)]
na_df['up'] = na_df['Close'] > na_df['Open']
summary = na_df.groupby('Index')['up'].agg(['sum','count'])
result_indices = summary[summary['sum'] > (summary['count']-summary['sum'])].index.tolist()
result = result_indices
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ly5gc8gPAIIyd1nME5L79fpn': ['index_info'], 'var_call_sBv8QfJyuc7e12FN2iTrBUmb': ['index_trade'], 'var_call_fCOSN88tLnVXSvtwMiN4VWTs': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_3e1Fa4X6TT18RONVt8OoqSKM': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_2tSNzB8Shi6bcNvjZWl36pP1': 'file_storage/call_2tSNzB8Shi6bcNvjZWl36pP1.json'}

exec(code, env_args)
