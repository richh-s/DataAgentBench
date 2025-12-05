code = """import json, pandas as pd

# Load full index_trade data from file
file_path = var_call_c89fZTl9zBcOoU9JgsxPYCga
with open(file_path, 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    df_trade[col] = pd.to_numeric(df_trade[col], errors='coerce')

# Parse date and filter since 2020-01-01
# Dates have mixed formats; let pandas infer
df_trade['Date'] = pd.to_datetime(df_trade['Date'], errors='coerce')
mask = df_trade['Date'] >= pd.Timestamp('2020-01-01')
df_trade = df_trade[mask]

# Subset to major Asian indices using domain knowledge mapping
asian_indices = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',  # SSE Composite
    '399001.SZ': 'Shenzhen Stock Exchange',  # SZSE Component
    '^NSEI': 'National Stock Exchange of India',  # Nifty 50
    '^KS11': 'Korea Exchange',  # KOSPI
    '^TWII': 'Taiwan Stock Exchange',  # TAIEX
}

df_asia = df_trade[df_trade['Index'].isin(asian_indices.keys())].copy()

# Compute intraday volatility (High - Low) / Open
df_asia['vol'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Drop rows with invalid values
df_asia = df_asia.replace([float('inf'), float('-inf')], pd.NA).dropna(subset=['vol'])

# Average volatility per index
avg_vol = df_asia.groupby('Index')['vol'].mean().reset_index()

# Find index with highest avg volatility
idx_max = avg_vol.loc[avg_vol['vol'].idxmax()]
result = {
    'Index': idx_max['Index'],
    'Exchange': asian_indices.get(idx_max['Index'], None),
    'AverageIntradayVolatility': float(idx_max['vol'])
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zyVJLxGq3eGrqs7TW6GhZj6c': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_c89fZTl9zBcOoU9JgsxPYCga': 'file_storage/call_c89fZTl9zBcOoU9JgsxPYCga.json'}

exec(code, env_args)
