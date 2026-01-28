code = """import json
import os

# Load index info data
index_info = [
  {"Exchange": "New York Stock Exchange", "Currency": "USD"},
  {"Exchange": "NASDAQ", "Currency": "USD"},
  {"Exchange": "Hong Kong Stock Exchange", "Currency": "HKD"},
  {"Exchange": "Shanghai Stock Exchange", "Currency": "CNY"},
  {"Exchange": "Tokyo Stock Exchange", "Currency": "JPY"},
  {"Exchange": "Euronext", "Currency": "EUR"},
  {"Exchange": "Shenzhen Stock Exchange", "Currency": "CNY"},
  {"Exchange": "Toronto Stock Exchange", "Currency": "CAD"},
  {"Exchange": "National Stock Exchange of India", "Currency": "INR"},
  {"Exchange": "Frankfurt Stock Exchange", "Currency": "EUR"},
  {"Exchange": "Korea Exchange", "Currency": "KRW"},
  {"Exchange": "SIX Swiss Exchange", "Currency": "CHF"},
  {"Exchange": "Taiwan Stock Exchange", "Currency": "TWD"},
  {"Exchange": "Johannesburg Stock Exchange", "Currency": "ZAR"}
]

# Load the index trade data
trade_data_key = 'var_functions.query_db:6'
trade_data_val = locals()[trade_data_key]

if isinstance(trade_data_val, str) and os.path.exists(trade_data_val):
    with open(trade_data_val, 'r') as f:
        index_trade = json.load(f)
else:
    index_trade = trade_data_val

print('Index info count:', len(index_info))
print('Index trade count:', len(index_trade))
print('First trade record:', index_trade[0])"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
