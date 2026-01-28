code = """import pandas as pd
import json

# Load the query result stored in the provided file path variable
with open(var_call_TZXThu6iajV9Zzz5o0syw6nD, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates robustly and filter for dates on/after 2020-01-01
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
start = pd.to_datetime('2020-01-01')
df = df[df['Date_parsed'] >= start]

# Convert numeric columns
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing or zero Open/High/Low
df = df.dropna(subset=['Open', 'High', 'Low'])
df = df[df['Open'] != 0]

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Group by index and compute mean volatility and counts
group = df.groupby('idx')['vol'].agg(['mean', 'count']).reset_index()

# If no data after filtering, prepare empty result
if group.empty:
    result = {'top_index': None, 'average_intraday_volatility': None, 'days': 0, 'per_index': {}}
else:
    top = group.loc[group['mean'].idxmax()]
    per_index = {row['idx']: {'mean': float(row['mean']), 'days': int(row['count'])} for _, row in group.iterrows()}
    result = {'top_index': str(top['idx']), 'average_intraday_volatility': float(top['mean']), 'days': int(top['count']), 'per_index': per_index}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zFHVXYXQlrTkQV7ncmbEjeI0': ['index_trade'], 'var_call_3iVSZI806irjFb88ImfcyqRf': ['index_info'], 'var_call_VaMxSHtwwmDf0Jk0iV4PTP7Y': [{'idx': '000001.SS'}, {'idx': '399001.SZ'}, {'idx': 'GDAXI'}, {'idx': 'GSPTSE'}, {'idx': 'HSI'}, {'idx': 'IXIC'}, {'idx': 'J203.JO'}, {'idx': 'N100'}, {'idx': 'N225'}, {'idx': 'NSEI'}, {'idx': 'NYA'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_TZXThu6iajV9Zzz5o0syw6nD': 'file_storage/call_TZXThu6iajV9Zzz5o0syw6nD.json'}

exec(code, env_args)
