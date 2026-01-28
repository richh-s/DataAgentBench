code = """import json
import pandas as pd

# Access the 2018 trading data for North American indices
trade_data = locals()['var_functions.query_db:14']

# Load the data if it's a filepath (handle both cases)
if isinstance(trade_data, str):
    with open(trade_data, 'r') as f:
        trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Ensure proper data types
df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Classify each day as up (Close > Open) or down (Close < Open)
# Skip days where Close == Open (neutral)
df['movement'] = df.apply(
    lambda row: 
        'up' if float(row['Close']) > float(row['Open']) 
        else 'down' if float(row['Close']) < float(row['Open']) 
        else 'neutral', 
    axis=1
)

# Count up, down, and neutral days for each index
results = []
for index in df['Index'].unique():
    index_data = df[df['Index'] == index]
    movement_counts = index_data['movement'].value_counts()
    up_days = int(movement_counts.get('up', 0))
    down_days = int(movement_counts.get('down', 0))
    neutral_days = int(movement_counts.get('neutral', 0))
    total_days = int(len(index_data))
    
    results.append({
        'Index': str(index),
        'Up Days': up_days,
        'Down Days': down_days,
        'Total Days': total_days,
        'More Up Than Down': bool(up_days > down_days)
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min(Date)': '2018-01-05 00:00:00', 'max(Date)': '2018-12-21 00:00:00', 'total_days': '84'}, {'Index': '399001.SZ', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-25 00:00:00', 'total_days': '76'}, {'Index': 'GDAXI', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '98'}, {'Index': 'GSPTSE', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '86'}, {'Index': 'HSI', 'min(Date)': '2018-01-05 00:00:00', 'max(Date)': '2018-12-21 00:00:00', 'total_days': '85'}, {'Index': 'IXIC', 'min(Date)': '2018-01-02 00:00:00', 'max(Date)': '2018-12-13 00:00:00', 'total_days': '75'}, {'Index': 'J203.JO', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-28 00:00:00', 'total_days': '81'}, {'Index': 'N100', 'min(Date)': '2018-01-12 00:00:00', 'max(Date)': '2018-12-07 00:00:00', 'total_days': '67'}, {'Index': 'N225', 'min(Date)': '2018-01-11 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '74'}, {'Index': 'NSEI', 'min(Date)': '2018-01-08 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '78'}, {'Index': 'NYA', 'min(Date)': '2018-01-09 00:00:00', 'max(Date)': '2018-12-20 00:00:00', 'total_days': '78'}, {'Index': 'SSMI', 'min(Date)': '2018-01-04 00:00:00', 'max(Date)': '2018-12-28 00:00:00', 'total_days': '93'}, {'Index': 'TWII', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-24 00:00:00', 'total_days': '78'}], 'var_functions.execute_python:12': [{'exchange': 'New York Stock Exchange', 'index': 'NYA'}, {'exchange': 'NASDAQ', 'index': 'IXIC'}, {'exchange': 'Toronto Stock Exchange', 'index': 'GSPTSE'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
