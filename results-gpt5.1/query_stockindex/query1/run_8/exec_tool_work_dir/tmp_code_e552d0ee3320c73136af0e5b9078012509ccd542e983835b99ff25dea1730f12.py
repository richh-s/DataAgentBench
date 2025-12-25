code = """import json, pandas as pd
from datetime import datetime

# Load full data from file
file_path = var_call_pJRGvra6NzVHEw0BtHU3I2af
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates to filter >= 2020-01-01 despite messy formats
parsed_dates = []
for d in df['Date']:
    parsed = None
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            parsed = datetime.strptime(d, fmt)
            break
        except Exception:
            continue
    parsed_dates.append(parsed)

df['ParsedDate'] = parsed_dates

# Filter
cutoff = datetime(2020,1,1)
mask = df['ParsedDate'].notna() & (df['ParsedDate'] >= cutoff)
recent = df[mask].copy()

# Compute intraday volatility
recent['vol'] = (recent['High'] - recent['Low']) / recent['Open']

# Map indices to regions using knowledge
asia_indices = ['N225','HSI','000001.SS','399001.SZ','NSEI','TWII','KOSPI','KOSPI2']

# Limit to Asia indices actually present
present_asia = [idx for idx in asia_indices if idx in recent['Index'].unique()]

result = (
    recent[recent['Index'].isin(present_asia)]
    .groupby('Index')['vol']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

answer = {
    'asia_indices_present': present_asia,
    'average_intraday_volatility_since_2020': result.to_dict(orient='records')
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d5C4nxzHM73VnyxkdCxXAnZK': ['index_info'], 'var_call_ogZ4zDfbJrnEJwihjlVJQnPE': ['index_trade'], 'var_call_b3tx8jBvjGiUbP2TEFfHeRno': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_XSKkwSwwcVkZ0KoNgSAUg8Qn': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_pJRGvra6NzVHEw0BtHU3I2af': 'file_storage/call_pJRGvra6NzVHEw0BtHU3I2af.json'}

exec(code, env_args)
