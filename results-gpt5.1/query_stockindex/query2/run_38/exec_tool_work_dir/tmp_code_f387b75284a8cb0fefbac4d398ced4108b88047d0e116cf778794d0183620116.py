code = """import json, pandas as pd, os

path = var_call_goUQCPaD5tbEMGMUxjnEPZvG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

north_american_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(north_american_indices)].copy()

summary = {}
for idx, grp in na_df.groupby('Index'):
    up = (grp['Close'] > grp['Open']).sum()
    down = (grp['Close'] < grp['Open']).sum()
    summary[idx] = {'up_days': int(up), 'down_days': int(down), 'more_up_than_down': bool(up > down)}

result = summary

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pkktpiVQPbQCG9hGHrJopHpR': ['index_info'], 'var_call_tMrXKtJvv5bYyPOQ19V9JEIp': ['index_trade'], 'var_call_dpp9HOIcWJ3T77VpEGdReWv3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_eWkoJm2ZRvu27ePJ6YbZ0kzW': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_goUQCPaD5tbEMGMUxjnEPZvG': 'file_storage/call_goUQCPaD5tbEMGMUxjnEPZvG.json'}

exec(code, env_args)
