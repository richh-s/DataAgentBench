code = """import json, pandas as pd

# load full index_trade data from file
path = var_call_7c2s2XSl7JVKjGE6IkEYRUMT
with open(path, 'r') as f:
    index_trade = json.load(f)

# to ensure we only use data since 2020-01-01, filter on Date by parsing year where possible
# Dates look messy; but dataset already filtered in SQL, so proceed.

df = pd.DataFrame(index_trade)

# coerce numeric columns
for col in ['Open','High','Low','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# drop rows with invalid Open or High/Low
df = df.dropna(subset=['Open','High','Low'])

# compute intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# map Asia-region indices based on known major exchanges in index_info
asia_indices = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': '^NSEI',
    'Korea Exchange': '^KS11',
    'Taiwan Stock Exchange': '^TWII'
}

asian_index_symbols = list(asia_indices.values())

asia_df = df[df['Index'].isin(asian_index_symbols)]

result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

answer = {
    'average_intraday_vol_by_index': result.to_dict(),
    'highest_vol_index': result.index[0] if len(result)>0 else None
}

out = json.dumps(answer)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_MNsBi52ooCqwDvBbNALuhoPS': ['index_info'], 'var_call_rCPzRsTPhECDYQIN0c0iFKaH': ['index_trade'], 'var_call_sZegIzRpLeaKMNNnnDsoPJSM': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_7c2s2XSl7JVKjGE6IkEYRUMT': 'file_storage/call_7c2s2XSl7JVKjGE6IkEYRUMT.json'}

exec(code, env_args)
