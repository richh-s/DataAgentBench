code = """import json
import pandas as pd

# Load data from the previous query result file
path = var_call_FDsmZSfmfdqh8wwfaSzWpznj
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns
for col in ['Open', 'High', 'Low']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates robustly
if 'Date' in df.columns:
    df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=False)
else:
    df['Date_parsed'] = pd.NaT

# Filter for dates since 2020-01-01
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# Remove invalid rows
df = df.dropna(subset=['Open', 'High', 'Low', 'Date_parsed'])
# Exclude non-positive Open
df = df[df['Open'] > 0]

# Compute intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and compute average volatility and count
grouped = df.groupby('Index').agg(average_intraday_volatility=('intraday_vol', 'mean'), count=('intraday_vol','count'))
# Reset index
grouped = grouped.reset_index()
# Sort descending by average volatility
grouped_sorted = grouped.sort_values('average_intraday_volatility', ascending=False)

# Prepare output
all_averages = grouped_sorted.to_dict(orient='records')
if len(all_averages) > 0:
    top = all_averages[0]
    top_index = top['Index']
    top_avg = top['average_intraday_volatility']
else:
    top_index = None
    top_avg = None

output = {
    'top_index': top_index,
    'average_intraday_volatility': top_avg,
    'all_averages': all_averages
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_BL7KBUGRSW0KmGWLmP2q4cJ8': ['index_trade'], 'var_call_7rZ7UDTIQi2qZMcbL6Bmek3O': ['index_info'], 'var_call_4yE3tDDz0XEtkNkMPGXznZRT': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_FDsmZSfmfdqh8wwfaSzWpznj': 'file_storage/call_FDsmZSfmfdqh8wwfaSzWpznj.json'}

exec(code, env_args)
