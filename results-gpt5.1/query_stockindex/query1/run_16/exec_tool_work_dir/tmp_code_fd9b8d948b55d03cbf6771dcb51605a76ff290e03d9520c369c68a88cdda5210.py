code = """import json, pandas as pd

# Load full index_trade data from file
path = var_call_EiLk22ZK6pyPzmCdQOA09A87
with open(path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter dates >= 2020-01-01 (date strings are varied; use pandas to parse)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date'] >= '2020-01-01']

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Average volatility per index
avg_vol = df.groupby('Index')['vol'].mean().reset_index()

# Map indices to regions (Asia vs others) using known major indices
asia_indices = {
    'N225',  # Nikkei 225 - Tokyo Stock Exchange (Japan)
    'HSI',   # Hang Seng Index - Hong Kong Stock Exchange
    '000001.SS',  # SSE Composite Index - Shanghai Stock Exchange (China)
    '399001.SZ',  # SZSE Component Index - Shenzhen Stock Exchange (China)
    '^NSEI',  # Nifty 50 - National Stock Exchange of India
    '^KS11',  # KOSPI - Korea Exchange (South Korea)
    '^TWII',  # TAIEX - Taiwan Stock Exchange
}

asia_avg = avg_vol[avg_vol['Index'].isin(asia_indices)].sort_values('vol', ascending=False)

result = None
if not asia_avg.empty:
    top = asia_avg.iloc[0]
    result = {
        'Index': top['Index'],
        'average_intraday_volatility_since_2020': float(top['vol'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QnVKXqHHmNqD0tbCrZymRug3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_EiLk22ZK6pyPzmCdQOA09A87': 'file_storage/call_EiLk22ZK6pyPzmCdQOA09A87.json'}

exec(code, env_args)
