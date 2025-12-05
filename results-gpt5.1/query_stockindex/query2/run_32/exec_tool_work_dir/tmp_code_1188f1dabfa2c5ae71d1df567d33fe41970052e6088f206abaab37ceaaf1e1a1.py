code = """import json, pandas as pd

path = var_call_5MksHchG626sR5GCo6hbgWTt
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american = ['NYA','IXIC','GSPTSE']
sub = df[df['Index'].isin(north_american)].copy()

res = []
for idx, g in sub.groupby('Index'):
    up = (g['Close'] > g['Open']).sum()
    down = (g['Close'] < g['Open']).sum()
    if up > down:
        res.append({'Index': idx, 'up_days': int(up), 'down_days': int(down)})

result = json.dumps(res)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_9I0THQ9sousvfmLjowkEuzh2': ['index_info'], 'var_call_Kwu0snAbpFHnwluHnQgtCap5': ['index_trade'], 'var_call_K1Hy400sGtigAEJ9shzYsY5k': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_ncd6dHBS1SCPxvvcU1iGekvX': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': 'IXIC'}], 'var_call_5MksHchG626sR5GCo6hbgWTt': 'file_storage/call_5MksHchG626sR5GCo6hbgWTt.json'}

exec(code, env_args)
