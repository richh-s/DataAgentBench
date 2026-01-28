code = """import json

# Read the full result from the file
file_key = 'var_functions.query_db:2'
file_path = locals()[file_key]

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Filter for Asian indices and group by index
asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NIFTY50', 'NSEI', 'KOSPI', 'KS11', 'TWII']

# Group data by index
index_data = {}
for record in trade_data:
    index = record['Index']
    if index in asian_indices:
        if index not in index_data:
            index_data[index] = []
        index_data[index].append(record)

# Check which indices have data
available_indices = list(index_data.keys())

# Calculate intraday volatility for each index: (High - Low) / Open
volatility_results = {}

for index, records in index_data.items():
    total_volatility = 0
    count = 0
    
    for record in records:
        try:
            high = float(record['High'])
            low = float(record['Low'])
            open_price = float(record['Open'])
            
            if open_price > 0:
                volatility = (high - low) / open_price
                total_volatility += volatility
                count += 1
        except (ValueError, TypeError):
            continue
    
    if count > 0:
        avg_volatility = total_volatility / count
        volatility_results[index] = {
            'avg_volatility': avg_volatility,
            'count': count
        }

# Find the index with highest average volatility
if volatility_results:
    sorted_indices = sorted(volatility_results.items(), key=lambda x: x[1]['avg_volatility'], reverse=True)
    result = {
        'top_index': sorted_indices[0][0],
        'avg_volatility': sorted_indices[0][1]['avg_volatility'],
        'all_indices': volatility_results
    }
else:
    result = {'error': 'No valid volatility data found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
