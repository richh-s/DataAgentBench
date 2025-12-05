code = """import json, pandas as pd
from datetime import datetime

# Load trades
path = var_call_ZgsA5y01aBz6TgXtehJOxaS0
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date to ISO and filter >= 2020-01-01
def parse_date(x):
    for fmt in ["%Y-%m-%d", "%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p"]:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return None

df['Date_dt'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date_dt'])
start = datetime(2020,1,1)
df = df[df['Date_dt'] >= start]

# Convert numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Open','High','Low'])

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low'])/df['Open']

# Map indices to regions (Asia vs others) using knowledge
asia_indices = set([
    'N225',   # Nikkei 225 - Tokyo
    'HSI',    # Hang Seng - Hong Kong
    '000001.SS', # Shanghai Composite (proxy)
    '399001.SZ', # Shenzhen Component
    '^BSESN',    # BSE Sensex (India) if present
    '^NSEI',     # Nifty 50 (India) if present
    '^KS11',     # KOSPI - Korea
    '^TWII',     # TAIEX - Taiwan
])

asia_df = df[df['Index'].isin(asia_indices)]
res = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result_dict = {
    'ordering': res.index.tolist(),
    'avg_vol': res.values.tolist()
}

print("__RESULT__:")
print(json.dumps(result_dict))"""

env_args = {'var_call_vXxBIAjYxuht7EBuCkFUXnY4': ['index_info'], 'var_call_Fib4S7ve341w5nMGDotn8twZ': ['index_trade'], 'var_call_dw1TZCg0YncXAkobo6K2CjWn': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_ZgsA5y01aBz6TgXtehJOxaS0': 'file_storage/call_ZgsA5y01aBz6TgXtehJOxaS0.json'}

exec(code, env_args)
