code = """import json, pandas as pd, re
from datetime import datetime

# Load full trade data from file
trade_data = json.load(open(var_functions.query_db:3, 'r'))

# Load index info data
index_info = var_functions.query_db:1

# Convert to DataFrames
df_trade = pd.DataFrame(trade_data)
df_info = pd.DataFrame(index_info)

print('__RESULT__:')
print('Loaded ' + str(len(df_trade)) + ' trade records and ' + str(len(df_info)) + ' index info records')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
