code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_o9yK6FRjHXBXmUwdMEU7albI)
records = json.loads(path.read_text())

df = pd.DataFrame(records)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col])

na_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(na_indices)].copy()

up_down = na_df.assign(
    up = lambda x: x['Close'] > x['Open'],
    down = lambda x: x['Close'] < x['Open']
).groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()

result = up_down.assign(more_up_than_down=lambda x: x['up_days'] > x['down_days']).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lGPPCd7nTpmAFuofQc0xS83Q': ['index_info'], 'var_call_kqUsTUwSrMRddGHO8eG1I40H': ['index_trade'], 'var_call_xNVV0Bhz4t7wBqOIssah7FA9': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_GVfU3qT1XnhZBAGhtdvrWQaJ': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_o9yK6FRjHXBXmUwdMEU7albI': 'file_storage/call_o9yK6FRjHXBXmUwdMEU7albI.json'}

exec(code, env_args)
