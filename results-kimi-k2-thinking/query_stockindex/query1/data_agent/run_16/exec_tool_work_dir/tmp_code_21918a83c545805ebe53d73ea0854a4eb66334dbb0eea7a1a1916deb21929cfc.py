code = """import json
import re
from datetime import datetime

# Read the stored data
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")
print(f"Sample records: {data[:3]}")

# Define the Asian indices and their corresponding exchanges
asian_indices = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'NSEI': 'National Stock Exchange of India'
}

print(f"Selected Asian indices: {list(asian_indices.keys())}")

# Parse dates in various formats and filter from 2020 onwards
def parse_date(date_str):
    if not date_str:
        return None
    try:
        # Remove time part if present
        date_part = date_str.split(' at ')[0].split(',')[0]
        # Try different date formats
        formats = [
            '%B %d, %Y',  # January 02, 1987
            '%d %b %Y',   # 31 Dec 1986
            '%Y-%m-%d',   # 2020-01-01
            '%m/%d/%Y',   # 01/02/2020
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_part, fmt)
            except:
                continue
        return None
    except:
        return None

# Filter data for Asian indices and from 2020 onwards
filtered_data = []
for record in data:
    index = record['Index']
    
    # Skip non-Asian indices
    if index not in asian_indices:
        continue
        
    # Parse date
    date_obj = parse_date(record['Date'])
    if date_obj is None:
        continue
        
    # Check if date is from 2020 onwards
    if date_obj.year < 2020:
        continue
        
    # Ensure we have valid price data
    try:
        open_price = float(record['Open'])
        high_price = float(record['High'])
        low_price = float(record['Low'])
        close_price = float(record['Close'])
        
        if open_price <= 0:
            continue
            
        # Calculate intraday volatility
        volatility = (high_price - low_price) / open_price
        
        filtered_data.append({
            'Index': index,
            'Date': record['Date'],
            'DateObj': date_obj,
            'Open': open_price,
            'High': high_price,
            'Low': low_price,
            'Close': close_price,
            'IntradayVolatility': volatility
        })
        
    except (ValueError, TypeError):
        continue

print(f"Filtered records from 2020 onwards: {len(filtered_data)}")
print(f"Records by index:")
for idx in asian_indices:
    count = sum(1 for r in filtered_data if r['Index'] == idx)
    print(f"  {idx}: {count}")"""

env_args = {'var_functions.query_db:0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
