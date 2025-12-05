code = """import json, pandas as pd

path = var_call_IQgRytpCryEWNzECKXkL32pq
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(north_american_indices)].copy()

up_down = na_df.assign(
    up = na_df['Close'] > na_df['Open'],
    down = na_df['Close'] < na_df['Open']
).groupby('Index').agg({'up':'sum','down':'sum'})

more_up = up_down[up_down['up'] > up_down['down']].index.tolist()

result = {
  'indices_with_more_up_than_down_days_in_2018_North_America': more_up,
  'details': up_down.to_dict(orient='index')
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_eKWz9rylokab7mXmJPXNbPv9': ['index_info'], 'var_call_qaM6yIPOTy9Ha6BChZU9sBT8': ['index_trade'], 'var_call_Es0H0TN2FBugrP482tSoY81I': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_Mnjy9AhjmAwwasaGs4F96C0g': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': 'IXIC'}], 'var_call_IQgRytpCryEWNzECKXkL32pq': 'file_storage/call_IQgRytpCryEWNzECKXkL32pq.json'}

exec(code, env_args)
