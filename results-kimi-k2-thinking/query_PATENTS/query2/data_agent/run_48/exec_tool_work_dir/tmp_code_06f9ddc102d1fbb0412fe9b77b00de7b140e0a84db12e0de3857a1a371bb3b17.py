code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load CPC level 4 definitions
cpc_file = locals()['var_functions.query_db:24']
with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

# Create CPC code to title mapping
cpc_titles = {defn['symbol'].strip(): defn['titleFull'] for defn in cpc_definitions}

# Load German patents data
german_file = locals()['var_functions.query_db:20']
with open(german_file, 'r') as f:
    german_patents = json.load(f)

# Process all German patents to get historical data
yearly_counts = defaultdict(lambda: defaultdict(int))
grant_pattern = r'(\d{4})'

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    cpc_str = patent.get('cpc', '[]')
    
    # Extract year
    match = re.search(grant_pattern, grant_date)
    if not match:
        continue
    year = int(match.group(1))
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                full_code = cpc_entry['code']
                # Extract level-4 part (first 4 characters like G06F, B60R, etc.)
                if len(full_code) >= 4:
                    level4_code = full_code[:4]
                    yearly_counts[level4_code][year] += 1
    except:
        continue

# Load second half 2019 data
second_half_file = locals()['var_functions.query_db:28']
with open(second_half_file, 'r') as f:
    second_half_2019 = json.load(f)

# Filter for second half and extract CPC codes
second_half_codes = set()
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']

for patent in second_half_2019:
    grant_date = patent.get('grant_date', '')
    cpc_str = patent.get('cpc', '[]')
    
    # Verify second half
    if not any(month in grant_date for month in second_half_months):
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                full_code = cpc_entry['code']
                if len(full_code) >= 4:
                    level4_code = full_code[:4]
                    second_half_codes.add(level4_code)
    except:
        continue

print('All level-4 CPC codes in German data:', len(yearly_counts))
print('German CPC from second half 2019:', len(second_half_codes))
print('Sample codes:', list(second_half_codes)[:10])

# Get year range
all_years = set()
for code in yearly_counts:
    all_years.update(yearly_counts[code].keys())
years = sorted(list(all_years))

print('Year range:', min(years), 'to', max(years))

# Calculate EMA for each CPC code
result = []
smoothing = 0.1

for cpc_code in second_half_codes:
    if cpc_code not in yearly_counts:
        continue
    
    # Get counts by year
    counts = [yearly_counts[cpc_code].get(year, 0) for year in years]
    
    # Calculate EMA
    ema = counts[0] if counts else 0
    ema_values = [ema]
    
    for i in range(1, len(years)):
        ema = (smoothing * counts[i]) + ((1 - smoothing) * ema)
        ema_values.append(ema)
    
    # Find best year (highest EMA)
    if ema_values:
        max_idx = ema_values.index(max(ema_values))
        best_year = years[max_idx]
        best_ema = ema_values[max_idx]
        
        result.append({
            'cpc_code': cpc_code,
            'titleFull': cpc_titles.get(cpc_code, 'N/A'),
            'best_year': best_year,
            'best_year_ema': best_ema
        })

# Sort by EMA descending
result_sorted = sorted(result, key=lambda x: x['best_year_ema'], reverse=True)

output = {
    'total_groups': len(result_sorted),
    'top_20_groups': result_sorted[:20]
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_german_patents': 18, 'total_cpc_entries': 219, 'sample_cpc_groups': ['F02D13/06', 'F02D41/20', 'G02B13/18', 'F02M59/102', 'G02B23/24', 'B60W30/194', 'C04B35/645', 'B41F22/00', 'F02D41/0087', 'H01R24/60']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'cpc_groups_count': 87, 'has_data': True}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_cpc_groups': 0, 'top_groups': []}}

exec(code, env_args)
