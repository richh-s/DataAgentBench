code = """import json
import re

# Get the file path from storage
file_path_key = 'var_functions.query_db:16'
file_path = globals()[file_path_key]

# Load the full dataset from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Define North American indices
north_american_indices = ['NYA', 'IXIC', 'GSPTSE']

# Function to count up and down days for each index
def count_up_down_days(index_data):
    up_days = 0
    down_days = 0
    
    for record in index_data:
        try:
            open_price = float(record['Open'])
            close_price = float(record['Close'])
            
            if close_price > open_price:
                up_days += 1
            elif close_price < open_price:
                down_days += 1
        except (ValueError, TypeError):
            continue
    
    return up_days, down_days

# Process data for each North American index
results = {}

for index in north_american_indices:
    index_data = [r for r in data if r['Index'] == index]
    up_days, down_days = count_up_down_days(index_data)
    results[index] = {
        'up_days': up_days,
        'down_days': down_days,
        'has_more_up_days': up_days > down_days
    }

# Find indices with more up days than down days
winning_indices = []
for index, stats in results.items():
    if stats['has_more_up_days']:
        winning_indices.append(index)

# Create output
output = {
    'indices_with_more_up_days': winning_indices,
    'all_indices_stats': results
}

# Print result
print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
