code = """import json, pandas as pd
from datetime import datetime

# load full index_trade
path = var_call_nTNg0O3tvyUXNq4qHzQW6Mg0
with open(path, 'r') as f:
    trades = json.load(f)

df = pd.DataFrame(trades)
# clean types
for col in ['Open','High','Low','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# normalize date to ISO and filter since 2020-01-01
parsed = pd.to_datetime(df['Date'], errors='coerce')
mask = parsed >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

grp = df.groupby('Index')['vol'].mean().reset_index().dropna()

# Map Asia indices by known symbols in this dataset
asia_symbols = ['N225','HSI','000001.SS','399001.SZ','399006.SZ','^NSEI','^KS11','^TWII']
res = grp[grp['Index'].isin(asia_symbols)].sort_values('vol', ascending=False)

best = res.iloc[0].to_dict() if not res.empty else None

result = json.dumps(best)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_GXEteNzre0ZkpgOd8ezHKhNu': ['index_info'], 'var_call_EBflKmf2sJAuhollrUb9UvwH': ['index_trade'], 'var_call_bJQ38K9cB0CLncUef3vOgXv4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_nTNg0O3tvyUXNq4qHzQW6Mg0': 'file_storage/call_nTNg0O3tvyUXNq4qHzQW6Mg0.json'}

exec(code, env_args)
