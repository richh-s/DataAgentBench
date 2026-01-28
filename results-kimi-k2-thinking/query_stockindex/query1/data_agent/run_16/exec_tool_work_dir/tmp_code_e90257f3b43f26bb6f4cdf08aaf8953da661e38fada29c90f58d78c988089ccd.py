code = """import json
from datetime import datetime

# Get the file path from the query result
result_file = locals()['var_functions.query_db:14']

# Read the data
with open(result_file, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Define Asian indices
asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']

# Process data: calculate intraday volatility for each record
volatility_data = {}
processed_count = 0
errors = 0

for record in data:
    try:
        index = record['Index']
        
        # Skip if not an Asian index
        if index not in asian_indices:
            continue
            
        # Parse date - extract year to verify it's >= 2020
        date_str = record['Date']
        
        # Extract year from various date formats
        year = None
        if '2020' in date_str:
            year = 2020
        elif '2021' in date_str:
            year = 2021
        elif '2022' in date_str:
            year = 2022
        elif '2023' in date_str:
            year = 2023
        elif '2024' in date_str:
            year = 2024
            
        if year is None or year < 2020:
            continue
            
        # Get price data
        open_price = float(record['Open'])
        high_price = float(record['High'])
        low_price = float(record['Low'])
        
        # Calculate intraday volatility: (High - Low) / Open
        if open_price > 0:
            volatility = (high_price - low_price) / open_price
            
            # Initialize list for this index if needed
            if index not in volatility_data:
                volatility_data[index] = []
                
            volatility_data[index].append(volatility)
            processed_count += 1
        else:
            errors += 1
            
    except Exception as e:
        errors += 1
        continue

print(f"Processed {processed_count} records with {errors} errors")
print(f"Indices found: {list(volatility_data.keys())}")

# Calculate average volatility for each index
avg_volatilities = {}
for index, volatilities in volatility_data.items():
    if volatilities:
        avg_volatility = sum(volatilities) / len(volatilities)
        avg_volatilities[index] = avg_volatility
        print(f"{index}: {len(volatilities)} days, avg volatility: {avg_volatility:.6f}")

# Find index with highest average volatility
if avg_volatilities:
    highest_index = max(avg_volatilities, key=avg_volatilities.get)
    highest_volatility = avg_volatilities[highest_index]
    
    # Map index to exchange name
    index_to_exchange = {
        'N225': 'Tokyo Stock Exchange',
        'HSI': 'Hong Kong Stock Exchange', 
        '000001.SS': 'Shanghai Stock Exchange',
        '399001.SZ': 'Shenzhen Stock Exchange',
        'TWII': 'Taiwan Stock Exchange',
        'NSEI': 'National Stock Exchange of India'
    }
    
    result = {
        'index_symbol': highest_index,
        'exchange_name': index_to_exchange.get(highest_index, 'Unknown'),
        'average_intraday_volatility': highest_volatility,
        'data_points': len(volatility_data[highest_index]),
        'all_indices_avg_volatility': avg_volatilities
    }
    
    print(f"\nHighest volatility index: {highest_index}")
    print(f"Average intraday volatility: {highest_volatility:.6f}")
    print(f"Based on {len(volatility_data[highest_index])} trading days")
else:
    result = {'error': 'No valid data found'}

# Output in required format
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
