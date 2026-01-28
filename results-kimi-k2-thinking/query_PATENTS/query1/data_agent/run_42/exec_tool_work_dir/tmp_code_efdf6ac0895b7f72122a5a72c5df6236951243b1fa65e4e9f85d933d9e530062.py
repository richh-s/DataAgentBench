code = """import json
import re

# Read the publication data with cpc_yearly_counts
file_path = str(locals()['var_functions.execute_python:14']).strip("'")
with open(file_path, 'r') as f:
    result_data = json.load(f)

cpc_yearly_counts = result_data['cpc_yearly_counts']

# Calculate EMA for each CPC group
alpha = 0.2  # smoothing factor
results = []

for cpc_code, yearly_counts in cpc_yearly_counts.items():
    # Sort years chronologically
    sorted_years = sorted(yearly_counts.keys())
    
    if len(sorted_years) < 2:
        continue
    
    # Calculate EMA
    ema_values = {}
    
    # Initialize with first year
    first_year = sorted_years[0]
    ema_values[first_year] = float(yearly_counts[first_year])
    
    # Calculate subsequent EMAs
    prev_ema = ema_values[first_year]
    for year in sorted_years[1:]:
        current_value = float(yearly_counts.get(year, 0))
        ema = alpha * current_value + (1 - alpha) * prev_ema
        ema_values[year] = ema
        prev_ema = ema
    
    # Find best year (highest EMA)
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    best_ema = ema_values[best_year]
    
    results.append({
        'cpc_code': cpc_code,
        'best_year': int(best_year),
        'best_ema': float(best_ema)
    })

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = [r for r in results if r['best_year'] == 2022]

# Extract and sort the CPC codes
answer_codes = [item['cpc_code'] for item in cpc_best_2022]
answer_codes.sort()

# Output as JSON-serializable string
result_json = json.dumps(answer_codes)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'cpc_yearly_counts': {}, 'year_range': None, 'total_cpc_codes': 0, 'total_publications': 277813}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
