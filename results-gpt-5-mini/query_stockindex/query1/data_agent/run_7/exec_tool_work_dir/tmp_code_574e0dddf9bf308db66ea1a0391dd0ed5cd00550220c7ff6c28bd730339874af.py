code = """import pandas as pd
import json

# Load query result JSON file
path = var_call_mQX70dPyez8dKiI4P8i89qJn

df = pd.read_json(path)

# Normalize column names if needed
# Convert numeric columns
for col in ['Open','High','Low']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates robustly
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for dates since 2020-01-01
df = df[df['Date'] >= pd.to_datetime('2020-01-01')]

# Drop rows with missing or zero Open
df = df.dropna(subset=['Open','High','Low','Date'])
df = df[df['Open'] != 0]

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and compute mean volatility and counts
grp = df.groupby('Index').agg(mean_vol=('vol','mean'), count=('vol','count')).reset_index()

# Prepare output
averages = {row['Index']: round(float(row['mean_vol']), 6) for _, row in grp.iterrows()}
counts = {row['Index']: int(row['count']) for _, row in grp.iterrows()}

if not grp.empty:
    top_row = grp.loc[grp['mean_vol'].idxmax()]
    top_index = top_row['Index']
    top_avg = round(float(top_row['mean_vol']), 6)
else:
    top_index = None
    top_avg = None

result = {
    'averages': averages,
    'counts': counts,
    'top_index': top_index,
    'top_avg': top_avg
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bUo6Q5TTnJ76YCJsVBXc7vUJ': ['index_trade'], 'var_call_QAG7xH5xPV7qPi6qE3CSKIUu': ['index_info'], 'var_call_UoZejKdrwjUIMbaCVbC1nXof': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_mQX70dPyez8dKiI4P8i89qJn': 'file_storage/call_mQX70dPyez8dKiI4P8i89qJn.json'}

exec(code, env_args)
