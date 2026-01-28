code = """import json
from collections import defaultdict

# Read the data from the query result file
result_file = locals()['var_functions.query_db:18']
with open(result_file, 'r') as f:
    data = json.load(f)

# Define Asian indices
asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']

# Initialize storage for volatility calculations
volatility_sums = defaultdict(float)
volatility_counts = defaultdict(int)
errors = 0

# Process each record to calculate intraday volatility
for record in data:
    try:
        index = record['Index']
        
        # Only process Asian indices
        if index not in asian_indices:
            continue
            
        # Extract price data
        open_price = float(record['Open'])
        high_price = float(record['High'])
        low_price = float(record['Low'])
        
        # Validate and calculate volatility
        if open_price > 0 and high_price >= low_price and high_price > 0 and low_price > 0:
            # Intraday volatility = (High - Low) / Open
            volatility = (high_price - low_price) / open_price
            volatility_sums[index] += volatility
            volatility_counts[index] += 1
        else:
            errors += 1
            
    except (ValueError, KeyError, TypeError):
        errors += 1
        continue

# Calculate average volatility for each index
avg_volatilities = {}
for index in volatility_sums:
    if volatility_counts[index] > 0:
        avg_volatilities[index] = volatility_sums[index] / volatility_counts[index]

print(f"Processed {sum(volatility_counts.values())} valid records with {errors} errors")
print(f"Data points per index: {dict(volatility_counts)}")
print(f"Average volatilities: {avg_volatilities}")

# Find the index with highest average volatility
if avg_volatilities:
    highest_index = max(avg_volatilities, key=avg_volatilities.get)
    
    # Map index symbols to exchange names
    index_to_exchange = {
        'N225': 'Tokyo Stock Exchange (Nikkei 225)',
        'HSI': 'Hong Kong Stock Exchange (Hang Seng Index)',
        '000001.SS': 'Shanghai Stock Exchange (SSE Composite)',
        '399001.SZ': 'Shenzhen Stock Exchange (Shenzhen Component)',
        'TWII': 'Taiwan Stock Exchange (TAIEX)',
        'NSEI': 'National Stock Exchange of India (NIFTY 50)'
    }
    
    result = {
        'index_symbol': highest_index,
        'exchange': index_to_exchange.get(highest_index, 'Unknown Exchange'),
        'average_intraday_volatility': avg_volatilities[highest_index],
        'trading_days_analyzed': volatility_counts[highest_index],
        'all_indices_average_volatility': avg_volatilities
    }
else:
    result = {'error': 'No valid data found for analysis'}

# Output in required format
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
