code = """import json, pandas as pd

# Load trade rows (may be file path)
trade_src = var_call_ktZGvXT5LGJqsz7r5rccfBOE
if isinstance(trade_src, str):
    with open(trade_src, 'r', encoding='utf-8') as f:
        trades = json.load(f)
else:
    trades = trade_src

df = pd.DataFrame(trades)
# Coerce types
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# North America mapping inferred from exchanges present
north_america_indices = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GSPTSE': 'Toronto Stock Exchange'
}

df = df[df['Index'].isin(north_america_indices.keys())].copy()

df['up'] = (df['Close'] > df['Open']).astype(int)
df['down'] = (df['Close'] < df['Open']).astype(int)

agg = df.groupby('Index')[['up','down']].sum().reset_index()
agg['exchange'] = agg['Index'].map(north_america_indices)
agg['more_up_than_down'] = agg['up'] > agg['down']

res = agg[agg['more_up_than_down']].sort_values('Index')[['Index','exchange','up','down']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_rVZV16awJMUKB5ZvUfnFmIPt': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_ktZGvXT5LGJqsz7r5rccfBOE': 'file_storage/call_ktZGvXT5LGJqsz7r5rccfBOE.json'}

exec(code, env_args)
