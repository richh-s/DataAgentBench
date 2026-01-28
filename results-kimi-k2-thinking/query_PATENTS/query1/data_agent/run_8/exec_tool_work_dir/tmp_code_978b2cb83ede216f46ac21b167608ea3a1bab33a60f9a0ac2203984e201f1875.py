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
            if re.match(r'^[A-Z][0-9]{2}[A-Z]?[0-9]+/[0-9]{2}$', code):
                cpc_year_counts[code][year] += 1
    except:
        continue

# Process ALL CPC codes
cpc_codes = list(cpc_year_counts.keys())
smoothing_factor = 0.2
best_cpc_for_2022 = []

for cpc in cpc_codes:
    year_counts = cpc_year_counts[cpc]
    if not year_counts:
        continue
    
    # Create series for all years (1900-2023)
    all_years = list(range(1900, 2024))
    values = [year_counts.get(year, 0) for year in all_years]
    
    # Calculate EMA
    ema_values = []
    # Initialize with first non-zero value or first value
    first_val = next((v for v in values if v > 0), values[0])
    ema_prev = first_val
    ema_values.append(ema_prev)
    
    for i in range(1, len(values)):
        if values[i] > 0 or ema_prev > 0:  # Only update if there's activity
            ema_current = smoothing_factor * values[i] + (1 - smoothing_factor) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
        else:
            ema_values.append(0)
    
    # Find year with highest EMA
    max_ema_idx = np.argmax(ema_values)
    best_year = all_years[max_ema_idx]
    
    if best_year == 2022:
        best_cpc_for_2022.append(cpc)

print(f'CPC codes with best year 2022: {len(best_cpc_for_2022)}')
print('Sample CPC codes:', best_cpc_for_2022[:10])

result = {
    'peaked_in_2022': len(best_cpc_for_2022),
    'codes': best_cpc_for_2022[:20]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:9': ['cpc_definition'], 'var_functions.execute_python:14': {'num_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'num_cpc_codes': 70324, 'num_years': 186, 'cpc_sample': ['C01B33/00', 'C01B35/00', 'H01M10/05', 'C01G45/00', 'C01P2002/76', 'Y02E60/10', 'H01M2004/02', 'H01M4/13', 'H01M4/52', 'H01M4/50'], 'years_sample': [1837, 1839, 1841, 1842, 1843]}, 'var_functions.execute_python:18': {'num_candidates': 171, 'sample_cpc': ['C01P2002/76', 'B29C70/48', 'B32B27/34', 'B32B2255/02', 'B32B27/10', 'B32B2307/50', 'B32B5/18', 'A01K2267/03', 'A61P7/00', 'A61P1/16']}}

exec(code, env_args)
