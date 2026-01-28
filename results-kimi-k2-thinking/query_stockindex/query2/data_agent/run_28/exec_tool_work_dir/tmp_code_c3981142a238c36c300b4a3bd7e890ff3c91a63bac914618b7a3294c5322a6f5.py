code = """import json

# Load the data from the previous query
result_key = 'var_functions.query_db:10'
# Since the result is stored in a file, I need to read it
import pathlib
import sys

# Let's see if it's a file path or actual data
if isinstance(locals().get(result_key), str) and locals()[result_key].endswith('.json'):
    with open(locals()[result_key], 'r') as f:
        data = json.load(f)
else:
    data = locals().get(result_key, [])

# Count up days and down days for each index in 2018
from collections import defaultdict

index_stats = defaultdict(lambda: {'up_days': 0, 'down_days': 0, 'total_days': 0})

for row in data:
    index = row['Index']
    open_price = float(row['Open'])
    close_price = float(row['Close'])
    
    if close_price > open_price:
        index_stats[index]['up_days'] += 1
        index_stats[index]['total_days'] += 1
    elif close_price < open_price:
        index_stats[index]['down_days'] += 1
        index_stats[index]['total_days'] += 1
    # If equal, we don't count as up or down

# Calculate net days (up - down) and filter for more up than down
results = []
for index, stats in index_stats.items():
    net_days = stats['up_days'] - stats['down_days']
    if net_days > 0:
        results.append({
            'index': index,
            'up_days': stats['up_days'],
            'down_days': stats['down_days'],
            'net_days': net_days,
            'total_days': stats['total_days']
        })

# Sort by net days descending
results.sort(key=lambda x: x['net_days'], reverse=True)

output_json = json.dumps(results)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'day_count': '84'}, {'Index': '399001.SZ', 'day_count': '76'}, {'Index': 'GDAXI', 'day_count': '98'}, {'Index': 'GSPTSE', 'day_count': '86'}, {'Index': 'HSI', 'day_count': '86'}, {'Index': 'IXIC', 'day_count': '75'}, {'Index': 'J203.JO', 'day_count': '81'}, {'Index': 'N100', 'day_count': '68'}, {'Index': 'N225', 'day_count': '74'}, {'Index': 'NSEI', 'day_count': '79'}, {'Index': 'NYA', 'day_count': '79'}, {'Index': 'SSMI', 'day_count': '93'}, {'Index': 'TWII', 'day_count': '78'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
