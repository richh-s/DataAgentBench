code = """import json, pandas as pd

data_path = var_call_hPHTlk67KFN24CNeyAuSSDpW
with open(data_path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Map indices to regions (North America only)
# From metadata: NYA (New York Stock Exchange, US), IXIC (NASDAQ, US), GSPTSE (Toronto Stock Exchange, Canada)
na_indices = ['NYA','IXIC','GSPTSE']

na_df = df[df['Index'].isin(na_indices)].copy()

na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary[summary['more_up_than_down']]['Index'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tQwNUQuDde7vGLa2eDTusead': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_BU2o1skxV4pxfvPfbFTJL4Kl': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_hPHTlk67KFN24CNeyAuSSDpW': 'file_storage/call_hPHTlk67KFN24CNeyAuSSDpW.json'}

exec(code, env_args)
