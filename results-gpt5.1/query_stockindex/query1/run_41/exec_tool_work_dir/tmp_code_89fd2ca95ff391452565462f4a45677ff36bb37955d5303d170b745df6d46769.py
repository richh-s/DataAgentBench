code = """import json, pandas as pd
from datetime import datetime

# load full large result
file_path = var_call_J1THC6lTRQP8sfqURFbcYI61
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# keep since 2020 only, parse messy dates
def parse_date(x):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return None

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df[df['Date_parsed'] >= datetime(2020,1,1)]

# convert numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# intraday volatility
df = df[df['Open']>0]
df['vol'] = (df['High'] - df['Low'])/df['Open']

# Asia indices mapping based on domain knowledge
asia_indices = {
    'N225':'Tokyo Stock Exchange',
    'HSI':'Hong Kong Stock Exchange',
    '000001.SS':'Shanghai Stock Exchange',
    '399001.SZ':'Shenzhen Stock Exchange',
    'NSEI':'National Stock Exchange of India',
    'TWII':'Taiwan Stock Exchange',
    'KS11':'Korea Exchange'
}

asia_df = df[df['Index'].isin(asia_indices.keys())]
res = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)
result = res.reset_index().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_BBqZsN7rO8aJkHryk1qz0k9C': ['index_info'], 'var_call_Gf5hnDn1Fvw3uVevneF0GG1X': ['index_trade'], 'var_call_1aCsh9zLrNMt3faRDTQml6I8': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_5Q2ZFp4BM6xBXd7MLKFU7E9y': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_J1THC6lTRQP8sfqURFbcYI61': 'file_storage/call_J1THC6lTRQP8sfqURFbcYI61.json'}

exec(code, env_args)
