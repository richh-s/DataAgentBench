code = """import json, pandas as pd

# load full index_trade data from file
path = var_call_LKaGXdAFC01R0X68p8TzQJxW
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
# parse date robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# filter since 2020
df = df[df['Date'] >= '2020-01-01']
# compute intraday volatility
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']
# focus on Asia indices: known mappings
asia_indices = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': '^NSEI',
    'Korea Exchange': '^KS11',
    'Taiwan Stock Exchange': '^TWII'
}

# subset to these symbols
df_asia = df[df['Index'].isin(asia_indices.values())]
result = df_asia.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

answer = {
    'avg_intraday_vol_by_index': result.to_dict(),
    'highest_index': result.index[0] if len(result)>0 else None,
    'highest_avg_intraday_vol': float(result.iloc[0]) if len(result)>0 else None
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_plbcEx0HCXXxLjaJFxIGqfRM': ['index_info'], 'var_call_sG8fRCtDSPj658RHs6w1EOBv': ['index_trade'], 'var_call_O1BgLP1681HWOoESij76Mo5E': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_LKaGXdAFC01R0X68p8TzQJxW': 'file_storage/call_LKaGXdAFC01R0X68p8TzQJxW.json'}

exec(code, env_args)
