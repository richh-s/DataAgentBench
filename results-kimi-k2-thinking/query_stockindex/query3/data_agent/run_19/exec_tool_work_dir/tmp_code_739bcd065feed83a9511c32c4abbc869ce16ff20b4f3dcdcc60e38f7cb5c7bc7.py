code = """import json
import pandas as pd

# Read the stored results
index_info = locals()['var_functions.query_db:5']

# Read the full price data from the file
price_data_file = "file_storage/functions.query_db:8.json"
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Create a mapping from exchanges to index symbols
exchange_to_index = {
    "Tokyo Stock Exchange": "N225",
    "Hong Kong Stock Exchange": "HSI", 
    "New York Stock Exchange": "NYA",
    "NASDAQ": "IXIC",
    "Shanghai Stock Exchange": "000001.SS",
    "Shenzhen Stock Exchange": "399001.SZ",
    "Frankfurt Stock Exchange": "GDAXI",
    "Toronto Stock Exchange": "GSPTSE",
    "National Stock Exchange of India": "NSEI",
    "Euronext": "N100"
}

# Also add country mapping based on exchange names
country_mapping = {
    "Tokyo Stock Exchange": "Japan",
    "Hong Kong Stock Exchange": "Hong Kong (China)", 
    "New York Stock Exchange": "United States",
    "NASDAQ": "United States",
    "Shanghai Stock Exchange": "China",
    "Shenzhen Stock Exchange": "China",
    "Frankfurt Stock Exchange": "Germany",
    "Toronto Stock Exchange": "Canada",
    "National Stock Exchange of India": "India",
    "Euronext": "Multi-country (Europe)"
}

print("__RESULT__:")
print(json.dumps({
    "price_records_count": len(price_data),
    "mapped_exchanges": len(exchange_to_index),
    "exchange_sample": list(exchange_to_index.items())[:3]
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'index_info_count': 10, 'price_data_file': 'file_storage/functions.query_db:8.json'}}

exec(code, env_args)
