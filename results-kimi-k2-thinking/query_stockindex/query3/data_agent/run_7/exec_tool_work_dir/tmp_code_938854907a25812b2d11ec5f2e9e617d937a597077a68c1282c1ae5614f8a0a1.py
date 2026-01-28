code = """import pandas as pd
import json

# Load the price data from the JSON file
price_data_file = locals()['var_functions.query_db:6']
if isinstance(price_data_file, str):
    with open(price_data_file, 'r') as f:
        price_data = json.load(f)
else:
    price_data = price_data_file

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Convert Date to datetime and CloseUSD to float
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

result_info = {
    'data_loaded': f"{len(df)} records",
    'date_range': f"{df['Date'].min()} to {df['Date'].max()}",
    'indices': sorted(df['Index'].unique())
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-04 00:00:00', 'record_count': '4354'}, {'Index': '399001.SZ', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '4355'}, {'Index': 'GDAXI', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '5590'}, {'Index': 'GSPTSE', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '6506'}, {'Index': 'HSI', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2000-01-14 00:00:00', 'record_count': '5604'}, {'Index': 'IXIC', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-06 00:00:00', 'record_count': '7351'}, {'Index': 'J203.JO', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2012-02-08 00:00:00', 'record_count': '1854'}, {'Index': 'N100', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2000-01-10 00:00:00', 'record_count': '4245'}, {'Index': 'N225', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-04 00:00:00', 'record_count': '7979'}, {'Index': 'NSEI', 'max(Date)': 'September 30, 2014 at 12:00 AM', 'min(Date)': '2007-09-25 00:00:00', 'record_count': '2577'}, {'Index': 'NYA', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-03 00:00:00', 'record_count': '7960'}, {'Index': 'SSMI', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '5188'}, {'Index': 'TWII', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-17 00:00:00', 'record_count': '4385'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
