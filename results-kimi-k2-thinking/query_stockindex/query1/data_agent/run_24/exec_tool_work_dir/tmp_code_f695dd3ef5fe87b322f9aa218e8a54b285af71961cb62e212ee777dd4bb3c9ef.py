code = """import json
import pandas as pd

# Load data
index_info = [{"Currency": "USD", "Exchange": "New York Stock Exchange"}, {"Currency": "USD", "Exchange": "NASDAQ"}, {"Currency": "HKD", "Exchange": "Hong Kong Stock Exchange"}, {"Currency": "CNY", "Exchange": "Shanghai Stock Exchange"}, {"Currency": "JPY", "Exchange": "Tokyo Stock Exchange"}, {"Currency": "EUR", "Exchange": "Euronext"}, {"Currency": "CNY", "Exchange": "Shenzhen Stock Exchange"}, {"Currency": "CAD", "Exchange": "Toronto Stock Exchange"}, {"Currency": "INR", "Exchange": "National Stock Exchange of India"}, {"Currency": "EUR", "Exchange": "Frankfurt Stock Exchange"}, {"Currency": "KRW", "Exchange": "Korea Exchange"}, {"Currency": "CHF", "Exchange": "SIX Swiss Exchange"}, {"Currency": "TWD", "Exchange": "Taiwan Stock Exchange"}, {"Currency": "ZAR", "Exchange": "Johannesburg Stock Exchange"}]

# Load trade data from file
trade_data_path = '/home/user/repo/files/9b43b6c4-7e0e-4a7e-9cc7-a6c7aa7ddaa3.json'
with open(trade_data_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrames
df_info = pd.DataFrame(index_info)
df_trade = pd.DataFrame(trade_data)

print('__RESULT__:')
print(json.dumps({
    'info_shape': df_info.shape,
    'trade_shape': df_trade.shape,
    'trade_indices': sorted(df_trade['Index'].unique().tolist()),
    'first_few': df_trade.head().to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
