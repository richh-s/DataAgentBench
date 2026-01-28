code = """import json
import pandas as pd

# Get the result file path from locals
result_file_path = locals()['var_functions.query_db:38']

# Read the data
with open(result_file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert numeric columns
for col in ['Open', 'High', 'Low', 'Close']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col])

# Calculate intraday volatility
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by index and calculate average intraday volatility for each Asian index
avg_volatility = df.groupby('Index')['Intraday_Volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

# Create result dictionary
result_output = avg_volatility.to_dict('records')

print('__RESULT__:')
print(json.dumps(result_output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': [{'Index': 'N225', 'Date': 'January 06, 1965 at 12:00 AM', 'Open': '1263.98999', 'High': '1263.98999', 'Low': '1263.98999', 'Close': '1263.98999'}, {'Index': 'N225', 'Date': 'January 13, 1965 at 12:00 AM', 'Open': '1281.670044', 'High': '1281.670044', 'Low': '1281.670044', 'Close': '1281.670044'}, {'Index': 'N225', 'Date': 'January 14, 1965 at 12:00 AM', 'Open': '1289.5', 'High': '1289.5', 'Low': '1289.5', 'Close': '1289.5'}, {'Index': 'N225', 'Date': 'January 21, 1965 at 12:00 AM', 'Open': '1270.459961', 'High': '1270.459961', 'Low': '1270.459961', 'Close': '1270.459961'}, {'Index': 'N225', 'Date': '26 Jan 1965, 00:00', 'Open': '1248.050049', 'High': '1248.050049', 'Low': '1248.050049', 'Close': '1248.050049'}], 'var_functions.query_db:36': [{'Index': 'HSI', 'Date': '2020-01-08 00:00:00', 'Open': '27999.58008', 'High': '28198.60938', 'Low': '27857.73047', 'Close': '28087.91992'}, {'Index': 'HSI', 'Date': '2020-01-10 00:00:00', 'Open': '28665.14063', 'High': '28665.14063', 'Low': '28504.26953', 'Close': '28638.19922'}, {'Index': 'HSI', 'Date': '2020-01-14 00:00:00', 'Open': '29149.5293', 'High': '29149.5293', 'Low': '28790.49023', 'Close': '28885.14063'}, {'Index': 'HSI', 'Date': '2020-01-16 00:00:00', 'Open': '28806.11914', 'High': '28987.73047', 'Low': '28709.57031', 'Close': '28883.03906'}, {'Index': 'HSI', 'Date': '2020-01-17 00:00:00', 'Open': '28988.16016', 'High': '29101.15039', 'Low': '28813.13086', 'Close': '29056.41992'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:42': {'record_count': 674, 'first_record': {'Index': '000001.SS', 'Date': '2020-01-08 00:00:00', 'Open': '3094.239014', 'High': '3094.239014', 'Low': '3059.131104', 'Close': '3066.893066'}}}

exec(code, env_args)
