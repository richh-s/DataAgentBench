code = """import json
import pandas as pd
# Load the data from the file
with open('/tmp/db_result_functions.query_db:4.json', 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert string values to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine if each day is up or down
df['is_up'] = df['Close'] > df['Open']
df['is_down'] = df['Close'] < df['Open']

# Group by Index and count up/down days
counts = df.groupby('Index').agg({
    'is_up': 'sum',
    'is_down': 'sum'
}).reset_index()

# Format the result
counts['up_days'] = counts['is_up'].astype(int)
counts['down_days'] = counts['is_down'].astype(int)

result = counts[['Index', 'up_days', 'down_days']].to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': [{'Index': '000001.SS', 'count': '84'}, {'Index': '399001.SZ', 'count': '76'}, {'Index': 'GDAXI', 'count': '98'}, {'Index': 'GSPTSE', 'count': '86'}, {'Index': 'HSI', 'count': '86'}, {'Index': 'IXIC', 'count': '75'}, {'Index': 'J203.JO', 'count': '81'}, {'Index': 'N100', 'count': '68'}, {'Index': 'N225', 'count': '74'}, {'Index': 'NSEI', 'count': '79'}, {'Index': 'NYA', 'count': '79'}, {'Index': 'SSMI', 'count': '93'}, {'Index': 'TWII', 'count': '78'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
