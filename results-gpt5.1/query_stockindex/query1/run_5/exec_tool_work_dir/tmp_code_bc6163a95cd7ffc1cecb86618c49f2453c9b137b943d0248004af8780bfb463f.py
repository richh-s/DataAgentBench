code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_HO3zDozEnyzZAaEyNqJu4kxa
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# normalize date and filter since 2020-01-01
# handle multiple date formats

def parse_date(x):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

cutoff = datetime(2020,1,1)
mask = df['Date_parsed'] >= cutoff
recent = df[mask].copy()

# compute intraday volatility
recent['vol'] = (recent['High'] - recent['Low']) / recent['Open']

avg_vol = recent.groupby('Index')['vol'].mean().reset_index()

# map indices to regions using knowledge
asia_indices = {'N225','HSI','000001.SS','399001.SZ','^BSESN','KOSPI','TWII'}

asia_avg = avg_vol[avg_vol['Index'].isin(asia_indices)].sort_values('vol', ascending=False)

result = {
    'asia_ranking': asia_avg.to_dict(orient='records')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TAUaovZQkUJ8EngXGy2lZBam': ['index_info'], 'var_call_1LmQVuwBTBD67jmmYr5CiiD2': ['index_trade'], 'var_call_r3mT1phTQQfUA5LaWkaBp5QQ': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_HO3zDozEnyzZAaEyNqJu4kxa': 'file_storage/call_HO3zDozEnyzZAaEyNqJu4kxa.json'}

exec(code, env_args)
