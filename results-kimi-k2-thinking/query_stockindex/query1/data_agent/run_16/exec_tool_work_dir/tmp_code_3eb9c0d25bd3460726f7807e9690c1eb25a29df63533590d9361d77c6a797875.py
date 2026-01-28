code = """import json
from datetime import datetime

# Read the data from the stored file
result_file = '/tmp/tmp2j8a3v7h.json'
with open(result_file, 'r') as f:
    data = json.load(f)

# Define Asian indices
asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']

# Filter and process data
results = []

for record in data:
    index = record['Index']
    
    # Skip non-Asian indices
    if index not in asian_indices:
        continue
    
    # Parse date (handle multiple formats)
    date_str = record['Date']
    date_obj = None
    
    try:
        # Try to extract year
        if '2020' in date_str or '2021' in date_str or '2022' in date_str or '2023' in date_str or '2024' in date_str:
            # Remove time part if present
            date_part = date_str.split(' at ')[0].split(',')[0]
            
            formats = [
                '%B %d, %Y',  # January 02, 1987
                '%d %b %Y',   # 31 Dec 1986
                '%Y-%m-%d',   # 2020-01-01
            ]
            
            for fmt in formats:
                try:
                    date_obj = datetime.strptime(date_part, fmt)
                    break
                except:
                    continue
    except:
        continue
    
    # Skip if date parsing failed or year < 2020
    if date_obj is None or date_obj.year < 2020:
        continue
    
    # Calculate intraday volatility
    try:
        open_price = float(record['Open'])
        high_price = float(record['High'])
        low_price = float(record['Low'])
        
        if open_price > 0:
            volatility = (high_price - low_price) / open_price
            results.append({
                'Index': index,
                'Date': record['Date'],
                'IntradayVolatility': volatility
            })
    except:
        continue

# Calculate average volatility per index
from collections import defaultdict
index_volatilities = defaultdict(list)

for r in results:
    index_volatilities[r['Index']].append(r['IntradayVolatility'])

average_volatilities = {}
for index, vols in index_volatilities.items():
    average_volatilities[index] = sum(vols) / len(vols)

# Find index with highest average volatility
if average_volatilities:
    highest_index = max(average_volatilities, key=average_volatilities.get)
    result = {
        'index': highest_index,
        'average_volatility': average_volatilities[highest_index],
        'all_averages': average_volatilities,
        'total_records': len(results)
    }
else:
    result = {'error': 'No data found'}

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
