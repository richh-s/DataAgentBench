code = """import json, pandas as pd

file_path = var_call_yQV9VUh3AykKrvT8E2SiZcqD
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter dates since 2020-01-01 (string includes earlier dates due to query quirk); parse and filter
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date_parsed'] >= '2020-01-01']

# Compute intraday volatility
df = df[df['Open'] > 0]
df['vol'] = (df['High'] - df['Low']) / df['Open']

avg_vol = df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = avg_vol.reset_index().to_dict(orient='records')

out = json.dumps({'avg_intraday_vol_by_index': result})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_WfEs6juHOs41b9mxJDYqOr23': ['index_info'], 'var_call_n7QyTWxdQjWhLIrAZYBlnORG': ['index_trade'], 'var_call_2X1zTzJNQUSlzevAgH8AzzrI': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_haS1578moaPKB4MEhQLK4lOe': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}], 'var_call_UxsDsP261TmgIcqKLpaG2rOT': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII']}, 'var_call_yQV9VUh3AykKrvT8E2SiZcqD': 'file_storage/call_yQV9VUh3AykKrvT8E2SiZcqD.json'}

exec(code, env_args)
