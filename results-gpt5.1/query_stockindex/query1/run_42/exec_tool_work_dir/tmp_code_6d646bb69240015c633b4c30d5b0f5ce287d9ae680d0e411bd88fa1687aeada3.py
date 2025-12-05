code = """import json, pandas as pd
from datetime import datetime

path = var_call_awjw8AXoymGjDHF7DaAwxfDC
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates robustly and filter from 2020-01-01
def parse_date(x):
    for fmt in ["%Y-%m-%d", "%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p"]:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

df = df[~df['Date_parsed'].isna()]
start = datetime(2020,1,1)
df = df[df['Date_parsed'] >= start]

# Convert to float
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Open','High','Low'])

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions manually using prior knowledge
asia_indices = set(['N225','HSI','000001.SS','399001.SZ','NSEI','TWII'])

asia_df = df[df['Index'].isin(asia_indices)]

result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

out = result.reset_index().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nlPAca7qclljLjuqANJ8PUly': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_qwBT8F2FEbKQFKTF4kwdAbEj': ['index_info'], 'var_call_TIRmf8oa3ERddDPCXL3KnaSO': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_awjw8AXoymGjDHF7DaAwxfDC': 'file_storage/call_awjw8AXoymGjDHF7DaAwxfDC.json'}

exec(code, env_args)
