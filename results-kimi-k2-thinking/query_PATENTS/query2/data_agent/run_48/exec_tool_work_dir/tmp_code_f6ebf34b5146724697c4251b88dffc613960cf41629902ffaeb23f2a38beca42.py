code = """import json
import pandas as pd
from collections import defaultdict
import re
from datetime import datetime

# Load CPC level 4 definitions
cpc_file = locals()['var_functions.query_db:24']
with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

# Create CPC code to title mapping
cpc_titles = {defn['symbol'].strip(): defn['titleFull'] for defn in cpc_definitions}

# Filter for actual level-4 codes (1 letter + 3 digits)
level4_codes = []
for code, title in cpc_titles.items():
    pattern = r'^[A-Z]\d{2}[A-Z]$'  # e.g., G06F, B60R, etc.
    if re.match(pattern, code):
        level4_codes.append(code)

print('CPC Level-4 codes found:', len(level4_codes))
print('Sample codes:', level4_codes[:10])

# Load German patents data
german_file = locals()['var_functions.query_db:20']
with open(german_file, 'r') as f:
    german_patents = json.load(f)

# Parse grant dates and collect CPC counts by year and code
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
                # Get level-4 part (first 4 characters)
                if len(full_code) >= 4:
                    level4_code = full_code[:4]
                    if level4_code in level4_codes:
                        yearly_counts[level4_code][year] += 1
    except:
        continue

# Get unique years sorted
all_years = set()
for code in yearly_counts:
    all_years.update(yearly_counts[code].keys())
years = sorted(list(all_years))
print('Years range:', years[:5], '...', years[-5:])

# Filter for second half of 2019 data
second_half_cpc_file = locals()['var_functions.query_db:28']
with open(second_half_cpc_file, 'r') as f:
    second_half_2019 = json.load(f)

# Identify CPC groups that appear in second half 2019
second_half_codes = set()
for patent in second_half_2019:
    cpc_str = patent.get('cpc', '[]')
    grant_date = patent.get('grant_date', '')
    
    # Check if second half of 2019
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
    if not any(month in grant_date for month in second_half_months):
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                full_code = cpc_entry['code']
                if len(full_code) >= 4:
                    level4_code = full_code[:4]
                    if level4_code in level4_codes:
                        second_half_codes.add(level4_code)
    except:
        continue

print('CPC groups from second half 2019:', len(second_half_codes))

# Build results
results = []
smoothing_factor = 0.1

for cpc_code in second_half_codes:
    # Get counts by year
    counts_by_year = {year: yearly_counts[cpc_code].get(year, 0) for year in years}
    
    # Calculate EMA
    ema_values = {}
    ema = None
    for year in sorted(years):
        count = counts_by_year[year]
        if ema is None:
            ema = count  # Initialize with first value
        else:
            ema = (smoothing_factor * count) + ((1 - smoothing_factor) * ema)
        ema_values[year] = ema
    
    # Find best year (highest EMA)
    if ema_values:
        best_year = max(ema_values, key=ema_values.get)
        results.append({
            'cpc_code': cpc_code,
            'titleFull': cpc_titles.get(cpc_code, 'N/A'),
            'best_year': best_year,
            'best_year_ema': ema_values[best_year]
        })

# Sort by best EMA descending
results_sorted = sorted(results, key=lambda x: x['best_year_ema'], reverse=True)

final_output = {
    'total_cpc_groups': len(results_sorted),
    'top_groups': results_sorted[:20]
}

print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_german_patents': 18, 'total_cpc_entries': 219, 'sample_cpc_groups': ['F02D13/06', 'F02D41/20', 'G02B13/18', 'F02M59/102', 'G02B23/24', 'B60W30/194', 'C04B35/645', 'B41F22/00', 'F02D41/0087', 'H01R24/60']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'cpc_groups_count': 87, 'has_data': True}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
