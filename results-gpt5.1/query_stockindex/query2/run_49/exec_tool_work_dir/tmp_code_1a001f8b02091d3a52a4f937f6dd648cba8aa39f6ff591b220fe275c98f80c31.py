code = """import json, pandas as pd

# Load full 2018 data from file
with open(var_call_jQgylKJ0Y1mM0p3Cd4s6cDj3, 'r') as f:
    data_2018 = json.load(f)

df = pd.DataFrame(data_2018)

# Ensure numeric types
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine up/down per row
df['up'] = df['Close'] > df['Open']
df['down'] = df['Close'] < df['Open']

# Aggregate per index
agg = df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()

# Map indices to regions manually using geographic knowledge
region_map = {
    'NYA': 'North America',      # New York Stock Exchange Composite
    'IXIC': 'North America',     # NASDAQ Composite
    'GSPTSE': 'North America',   # S&P/TSX Composite (Toronto)
    'N225': 'Asia',
    'HSI': 'Asia',
    '000001.SS': 'Asia',
    '399001.SZ': 'Asia',
    'NSEI': 'Asia',
    'GDAXI': 'Europe',
    'N100': 'Europe',
    'SSMI': 'Europe',
    'TWII': 'Asia',
    'J203.JO': 'Africa',
}

agg['region'] = agg['Index'].map(region_map)

# Filter to North America and up_days > down_days
north_america = agg[agg['region'] == 'North America']
result_df = north_america[north_america['up_days'] > north_america['down_days']]

result = result_df[['Index', 'up_days', 'down_days']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gmrQlf1kwr2EsEBEbQaHBobn': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_GP7VrL0LtyzXHVkiQjVqt68H': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_jQgylKJ0Y1mM0p3Cd4s6cDj3': 'file_storage/call_jQgylKJ0Y1mM0p3Cd4s6cDj3.json'}

exec(code, env_args)
