code = """import json
import pandas as pd

# Load the 2018 trade data
file_path_2018 = var_functions.query_db:16
with open(file_path_2018, 'r') as f:
    trade_2018 = json.load(f)

# Convert to DataFrame
df_2018 = pd.DataFrame(trade_2018)
df_2018['Date'] = pd.to_datetime(df_2018['Date'])
df_2018['Open'] = pd.to_numeric(df_2018['Open'])
df_2018['Close'] = pd.to_numeric(df_2018['Close'])

# Process each index
def count_up_down_days(group):
    up_days = (group['Close'] > group['Open']).sum()
    down_days = (group['Close'] < group['Open']).sum()
    flat_days = (group['Close'] == group['Open']).sum()
    return {
        'index': group['Index'].iloc[0],
        'up_days': int(up_days),
        'down_days': int(down_days),
        'flat_days': int(flat_days),
        'total_days': len(group),
        'more_up_than_down': bool(up_days > down_days)
    }

# Group by index and count up/down days
results = df_2018.groupby('Index').apply(count_up_down_days).tolist()

# Print results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
