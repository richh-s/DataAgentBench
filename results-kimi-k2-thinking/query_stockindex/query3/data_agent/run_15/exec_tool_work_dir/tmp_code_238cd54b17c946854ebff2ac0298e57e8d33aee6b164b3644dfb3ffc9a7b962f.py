code = """# Load the complete price data
import json
import pandas as pd
from datetime import datetime

# Read the full price data from file
price_data_file = locals()['var_functions.query_db:12']
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Convert Date and CloseUSD to proper types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

print('Total records:', len(df))
print('Unique indices:', df['Index'].nunique())
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('\nAll indices:', df['Index'].unique())

# Basic mapping of indices to countries/regions
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    'NYA': 'USA',
    'IXIC': 'USA',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'TWII': 'Taiwan',
    'SSMI': 'Switzerland',
    'N100': 'Netherlands/Europe',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    '000001.SS': 'China',
    '399001.SZ': 'China'
}

# Show the data for each index
print('\nData coverage by index:')
for index in df['Index'].unique():
    idx_data = df[df['Index'] == index]
    print(f"{index}: {len(idx_data)} records, {idx_data['Date'].min().strftime('%Y-%m-%d')} to {idx_data['Date'].max().strftime('%Y-%m-%d')}")

print('__RESULT__:')
print(json.dumps({'status': 'data_loaded', 'indices': list(df['Index'].unique())}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'NYA', 'Date': '2000-01-03 00:00:00', 'Open': '6762.109863', 'High': '6762.109863', 'Low': '6762.109863', 'Close': '6762.109863', 'Adj Close': '6762.109863', 'CloseUSD': '6762.109863'}, {'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'Open': '1368.692993', 'High': '1407.517944', 'Low': '1361.213989', 'Close': '1406.370972', 'Adj Close': '1406.370972', 'CloseUSD': '225.01935552'}, {'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'Open': '1407.828979', 'High': '1433.780029', 'Low': '1398.322998', 'Close': '1409.682007', 'Adj Close': '1409.682007', 'CloseUSD': '225.54912112'}, {'Index': '399001.SZ', 'Date': '2000-01-05 00:00:00', 'Open': '3500.129883', 'High': '3589.179932', 'Low': '3468.689941', 'Close': '3486.290039', 'Adj Close': '3486.250977', 'CloseUSD': '557.80640624'}], 'var_functions.execute_python:10': {'index_info_sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'index_symbols': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'price_sample': [{'Index': 'NYA', 'Date': '2000-01-03 00:00:00', 'Open': '6762.109863', 'High': '6762.109863', 'Low': '6762.109863', 'Close': '6762.109863', 'Adj Close': '6762.109863', 'CloseUSD': '6762.109863'}, {'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'Open': '1368.692993', 'High': '1407.517944', 'Low': '1361.213989', 'Close': '1406.370972', 'Adj Close': '1406.370972', 'CloseUSD': '225.01935552'}, {'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'Open': '1407.828979', 'High': '1433.780029', 'Low': '1398.322998', 'Close': '1409.682007', 'Adj Close': '1409.682007', 'CloseUSD': '225.54912112'}, {'Index': '399001.SZ', 'Date': '2000-01-05 00:00:00', 'Open': '3500.129883', 'High': '3589.179932', 'Low': '3468.689941', 'Close': '3486.290039', 'Adj Close': '3486.250977', 'CloseUSD': '557.80640624'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
