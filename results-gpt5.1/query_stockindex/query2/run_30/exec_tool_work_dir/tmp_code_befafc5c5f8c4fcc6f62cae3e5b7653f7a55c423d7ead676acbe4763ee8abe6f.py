code = """import json, pandas as pd
from pathlib import Path

# Load full 2018 trade data
file_path = Path(var_call_0VhaHCGOsS0wKr40PLfK11mW)
records = json.loads(file_path.read_text())

df = pd.DataFrame(records)
# Ensure numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Filter to North American indices: NYA (NYSE Composite, US), IXIC (Nasdaq Composite, US), GSPTSE (S&P/TSX, Canada)
north_american_indices = ['NYA', 'IXIC', 'GSPTSE']

df_na = df[df['Index'].isin(north_american_indices)].copy()

# Compute up and down per index
summary = []
for idx, g in df_na.groupby('Index'):
    up_days = (g['Close'] > g['Open']).sum()
    down_days = (g['Close'] < g['Open']).sum()
    summary.append({'Index': idx, 'up_days': int(up_days), 'down_days': int(down_days), 'more_up_than_down': bool(up_days > down_days)})

result = json.dumps(summary)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ZO5N8p6wMFHBvhCtM3Us3WcE': ['index_info'], 'var_call_YLs4fbymUWOpe2txgIYtJCdB': ['index_trade'], 'var_call_eYMLOlqMlgcdfcevZo4zXusF': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_zv6bB6SZOhDvojQHh0M57W4B': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'J203.JO'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_0VhaHCGOsS0wKr40PLfK11mW': 'file_storage/call_0VhaHCGOsS0wKr40PLfK11mW.json'}

exec(code, env_args)
