code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read full CPC level 5 data
level5_file = locals()['var_functions.query_db:12']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

# Create set of level 5 symbols
level5_symbols = set()
for item in level5_data:
    symbol = item['symbol']
    level5_symbols.add(symbol)

print(f"Total level 5 CPC symbols: {len(level5_symbols)}")
print(f"Sample symbols: {list(level5_symbols)[:10]}")

# Read patent data
patents_file = locals()['var_functions.query_db:8']
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

print(f"Total patent records: {len(patents_data)}")

# Parse data and count filings per year for each level 5 group
yearly_group_counts = defaultdict(lambda: defaultdict(int))
cpc_pattern = re.compile(r'"code":\s*"([^"]+)"')
year_pattern = re.compile(r'(\d{4})')

processed = 0
for record in patents_data:
    processed += 1
    if processed % 50000 == 0:
        print(f"Processed {processed} records...")
    
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    cpc_matches = cpc_pattern.findall(cpc_str)
    
    # Extract year
    pub_date = record.get('publication_date', '')
    if not pub_date:
        continue
    
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Map each CPC code to level 5 group and count
    for cpc_code in cpc_matches:
        # Extract group symbol (main group)
        parts = cpc_code.split('/')
        main_group = parts[0]
        
        # For CPC codes like H01M10/0565, the level 5 group is the main group
        # For codes like H01M, it's already the group
        if main_group in level5_symbols:
            group_code = main_group
        else:
            # Try shorter prefixes (common practice for CPC)
            if len(main_group) > 4:
                prefix4 = main_group[:4]
                if prefix4 in level5_symbols:
                    group_code = prefix4
                    continue  # Use the first match
        
        # Count this group code for the year
        if 'group_code' in locals():
            yearly_group_counts[group_code][year] += 1

print(f"Finished processing {processed} records")
print(f"Found {len(yearly_group_counts)} CPC groups with filings")

# Calculate EMA for each group code and find those with best year 2022
results = []

for group_code, year_counts in yearly_group_counts.items():
    # Sort years chronologically
    years = sorted(year_counts.items())
    if len(years) < 2:
        continue
    
    # Calculate EMA (smoothing factor 0.2)
    ema = years[0][1]  # First year value
    year_ema = {years[0][0]: ema}
    
    for year, count in years[1:]:
        ema = 0.2 * count + 0.8 * ema
        year_ema[year] = ema
    
    # Find best year (max EMA)
    best_year = max(year_ema.keys(), key=lambda y: year_ema[y])
    best_ema = year_ema[best_year]
    
    # Check if best year is 2022
    if best_year == 2022:
        results.append({
            'cpc_group_code': group_code,
            'ema_2022': best_ema,
            'yearly_counts': year_counts
        })

print(f"Found {len(results)} CPC groups with best year 2022")

# Sort by EMA value (highest first)
results.sort(key=lambda x: x['ema_2022'], reverse=True)

# Extract just the CPC group codes
cpc_codes = [r['cpc_group_code'] for r in results]

print('__RESULT__:')
print(json.dumps(cpc_codes))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': ['A01N', 'A01N', 'A01N', 'A01N', 'A01N', 'A01K', 'A01K', 'A01N', 'A01K', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01K', 'A01K', 'A01D', 'A01N', 'A01K', 'A01N', 'A01N', 'A01K', 'A01K', 'A01K', 'A01G', 'A01K', 'A01N', 'A01K', 'A01N', 'A01G', 'A01K', 'A01K', 'A01K', 'A01N', 'A01D', 'A01G', 'A01K', 'A01N', 'A01K', 'A01K', 'A01D', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01D', 'A01K', 'A01N', 'A01K', 'A01N', 'A01D', 'A01K', 'A01N', 'A01D', 'A01K', 'A01F', 'A01K', 'A01D', 'A01K', 'A01K', 'A01K', 'A01K', 'A01G', 'A01N', 'A01K', 'A01D', 'A01G', 'A01C', 'A01G', 'A01K', 'A01D', 'A01D', 'A01D', 'A01D', 'A01D', 'A01N'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
