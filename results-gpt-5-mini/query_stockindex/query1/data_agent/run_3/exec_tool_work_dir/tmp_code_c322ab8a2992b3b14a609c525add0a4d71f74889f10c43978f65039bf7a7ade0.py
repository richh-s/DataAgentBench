code = """import json
import pandas as pd

# Load the query result from storage
path = var_call_fpWOycSzPFNXoWKut97X9j66
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)

# Keep relevant columns and coerce numeric
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates robustly
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)

# For any rows still NaT, try more parsing attempts (strip timezone words)
def try_parse(x):
    if pd.isna(x):
        return pd.NaT
    s = str(x)
    # remove ' at 12:00 AM' or similar
    s = s.replace(' at 12:00 AM', '')
    s = s.replace(', 00:00', '')
    try:
        return pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
    except:
        return pd.NaT

mask_nat = df['Date_parsed'].isna()
if mask_nat.any():
    df.loc[mask_nat, 'Date_parsed'] = df.loc[mask_nat, 'Date'].apply(try_parse)

# Filter to dates since 2020-01-01
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')].copy()

# Compute intraday volatility (High - Low) / Open
# Avoid division by zero or missing
df = df[df['Open'].notna() & df['High'].notna() & df['Low'].notna()]

df = df[df['Open'] != 0]

df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and compute average intraday volatility and count
group = df.groupby('Index').agg(avg_intraday_vol=('intraday_vol', 'mean'), days=('intraday_vol','count'))

group = group.reset_index()

# Keep only Asia indices present in the earlier selection
asia_indices = ['000001.SS','399001.SZ','HSI','N225','NSEI','TWII']
group = group[group['Index'].isin(asia_indices)].copy()

# If no data, return an explanatory result
if group.empty:
    result = {"error": "No data for Asia indices since 2020 after parsing dates."}
else:
    # Find index with highest average intraday volatility
    top = group.sort_values('avg_intraday_vol', ascending=False).iloc[0]
    result = {
        'index': top['Index'],
        'avg_intraday_vol': float(top['avg_intraday_vol']),
        'days_used': int(top['days'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gRBqPUB8t8WEDetiQTT4Wmgn': ['index_trade'], 'var_call_7PfQPmrqjmGgRfOVzylIGULF': ['index_info'], 'var_call_5Gb40QjfFc9WvJo6SuSBdnTy': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_fpWOycSzPFNXoWKut97X9j66': 'file_storage/call_fpWOycSzPFNXoWKut97X9j66.json'}

exec(code, env_args)
