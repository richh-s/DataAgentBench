code = """import json
import pandas as pd

# Load the full query result from the JSON file path provided in storage
path = var_call_mWUMMKaudSVlyw5NUjLUyPhR
with open(path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure numeric types
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Determine up and down days
df['up'] = (df['Close'] > df['Open']).astype(int)
df['down'] = (df['Close'] < df['Open']).astype(int)

# Aggregate by Index
group = df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()

# Indices with more up days than down days
res_indices = group[group['up_days'] > group['down_days']]['Index'].tolist()

output = {
    'indices_more_up_than_down': res_indices,
    'counts': group.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Mx94o3NlvHwsNvNb3oKak6PD': ['index_trade'], 'var_call_PCEhHfycYWpHWkSDHEWYxyiQ': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_mWUMMKaudSVlyw5NUjLUyPhR': 'file_storage/call_mWUMMKaudSVlyw5NUjLUyPhR.json'}

exec(code, env_args)
