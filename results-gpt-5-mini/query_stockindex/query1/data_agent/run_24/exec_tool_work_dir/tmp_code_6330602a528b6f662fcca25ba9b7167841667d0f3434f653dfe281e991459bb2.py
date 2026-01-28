code = """import json
import pandas as pd

# Load the large query result from the provided file path variable
fn = var_call_phSmNixNYd34T2gp0hJXw4AP
with open(fn, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure expected columns exist
if 'index_symbol' not in df.columns:
    # try alternate name
    if 'Index' in df.columns:
        df = df.rename(columns={'Index':'index_symbol'})

# Parse dates robustly and filter for dates since 2020-01-01
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
start_date = pd.to_datetime('2020-01-01')
df = df[df['Date_parsed'] >= start_date]

# Convert numeric columns
for col in ['Open', 'High', 'Low']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        df[col] = pd.NA

# Remove rows with invalid or zero Open
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Group by index and compute average volatility and counts
grouped = df.groupby('index_symbol')['vol'].agg(['mean','count']).reset_index()
# Prepare results
by_index = {row['index_symbol']: (None if pd.isna(row['mean']) else float(row['mean'])) for _, row in grouped.iterrows()}

if len(grouped) == 0:
    result = {"error": "No data for dates since 2020-01-01 after filtering and cleaning."}
else:
    top = grouped.loc[grouped['mean'].idxmax()]
    top_index = top['index_symbol']
    top_mean = float(top['mean'])
    top_count = int(top['count'])

    result = {
        'top_index': top_index,
        'average_intraday_volatility': top_mean,
        'data_points': top_count,
        'by_index': by_index
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jAIirGx2UG4WZxBoHRlWqA0E': ['index_info'], 'var_call_s84GjUFnMuDrxPjrpnD2JgEc': ['index_trade'], 'var_call_f0QWGbLafrzIcE762r9wcBTI': [{'index_symbol': '000001.SS'}, {'index_symbol': '399001.SZ'}, {'index_symbol': 'GDAXI'}, {'index_symbol': 'GSPTSE'}, {'index_symbol': 'HSI'}, {'index_symbol': 'IXIC'}, {'index_symbol': 'J203.JO'}, {'index_symbol': 'N100'}, {'index_symbol': 'N225'}, {'index_symbol': 'NSEI'}, {'index_symbol': 'NYA'}, {'index_symbol': 'SSMI'}, {'index_symbol': 'TWII'}], 'var_call_phSmNixNYd34T2gp0hJXw4AP': 'file_storage/call_phSmNixNYd34T2gp0hJXw4AP.json'}

exec(code, env_args)
