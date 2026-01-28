code = """import json
import pandas as pd

# Load the data from the previous query
result_file = var_functions.query_db:8
with open(result_file, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert Open and Close to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Add a column to identify up/down days
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Group by index and count up/down days
summary = df.groupby('Index').agg({
    'is_up_day': 'sum',
    'is_down_day': 'sum'
}).reset_index()

# Identify indices with more up days than down days
summary['more_up_than_down'] = summary['is_up_day'] > summary['is_down_day']

# Filter for indices with more up days
result = summary[summary['more_up_than_down']].copy()

# Map index symbols to exchange names for clarity
index_to_exchange = {
    'NYA': 'New York Stock Exchange (NYSE Composite)',
    'IXIC': 'NASDAQ (NASDAQ Composite)',
    'GSPTSE': 'Toronto Stock Exchange (S&P/TSX Composite)'
}

result['Exchange_Name'] = result['Index'].map(index_to_exchange)

# Sort by difference (up days - down days) for better presentation
result['difference'] = result['is_up_day'] - result['is_down_day']
result = result.sort_values('difference', ascending=False)

# Prepare output
output = []
for _, row in result.iterrows():
    output.append({
        'Index': row['Index'],
        'Exchange': row['Exchange_Name'],
        'Up_Days': int(row['is_up_day']),
        'Down_Days': int(row['is_down_day']),
        'Difference': int(row['difference'])
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
