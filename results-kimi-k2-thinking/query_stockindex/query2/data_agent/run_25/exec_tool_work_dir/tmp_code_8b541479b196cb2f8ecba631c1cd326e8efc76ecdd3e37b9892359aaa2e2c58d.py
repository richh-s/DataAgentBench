code = """import json
file_path = 'var_functions.query_db:8'
if isinstance(file_path, str) and '.json' in file_path:
    # It's a filepath, read from file
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    # It's direct data
    data = locals().get('var_functions.query_db:8', [])

# Process data to calculate up and down days for each index
from collections import defaultdict

index_stats = defaultdict(lambda: {'up': 0, 'down': 0})

for row in data:
    try:
        open_price = float(row['Open'])
        close_price = float(row['Close'])
        
        if close_price > open_price:
            index_stats[row['Index']]['up'] += 1
        elif close_price < open_price:
            # Count only strict down days (not equal)
            index_stats[row['Index']]['down'] += 1
    except (ValueError, TypeError):
        continue

# Identify indices with more up days than down days
result_indices = []
for idx, stats in index_stats.items():
    if stats['up'] > stats['down']:
        result_indices.append({
            'index': idx,
            'up_days': stats['up'],
            'down_days': stats['down'],
            'total_days': stats['up'] + stats['down']
        })

# Sort by index name
result_indices.sort(key=lambda x: x['index'])

result = json.dumps(result_indices, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
