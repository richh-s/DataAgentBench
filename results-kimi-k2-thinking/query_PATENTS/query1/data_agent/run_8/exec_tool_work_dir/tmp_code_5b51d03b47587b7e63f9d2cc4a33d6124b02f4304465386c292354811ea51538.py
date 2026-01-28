code = """import json
import pandas as pd
import re
from collections import defaultdict
import numpy as np

# Get file path from storage
file_path = locals()['var_functions.query_db:5']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse CPC codes and count filings per year
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for record in data:
    # Get year from publication date
    pub_date_str = record['publication_date']
    year_match = re.search(r'(\d{4})', pub_date_str)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Skip old years to focus on modern patent activity
    if year < 1900 or year > 2023:
        continue
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            # Extract level 5 CPC codes: format like A61K31/00, H01M10/05
            # Pattern: 1 letter + 2 digits + optional letter + digits + / + 2 digits
            if re.match(r'^[A-Z][0-9]{2}[A-Z]?[0-9]+/[0-9]{2}$', code):
                cpc_year_counts[code][year] += 1
    except:
        continue

# Get all CPC codes and years
cpc_codes = list(cpc_year_counts.keys())
all_years = sorted(set(year for cpc in cpc_codes for year in cpc_year_counts[cpc].keys()))

print(f'CPC codes: {len(cpc_codes)}')
print(f'Years: {len(all_years)} from {all_years[0]} to {all_years[-1]}')

# Calculate EMA for each CPC code
smoothing_factor = 0.2
best_cpc_for_2022 = []

for cpc in cpc_codes[:1000]:  # Process a subset first for testing
    year_counts = cpc_year_counts[cpc]
    if not year_counts:
        continue
    
    # Create series for all years
    years = sorted(year_counts.keys())
    values = [year_counts[year] for year in years]
    
    # Calculate EMA
    ema_values = []
    ema_prev = values[0]  # Initialize with first value
    ema_values.append(ema_prev)
    
    for i in range(1, len(values)):
        ema_current = smoothing_factor * values[i] + (1 - smoothing_factor) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find year with highest EMA
    max_ema_idx = np.argmax(ema_values)
    best_year = years[max_ema_idx]
    best_ema = ema_values[max_ema_idx]
    
    if best_year == 2022:
        best_cpc_for_2022.append({
            'cpc': cpc,
            'best_year': best_year,
            'max_ema': best_ema,
            'value_in_best_year': values[max_ema_idx]
        })

print(f'CPC codes with best year 2022: {len(best_cpc_for_2022)}')
if best_cpc_for_2022:
    print('Sample:')
    for item in best_cpc_for_2022[:5]:
        print(f"  {item['cpc']}: EMA={item['max_ema']:.2f}, filings={item['value_in_best_year']}")

result = {
    'num_candidates': len(best_cpc_for_2022),
    'sample_cpc': [item['cpc'] for item in best_cpc_for_2022[:10]]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:9': ['cpc_definition'], 'var_functions.execute_python:14': {'num_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'num_cpc_codes': 70324, 'num_years': 186, 'cpc_sample': ['C01B33/00', 'C01B35/00', 'H01M10/05', 'C01G45/00', 'C01P2002/76', 'Y02E60/10', 'H01M2004/02', 'H01M4/13', 'H01M4/52', 'H01M4/50'], 'years_sample': [1837, 1839, 1841, 1842, 1843]}}

exec(code, env_args)
