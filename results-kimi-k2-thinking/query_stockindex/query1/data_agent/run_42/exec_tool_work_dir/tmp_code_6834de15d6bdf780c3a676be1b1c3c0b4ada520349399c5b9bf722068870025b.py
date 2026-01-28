code = """import json
import os

# Load trade data
trade_data_key = 'var_functions.query_db:6'
if trade_data_key in locals():
    trade_data = locals()[trade_data_key]
else:
    trade_data = None

# Check if it's a file path or direct data
index_trade = []
if isinstance(trade_data, str) and os.path.exists(trade_data):
    with open(trade_data, 'r') as f:
        index_trade = json.load(f)
elif isinstance(trade_data, list):
    index_trade = trade_data
else:
    index_trade = []

# Analyze the data
result_info = {
    'total_records': len(index_trade),
    'first_record': index_trade[0] if index_trade else None,
    'last_record': index_trade[-1] if index_trade else None,
    'unique_indices': sorted(list(set([r.get('Index') for r in index_trade if 'Index' in r]))) if index_trade else []
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
