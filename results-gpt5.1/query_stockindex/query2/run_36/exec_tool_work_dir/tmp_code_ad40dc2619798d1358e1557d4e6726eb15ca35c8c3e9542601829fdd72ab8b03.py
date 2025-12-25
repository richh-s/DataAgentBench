code = """import json, pandas as pd
from pathlib import Path

# Load full 2018 index data
file_path = Path(var_call_0JQwEjYmtZIurLkZYQNRA1)
records = json.loads(file_path.read_text())

# Create DataFrame
df = pd.DataFrame(records)

# Ensure numeric types
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Filter for North American indices based on knowledge: NYA (NYSE, US), IXIC (NASDAQ, US), GSPTSE (Toronto, Canada)
north_america = df[df['Index'].isin(['NYA','IXIC','GSPTSE'])]

# Determine up and down days
north_america['up'] = north_america['Close'] > north_america['Open']
north_america['down'] = north_america['Close'] < north_america['Open']

summary = north_america.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7F9cVAqVxpkNC1lH8C0WxPpn': ['index_info'], 'var_call_yDqmz7bEyPLCfLSFRE6uxRkD': ['index_trade'], 'var_call_D39aTmK70YK9eUNmg65eYgUr': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_4qaeVFML0yZqwhZ7uxNKm22K': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_0JQwEjYmtZIurLkZYQNQNRA1': 'file_storage/call_0JQwEjYmtZIurLkZYQNQNRA1.json'}

exec(code, env_args)
