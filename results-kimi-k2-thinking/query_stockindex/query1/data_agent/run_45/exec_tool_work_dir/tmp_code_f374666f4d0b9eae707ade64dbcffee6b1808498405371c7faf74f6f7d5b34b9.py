code = """import json, pandas as pd
from datetime import datetime

# Load data
trade_file = globals()['var_functions.query_db:3']
with open(trade_file, 'r') as f:
    trade = json.load(f)

df = pd.DataFrame(trade)

# Convert numeric columns to float
for col in ['Open', 'High', 'Low', 'Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
# Try multiple formats

def try_parse_date(s):
    s = str(s)
    try:
        # Try pandas parser with dayfirst=False
        return pd.to_datetime(s, dayfirst=False, errors='coerce')
    except Exception:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(try_parse_date)

# Filter from 2020 onward
df_2020 = df[df['Date_parsed'] >= datetime(2020, 1, 1)].copy()

# Compute intraday volatility
df_2020['IntradayVol'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Define Asia indices (based on known mapping)
asia_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII']
# Filter Asia indices present in data
asia_df = df_2020[df_2020['Index'].isin(asia_indices)]

# Compute average intraday volatility per index
avg_vol = asia_df.groupby('Index')['IntradayVol'].mean().sort_values(ascending=False)

result = {
    'avg_intraday_volatility': {idx: float(avg_vol[idx]) for idx in avg_vol.index},
    'highest_index': avg_vol.idxmax(),
    'highest_value': float(avg_vol.max())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:26': {'records': 14, 'sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}]}, 'var_functions.execute_python:28': {'unique_indices': ['HSI', 'NYA', 'IXIC', '000001.SS', 'N225', 'N100', '399001.SZ', 'GSPTSE', 'NSEI', 'GDAXI', 'SSMI', 'TWII', 'J203.JO'], 'asia_map': {'Tokyo Stock Exchange': ['N225'], 'Hong Kong Stock Exchange': ['HSI'], 'Shanghai Stock Exchange': ['000001.SS', '000002.SS', '000300.SS'], 'Shenzhen Stock Exchange': ['399001.SZ', '399006.SZ'], 'National Stock Exchange of India': ['NSEI', '^NSEI', 'NIFTY'], 'Korea Exchange': ['KS11', '^KS11', 'KOSPI'], 'Taiwan Stock Exchange': ['TWII', '^TWII']}, 'records_2020': 3638}}

exec(code, env_args)
