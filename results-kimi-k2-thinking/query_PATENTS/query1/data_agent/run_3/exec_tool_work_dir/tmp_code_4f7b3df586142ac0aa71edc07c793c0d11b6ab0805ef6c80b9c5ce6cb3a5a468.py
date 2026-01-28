code = """import json
import re
from collections import defaultdict
import pandas as pd

# Read the full data from the file
file_path = locals()['var_functions.query_db:8']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Parse CPC codes and extract years
yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_code_pattern = re.compile(r'"code":\s*"([^"]+)"')

# Extract year from publication_date
year_pattern = re.compile(r'(\d{4})')

records_processed = 0
for record in data:
    records_processed += 1
    if records_processed % 50000 == 0:
        print(f"Processed {records_processed} records...")
    
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    cpc_matches = cpc_code_pattern.findall(cpc_str)
    
    # Extract year from publication_date
    pub_date = record.get('publication_date', '')
    if not pub_date:
        continue
    
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Count each CPC code for this year
    for cpc_code in cpc_matches:
        yearly_counts[cpc_code][year] += 1

print(f"Finished processing {records_processed} records")
print(f"Found {len(yearly_counts)} unique CPC codes")

# Get all CPC codes at level 5 from the database
cpc_level5_result = locals()['var_functions.query_db:6']
# Convert to list of symbols
level5_symbols = set()
for item in cpc_level5_result:
    symbol = item['symbol']
    level5_symbols.add(symbol)

print(f"Found {len(level5_symbols)} level 5 CPC symbols in database")

# Now calculate exponential moving averages for each CPC code
result_data = []

for cpc_code, year_counts in yearly_counts.items():
    # Check if this CPC code is at level 5
    # Level 5 codes are typically the group level (e.g., A01B, C01B, etc.)
    # We'll check if the base symbol (first part before / or first 4-5 chars) matches a level 5 symbol
    
    base_symbol = cpc_code.split('/')[0]
    if '/' in cpc_code:
        # For codes like H01M10/0565, the main group is H01M10
        parts = cpc_code.split('/')
        main_group = parts[0]
        if len(main_group) <= 5:
            group_code = main_group
        else:
            # For codes with more characters, extract first 4 if possible
            group_code = main_group[:4]
    else:
        # For codes without /, use first 4-5 characters
        group_code = base_symbol[:5]
    
    # Check if this group_code is in level5_symbols
    if group_code not in level5_symbols:
        continue
    
    # Get sorted years and counts
    years = sorted(year_counts.items())
    if len(years) < 2:  # Need at least 2 years for EMA
        continue
    
    # Calculate EMA with smoothing factor 0.2
    ema_values = []
    first_year = years[0][0]
    # Initialize EMA with first value
    ema = years[0][1]
    year_ema_map = {first_year: ema}
    
    for i in range(1, len(years)):
        year, count = years[i]
        ema = 0.2 * count + 0.8 * ema
        year_ema_map[year] = ema
    
    # Find best year (highest EMA)
    if year_ema_map:
        best_year = max(year_ema_map.keys(), key=lambda y: year_ema_map[y])
        best_ema = year_ema_map[best_year]
        
        # Add to result if best year is 2022
        if best_year == 2022:
            result_data.append({
                'cpc_group_code': group_code,
                'best_year': best_year,
                'ema_value': best_ema,
                'all_years': year_counts
            })

print(f"Found {len(result_data)} CPC codes with best year 2022")

# Sort by EMA value (descending) to get highest exponential moving averages
result_data.sort(key=lambda x: x['ema_value'], reverse=True)

# Extract just the CPC group codes
cpc_codes_2022 = [item['cpc_group_code'] for item in result_data]

# Print results in the required format
print('__RESULT__:')
print(json.dumps(cpc_codes_2022))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
