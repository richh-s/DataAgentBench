code = """import pandas as pd, json

# Load full trade data from file path
import os
file_path = var_call_SLh5bFvRl3sxdCoEJI1B7zsc
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse date to filter since 2020-01-01
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df_2020 = df[mask].copy()

# Compute intraday volatility
df_2020['vol'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Filter for Asian indices based on index symbol mapping (from domain knowledge and exchanges list)
# Asia indices present in this dataset likely: N225 (Tokyo), HSI (Hong Kong), 000001.SS (Shanghai), 399001.SZ or similar (Shenzhen),
# NIFTY or ^NSEI (National Stock Exchange of India), KS11 (Korea Exchange), TWII (Taiwan), etc.

asian_indices = [
    'N225',      # Nikkei 225 - Tokyo Stock Exchange (Japan)
    'HSI',       # Hang Seng Index - Hong Kong Stock Exchange (Hong Kong)
    '000001.SS', # SSE Composite - Shanghai Stock Exchange (China)
    '399001.SZ', # Shenzhen Component Index - Shenzhen Stock Exchange (China)
    '^NSEI',     # NIFTY 50 - National Stock Exchange of India (India)
    'KS11',      # KOSPI - Korea Exchange (South Korea)
    '^TWII',     # TAIEX - Taiwan Stock Exchange (Taiwan)
]

asian_df = df_2020[df_2020['Index'].isin(asian_indices)].copy()

# If some of these symbols are not in data, restrict to actually present ones
present_asian_indices = asian_df['Index'].unique().tolist()

avg_vol = asian_df.groupby('Index')['vol'].mean().reset_index()

if not avg_vol.empty:
    # Find index with highest avg volatility
    max_row = avg_vol.loc[avg_vol['vol'].idxmax()]
    result = {
        'asian_indices_present': present_asian_indices,
        'highest_vol_index': max_row['Index'],
        'highest_avg_intraday_volatility': max_row['vol']
    }
else:
    # If our guessed symbols didn't match, compute for all indices and then we will interpret manually
    avg_vol_all = df_2020.groupby('Index')['vol'].mean().reset_index()
    if avg_vol_all.empty:
        result = {
            'error': 'No data since 2020 after cleaning.'
        }
    else:
        max_row = avg_vol_all.loc[avg_vol_all['vol'].idxmax()]
        result = {
            'asian_indices_present': [],
            'highest_vol_index_all': max_row['Index'],
            'highest_avg_intraday_volatility_all': max_row['vol']
        }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mXRC6R7etpA28XGPmqqPgFNj': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_SLh5bFvRl3sxdCoEJI1B7zsc': 'file_storage/call_SLh5bFvRl3sxdCoEJI1B7zsc.json'}

exec(code, env_args)
