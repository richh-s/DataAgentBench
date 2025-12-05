code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_9Jhq4S58wn8ymDMwIOwBXo0b)
records = json.loads(path.read_text())

# Load into DataFrame
df = pd.DataFrame(records)

# Convert numeric columns
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter to North American indices based on prior knowledge mapping
# NYA -> New York Stock Exchange (US), IXIC -> NASDAQ (US), GSPTSE -> Toronto Stock Exchange (Canada)
north_american = ['NYA','IXIC','GSPTSE']
df_na = df[df['Index'].isin(north_american)].copy()

# Classify up/down days
df_na['up'] = df_na['Close'] > df_na['Open']
df_na['down'] = df_na['Close'] < df_na['Open']

summary = df_na.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down','sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ETwEYgGyuhMZevKsnYQeJq21': ['index_info'], 'var_call_PlI6uNyIeaSXUyHfHDbEV0XA': ['index_trade'], 'var_call_FI0COkf9Xrq3cpiRwXHqoBFX': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_CUzTWh4UT58UYXXWFO0jKTSs': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_9Jhq4S58wn8ymDMwIOwBXo0b': 'file_storage/call_9Jhq4S58wn8ymDMwIOwBXo0b.json'}

exec(code, env_args)
