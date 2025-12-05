code = """import json, pandas as pd

path = var_call_9y03z6hGr4ZBXi9tpgn246CB
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

is_up = df['Close'] > df['Open']
is_down = df['Close'] < df['Open']

summary = df.groupby('Index').agg(up_days = ('Close', lambda s: int((df.loc[s.index, 'Close'] > df.loc[s.index, 'Open']).sum())),
                                  down_days = ('Close', lambda s: int((df.loc[s.index, 'Close'] < df.loc[s.index, 'Open']).sum())))

summary['more_up_than_down'] = summary['up_days'] > summary['down_days']
result = summary.reset_index().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8FSLSxyQrYbbVhsTXaj0og0w': ['index_info'], 'var_call_NuQmf9wisqG93eQ5bBhYbacs': ['index_trade'], 'var_call_6C7O3Fh5bmHamhnbGoYWfqMH': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_GywNJaCWVx6Ham3goSnKqRcb': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_9y03z6hGr4ZBXi9tpgn246CB': 'file_storage/call_9y03z6hGr4ZBXi9tpgn246CB.json'}

exec(code, env_args)
