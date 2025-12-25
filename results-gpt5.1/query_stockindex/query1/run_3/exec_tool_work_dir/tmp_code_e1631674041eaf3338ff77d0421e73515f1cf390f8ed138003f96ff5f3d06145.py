code = """import json, pandas as pd
from datetime import datetime

# Load full trade data from file
file_path = var_call_NFag8R2yaBEOArFKaGCddMB4
with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates robustly and filter since 2020-01-01
# Dates appear in multiple string formats; use pandas to_datetime with errors='coerce'
df['DateParsed'] = pd.to_datetime(df['Date'], errors='coerce')
cutoff = pd.Timestamp('2020-01-01')
df = df[df['DateParsed'] >= cutoff].copy()

# Compute intraday volatility (High - Low) / Open
df['Vol'] = (df['High'] - df['Low']) / df['Open']

# Drop rows with invalid Vol
df = df[df['Vol'].notna() & (df['Open'] != 0)]

# Map indices to regions using geographic knowledge.
# We'll inspect unique indices first to know what we have.
unique_indices = sorted(df['Index'].unique().tolist())

# Hard-code mapping for known indices in this dataset.
# Based on typical major indices corresponding to exchanges in indexinfo_database.
region_map = {
    'N225': 'Asia',        # Tokyo Stock Exchange, Japan
    'HSI': 'Asia',         # Hong Kong Stock Exchange, Hong Kong
    '000001.SS': 'Asia',   # Shanghai Stock Exchange Composite, China
    '399001.SZ': 'Asia',   # Shenzhen Component, China
    '399006.SZ': 'Asia',   # ChiNext, China
    '^NSEI': 'Asia',       # Nifty 50, India (symbol example)
    '^KS11': 'Asia',       # KOSPI, Korea
    '^TWII': 'Asia',       # TAIEX, Taiwan
    # Non-Asia examples (for completeness if present)
    '^GSPC': 'North America',
    '^DJI': 'North America',
    '^IXIC': 'North America',
    '^GDAXI': 'Europe',
    '^FCHI': 'Europe',
    '^STOXX50E': 'Europe',
    '^GSPTSE': 'North America',
}

# Assign region, default to 'Other'
df['Region'] = df['Index'].map(region_map).fillna('Other')

# Filter to Asia region
asia = df[df['Region'] == 'Asia'].copy()

if asia.empty:
    result = {"error": "No Asia-region indices found in the dataset after 2020."}
else:
    # Average intraday volatility per index
    avg_vol = asia.groupby('Index')['Vol'].mean().reset_index()
    top_row = avg_vol.sort_values('Vol', ascending=False).iloc[0]
    result = {
        'top_index': top_row['Index'],
        'average_intraday_volatility': float(top_row['Vol']),
        'all_asia_indices_ranked': avg_vol.sort_values('Vol', ascending=False).to_dict(orient='records')
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TI4iMsWgC08kX3ZbPuND6kNz': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_NFag8R2yaBEOArFKaGCddMB4': 'file_storage/call_NFag8R2yaBEOArFKaGCddMB4.json'}

exec(code, env_args)
