code = """import pandas as pd
import numpy as np
import json
import re
from collections import defaultdict

# Load the publication data file
file_path = var_functions.query_db:10

with open(file_path, 'r') as f:
    publications = json.load(f)

print(f'Loaded {len(publications)} publications')

# Extract year and CPC codes from publications
year_pub_data = []
for pub in publications:
    # Parse publication date
    pub_date = pub['publication_date']
    year_match = re.search(r'(\d{4})', pub_date)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Parse CPC codes (JSON string)
    cpc_str = pub['cpc']
    try:
        cpc_list = json.loads(cpc_str)
        codes = [item['code'] for item in cpc_list if 'code' in item]
        year_pub_data.append({
            'year': year,
            'cpc_codes': codes
        })
    except:
        continue

print(f'Processed {len(year_pub_data)} publication records')

# Count patents per year
year_counts = defaultdict(int)
for item in year_pub_data:
    year_counts[item['year']] += 1
    
years = sorted(year_counts.keys())
print(f'Year range: {min(years)} to {max(years)}')

# Calculate EMA for each CPC group at level 5
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for item in year_pub_data:
    year = item['year']
    for code in item['cpc_codes']:
        # Get level 5 group (first 5 characters before any /)
        base_code = code.split('/')[0]
        if len(base_code) >= 5:
            level5_code = base_code[:5]
            cpc_year_counts[level5_code][year] += 1

print(f'Found {len(cpc_year_counts)} CPC groups at level 5')

# Calculate EMA for each group
alpha = 0.2
results = []

for cpc_code in cpc_year_counts:
    counts_by_year = cpc_year_counts[cpc_code]
    
    # Get all years with data
    years = sorted(counts_by_year.keys())
    if not years:
        continue
    
    # Build time series sorted by year
    time_series = []
    for year in range(min(years), max(years) + 1):
        count = counts_by_year.get(year, 0)
        time_series.append((year, count))
    
    # Calculate EMA
    ema_values = []
    ema_prev = None
    for year, count in time_series:
        if ema_prev is None:
            ema = float(count)
        else:
            ema = alpha * count + (1 - alpha) * ema_prev
        ema_prev = ema
        ema_values.append((year, ema))
    
    # Find year with highest EMA
    best_year, best_ema = max(ema_values, key=lambda x: x[1])
    
    # Only include if best year is 2022
    if best_year == 2022:
        results.append({
            'cpc_code': cpc_code,
            'best_ema': best_ema
        })

# Sort by EMA descending
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

print(f'Found {len(results_sorted)} CPC groups with best year 2022')

# Output just the CPC codes
output_codes = [r['cpc_code'] for r in results_sorted]
print('__RESULT__:')
print(json.dumps(output_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'count': '277813'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
