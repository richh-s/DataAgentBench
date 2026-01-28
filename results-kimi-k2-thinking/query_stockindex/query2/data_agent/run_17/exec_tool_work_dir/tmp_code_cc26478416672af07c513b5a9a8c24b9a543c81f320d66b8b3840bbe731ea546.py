code = """# Read the full query result from the file path stored in var_functions.query_db:8
import json
import os

file_path = var_functions.query_db:8

# Load the complete data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Loaded {len(data)} records from file")

# Create a mapping from Index to exchange info
exchange_info = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GSPTSE': 'Toronto Stock Exchange'
}

# Group data by index
from collections import defaultdict
indices_data = defaultdict(list)
for record in data:
    indices_data[record['Index']].append(record)

# Calculate up and down days for each index
results = {}
for index, trades in indices_data.items():
    up_days = 0
    down_days = 0
    for trade in trades:
        # Convert to float and check if closing > opening
        open_price = float(trade['Open'])
        close_price = float(trade['Close'])
        if close_price > open_price:
            up_days += 1
        elif close_price < open_price:
            down_days += 1
    total_days = len(trades)
    results[index] = {
        'up_days': up_days,
        'down_days': down_days,
        'total_days': total_days,
        'exchange': exchange_info.get(index, 'Unknown')
    }

# Print formatted results
for index, stats in results.items():
    print(f"Index: {index}")
    print(f"  Exchange: {stats['exchange']}")
    print(f"  Up days: {stats['up_days']}, Down days: {stats['down_days']}")
    print(f"  More up days than down days: {stats['up_days'] > stats['down_days']}")
    print()

# Identify which have more up days
indices_more_up_days = [idx for idx, stats in results.items() if stats['up_days'] > stats['down_days']]

final_result = {
    'analyzed_indices': list(results.keys()),
    'indices_with_more_up_days': indices_more_up_days,
    'detailed_stats': results
}
print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
