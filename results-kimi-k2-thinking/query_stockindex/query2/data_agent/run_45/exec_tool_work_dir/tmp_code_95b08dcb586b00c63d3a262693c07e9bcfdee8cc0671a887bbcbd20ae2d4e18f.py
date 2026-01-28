code = """import json
import pandas as pd

result_file = locals()['var_functions.query_db:24']

# Read the file content to see what we're dealing with
with open(result_file, 'r') as f:
    content = f.read()

# Check first 500 characters
preview = content[:500]

print('__RESULT__:')
print(json.dumps({'preview': preview}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['index_info'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': [{'Index': 'IXIC', 'Date': '2018-01-02 00:00:00', 'Open': '6937.649902', 'Close': '7006.899902'}, {'Index': 'IXIC', 'Date': '2018-01-04 00:00:00', 'Open': '7089.5', 'Close': '7077.910156'}, {'Index': 'IXIC', 'Date': '2018-01-08 00:00:00', 'Open': '7135.379883', 'Close': '7157.390137'}, {'Index': 'IXIC', 'Date': '2018-01-11 00:00:00', 'Open': '7168.72998', 'Close': '7211.779785'}, {'Index': 'IXIC', 'Date': '2018-01-17 00:00:00', 'Open': '7257.77002', 'Close': '7298.279785'}], 'var_functions.query_db:30': [{'total_records': '86', 'Index': 'GSPTSE', 'records_per_index': '86'}, {'total_records': '78', 'Index': 'NYA', 'records_per_index': '78'}, {'total_records': '75', 'Index': 'IXIC', 'records_per_index': '75'}]}

exec(code, env_args)
