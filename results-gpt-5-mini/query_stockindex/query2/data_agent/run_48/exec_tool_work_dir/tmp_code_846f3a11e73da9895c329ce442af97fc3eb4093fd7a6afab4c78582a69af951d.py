code = """import json
import pandas as pd
path = var_call_69rkbZXFvsPGvNgEsBF2DZXV
with open(path, 'r') as f:
    records = json.load(f)

# build dataframe
df = pd.DataFrame(records)
# convert numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
# drop missing
df = df.dropna(subset=['Open','Close'])
# ensure 2018
if 'Date' in df.columns:
    df = df[df['Date'].astype(str).str.startswith('2018')]
# compute up/down counts per Index
group = df.groupby('Index').apply(lambda g: pd.Series({'up': int((g['Close']>g['Open']).sum()), 'down': int((g['Close']<g['Open']).sum())})).reset_index()
# North American indices from index_info: NYSE -> NYA, NASDAQ -> IXIC, Toronto -> GSPTSE
north = ['IXIC','NYA','GSPTSE']
group_north = group[group['Index'].isin(north)].copy()
more_up = group_north[group_north['up']>group_north['down']]['Index'].tolist()
res = {'counts': group_north.to_dict(orient='records'), 'more_up_indices': more_up}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Utml8TGbeS8Cb2IhqfVb0ZwI': ['index_info'], 'var_call_aY1zDKf1dm70elWEKo7rzjXt': ['index_trade'], 'var_call_k5dLsDsojVy7yjhYyIeWDlI5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_69rkbZXFvsPGvNgEsBF2DZXV': 'file_storage/call_69rkbZXFvsPGvNgEsBF2DZXV.json', 'var_call_PGAobuBQy2A170H14KGcw7Rx': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}]}

exec(code, env_args)
