code = """import json
import pandas as pd
import re
from datetime import datetime

# Load CPC and publication data
cpc_data_file = locals()['var_functions.query_db:7']
with open(cpc_data_file, 'r') as f:
    publications = json.load(f)

# Load level 5 CPC codes
level5_file = locals()['var_functions.query_db:8']
with open(level5_file, 'r') as f:
    level5_codes = [item['symbol'] for item in json.load(f)]

print(f"Total publications: {len(publications)}")
print(f"Level 5 CPC codes: {len(level5_codes)}")
print(f"Sample level 5 codes: {level5_codes[:10]}")

# Process data - extract CPC codes and years
cpc_yearly_counts = {}

for pub in publications:
    # Parse publication date
    pub_date_str = pub.get('publication_date', '')
    if not pub_date_str:
        continue
    
    # Extract year from date string like "Aug 3rd, 2021"
    year_match = re.search(r'(\d{4})', pub_date_str)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Parse CPC codes (stored as JSON string)
    cpc_json = pub.get('cpc', '')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract CPC group code at level 5 (format: XNNN/N... or XNNNN)
                # For level 5, we want the main group level (e.g., H01M from H01M10/0525)
                parts = code.split('/')
                if len(parts) >= 1:
                    main_group = parts[0]
                    # Extract first 4 characters (e.g., H01M from H01M10)
                    if len(main_group) >= 4:
                        cpc_group = main_group[:4]
                        # Check if this is a level 5 code
                        if cpc_group in level5_codes:
                            if cpc_group not in cpc_yearly_counts:
                                cpc_yearly_counts[cpc_group] = {}
                            cpc_yearly_counts[cpc_group][year] = cpc_yearly_counts[cpc_group].get(year, 0) + 1
    except:
        continue

print(f"CPC groups with data: {len(cpc_yearly_counts)}")

# Get all years
all_years = set()
for counts in cpc_yearly_counts.values():
    all_years.update(counts.keys())
all_years = sorted(list(all_years))
print(f"Years found: {all_years}")

# Calculate EMA for each CPC group
ema_data = {}
smoothing_factor = 0.2

for cpc_group, yearly_counts in cpc_yearly_counts.items():
    if len(yearly_counts) < 2:  # Need at least 2 years for EMA
        continue
    
    # Sort years and get counts
    sorted_years = sorted(yearly_counts.items())
    
    # Calculate EMA
    ema_values = []
    # Initialize with first year value
    ema_prev = sorted_years[0][1]
    
    for year, count in sorted_years:
        ema_current = (smoothing_factor * count) + ((1 - smoothing_factor) * ema_prev)
        ema_values.append((year, ema_current))
        ema_prev = ema_current
    
    ema_data[cpc_group] = ema_values

print(f"CPC groups with EMA data: {len(ema_data)}")

# Find CPC groups whose best year is 2022
cpc_best_year_2022 = []
for cpc_group, ema_values in ema_data.items():
    max_ema = 0
    best_year = None
    
    for year, ema_value in ema_values:
        if ema_value > max_ema:
            max_ema = ema_value
            best_year = year
    
    if best_year == 2022:
        cpc_best_year_2022.append(cpc_group)

print(f"CPC groups with best year 2022: {cpc_best_year_2022}")
print(f"Count: {len(cpc_best_year_2022)}")

# Return result
result = json.dumps(cpc_best_year_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
