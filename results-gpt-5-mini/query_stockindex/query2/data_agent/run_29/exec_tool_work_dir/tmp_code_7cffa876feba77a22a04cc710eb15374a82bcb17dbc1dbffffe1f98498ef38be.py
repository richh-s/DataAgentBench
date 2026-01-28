code = """import json
import pandas as pd

# Load the large query result from the JSON file path stored in the provided variable
path = var_call_gIU3iIVENibCqA6kbv0hzfpD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure numeric types
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Define North American indices present in the dataset
na_indices = ['IXIC', 'NYA', 'GSPTSE']

# Filter to 2018 (already filtered in query) and North American indices
df_na = df[df['Index'].isin(na_indices)].copy()

# Compute up/down/equal days
df_na['up'] = (df_na['Close'] > df_na['Open']).astype(int)
df_na['down'] = (df_na['Close'] < df_na['Open']).astype(int)
df_na['equal'] = (df_na['Close'] == df_na['Open']).astype(int)

# Aggregate counts per index
agg = df_na.groupby('Index')[['up','down','equal']].sum().reset_index()

# Identify indices with more up days than down days
more_up = agg[agg['up'] > agg['down']]['Index'].tolist()

# Prepare result
result = {
    'more_up_indices': more_up,
    'counts': agg.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l0c2o9f1LluUdaZeITIjfJkK': ['index_trade'], 'var_call_gIU3iIVENibCqA6kbv0hzfpD': 'file_storage/call_gIU3iIVENibCqA6kbv0hzfpD.json', 'var_call_HhtvcDUkhJarjgnYV6QVdUu8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
