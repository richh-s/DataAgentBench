code = """import json
import os

# Load trade data
trade_data_key = 'var_functions.query_db:6'
if trade_data_key in locals():
    trade_data = locals()[trade_data_key]
else:
    trade_data = None

print('Trade data type:', type(trade_data))

# Check if it's a file path
index_trade = []
if isinstance(trade_data, str) and os.path.exists(trade_data):
    print('Loading data from file')
    with open(trade_data, 'r') as f:
        index_trade = json.load(f)
elif isinstance(trade_data, list):
    print('Using direct list data')
    index_trade = trade_data
else:
    print('No data found')

print('Total records loaded:', len(index_trade) if index_trade else 0)

if index_trade:
    print('First record:', index_trade[0])
    print('Last record:', index_trade[-1])
    
    # Get unique indices
    unique_indices = set()
    for record in index_trade:
        if 'Index' in record:
            unique_indices.add(record['Index'])
    
    print('Unique indices found:', sorted(list(unique_indices)))
else:
    print('No data to process')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
