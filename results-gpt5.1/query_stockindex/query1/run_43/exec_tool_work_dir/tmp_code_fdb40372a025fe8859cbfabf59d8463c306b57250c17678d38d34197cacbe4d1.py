code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_HZivQxb15NgHieMlKFpotm5K
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# coerce numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse dates to filter since 2020-01-01
# dates are messy strings; let pandas infer
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')

mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# map indices to regions (Asia vs others) based on domain knowledge
asia_indices = {
    'HSI',        # Hong Kong Stock Exchange
    '000001.SS',  # Shanghai SE Composite
    '399001.SZ',  # Shenzhen SE Component
    'N225',       # Nikkei 225 (Tokyo)
    '^NSEI',      # Nifty 50 (India NSE) often coded as ^NSEI
    '^BSESN',     # Sensex (BSE India) if present
    '^KS11',      # KOSPI (Korea)
    '^TWII',      # TAIEX (Taiwan)
}

# keep only those indices that are in Asia set (intersection with existing)
existing_indices = set(df['Index'].unique())
selected_asia = sorted(list(existing_indices.intersection(asia_indices)))

asia_df = df[df['Index'].isin(selected_asia)].copy()

result = {}
if not asia_df.empty:
    avg_vol = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)
    result['ranking'] = avg_vol.to_dict()
    result['top_index'] = avg_vol.index[0]
    result['top_avg_intraday_vol'] = float(avg_vol.iloc[0])
else:
    result['error'] = 'No Asia indices found in data.'

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_jPgGixsD6fgML2CsVRecn2tr': ['index_info'], 'var_call_ymyvzMyAcSVPguXNhwmvNIY9': ['index_trade'], 'var_call_XxffXMTkmCNLnuOhpfnu5lzR': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_HZivQxb15NgHieMlKFpotm5K': 'file_storage/call_HZivQxb15NgHieMlKFpotm5K.json'}

exec(code, env_args)
