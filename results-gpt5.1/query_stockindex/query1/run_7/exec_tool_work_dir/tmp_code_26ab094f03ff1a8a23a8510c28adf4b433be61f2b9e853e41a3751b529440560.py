code = """import json, pandas as pd
from datetime import datetime

# load full trade data from file
path = var_call_rlfdZsfCobwU4r6P3OJAHEqu
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse date; keep rows >= 2020-01-01
# dates seem messy; try pd.to_datetime with errors=coerce
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# keep only Asia indices based on symbol knowledge
asia_indices = ['N225','HSI','000001.SS','399001.SZ','^KS11','^TWII','^BSESN']

asia_df = df[df['Index'].isin(asia_indices)].copy()

# compute intraday volatility (High-Low)/Open, skip if Open<=0 or NaN
asia_df = asia_df[asia_df['Open']>0]
asia_df['vol'] = (asia_df['High'] - asia_df['Low']) / asia_df['Open']

result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False).reset_index()

answer = {
    'ranked_average_intraday_volatility_since_2020': result.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_xg9hcAADNeLCE1U9nr3pZBPG': ['index_info'], 'var_call_qQTSEYaCdxX6p641ybmQsKlz': ['index_trade'], 'var_call_7Mcwgz8dw8667dNo0m03J9eK': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_rlfdZsfCobwU4r6P3OJAHEqu': 'file_storage/call_rlfdZsfCobwU4r6P3OJAHEqu.json'}

exec(code, env_args)
