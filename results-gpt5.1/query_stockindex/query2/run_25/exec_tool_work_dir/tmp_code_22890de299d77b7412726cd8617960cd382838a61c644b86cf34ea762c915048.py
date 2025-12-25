code = """import json, pandas as pd

# Load full 2018 trades
with open(var_call_vrlUO8UvNBp2AP64UjqF75BK, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine regions for indices using geographic knowledge
# Indices in dataset: J203.JO (South Africa), IXIC (NASDAQ, USA), N225 (Japan), GSPTSE (Canada),
# NSEI (India), GDAXI (Germany), NYA (NYSE Composite, USA), HSI (Hong Kong), N100 (Euronext 100, Europe),
# 399001.SZ (China), 000001.SS (China), SSMI (Switzerland), TWII (Taiwan)

north_american_indices = ['IXIC', 'NYA', 'GSPTSE']

# Filter for North American indices
na_df = df[df['Index'].isin(north_american_indices)].copy()

# Classify days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()

summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary[summary['more_up_than_down']]['Index'].tolist()

out = {
    'north_american_indices': north_american_indices,
    'summary': summary.to_dict(orient='records'),
    'indices_with_more_up_than_down': result
}

res_str = json.dumps(out)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_wAnkbZoY1AefV55H5VxqNEH9': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_0bBBcSkZs1bmCvt0arA0eebk': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_vrlUO8UvNBp2AP64UjqF75BK': 'file_storage/call_vrlUO8UvNBp2AP64UjqF75BK.json'}

exec(code, env_args)
