code = """import json, pandas as pd, os

# Load full index_trade data from file path
path = var_call_ZRvGdt1RuDFDeUuEr7K3y7lE
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# filter from 2020-01-01 using string contains/parse
# Dates are strings in various formats; parse to datetime
df['Date_dt'] = pd.to_datetime(df['Date'], errors='coerce')
mask = df['Date_dt'] >= pd.Timestamp('2020-01-01')
df_2020 = df[mask].copy()

# Compute intraday volatility
df_2020['vol'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Average by index
avg_vol = df_2020.groupby('Index')['vol'].mean().reset_index()

# Identify Asian indices using geographic knowledge
asia_indices = {
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    'KS11': 'Korea Exchange',
    '^TWII': 'Taiwan Stock Exchange',
    '^NSEI': 'National Stock Exchange of India'
}

avg_vol_asia = avg_vol[avg_vol['Index'].isin(asia_indices.keys())].copy()

# find max
if not avg_vol_asia.empty:
    idxmax = avg_vol_asia['vol'].idxmax()
    row = avg_vol_asia.loc[idxmax]
    result = {
        'Index': row['Index'],
        'Exchange': asia_indices.get(row['Index'], None),
        'average_intraday_volatility': row['vol']
    }
else:
    result = None

out = json.dumps(result, default=float)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_XBgf8zcPILrOkEgV920W3XT9': ['index_info'], 'var_call_wV30fNv94PTsqmA7B9FiAXRi': ['index_trade'], 'var_call_sQyyeBO899kokhnYB1vTPBI4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_ZRvGdt1RuDFDeUuEr7K3y7lE': 'file_storage/call_ZRvGdt1RuDFDeUuEr7K3y7lE.json'}

exec(code, env_args)
