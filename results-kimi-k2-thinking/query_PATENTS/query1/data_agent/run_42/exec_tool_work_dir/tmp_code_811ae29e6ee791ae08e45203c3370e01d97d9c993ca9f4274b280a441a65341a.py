code = """import json
import re

# Read the publication data with cpc_yearly_counts
file_path = 'var_functions.execute_python:14'
with open(file_path.replace("'", ""), 'r') as f:
    result_data = json.load(f)

cpc_yearly_counts = result_data['cpc_yearly_counts']

print(f"Total CPC groups to process: {len(cpc_yearly_counts)}")
if cpc_yearly_counts:
    sample_cpc = list(cpc_yearly_counts.keys())[0]
    print(f"Sample CPC {sample_cpc} data: {cpc_yearly_counts[sample_cpc]}")

# Determine year range
all_years = set()
for counts in cpc_yearly_counts.values():
    all_years.update(counts.keys())

if all_years:
    min_year = min(all_years)
    max_year = max(all_years)
    print(f"Year range: {min_year} to {max_year}")
else:
    print("No years found")

# Calculate EMA for each CPC group
alpha = 0.2  # smoothing factor
results = []

for cpc_code, yearly_counts in cpc_yearly_counts.items():
    # Sort years chronologically
    sorted_years = sorted(yearly_counts.keys())
    
    if len(sorted_years) < 2:
        continue  # Need at least 2 years for EMA
    
    # Calculate EMA
    ema_values = {}
    
    # Initialize with first year
    first_year = sorted_years[0]
    ema_values[first_year] = yearly_counts[first_year]
    
    # Calculate subsequent EMAs
    prev_ema = ema_values[first_year]
    for year in sorted_years[1:]:
        current_value = yearly_counts.get(year, 0)
        ema = alpha * current_value + (1 - alpha) * prev_ema
        ema_values[year] = ema
        prev_ema = ema
    
    # Find best year (highest EMA)
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    best_ema = ema_values[best_year]
    
    # Also get raw count for best year
    best_year_raw_count = yearly_counts.get(best_year, 0)
    
    results.append({
        'cpc_code': cpc_code,
        'best_year': best_year,
        'best_ema': best_ema,
        'best_year_raw_count': best_year_raw_count,
        'ema_values': ema_values,
        'yearly_counts': yearly_counts
    })

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = [r for r in results if r['best_year'] == 2022]

print(f"\nTotal CPC groups: {len(results)}")
print(f"CPC groups with best year 2022: {len(cpc_best_2022)}")

if cpc_best_2022:
    print(f"\nTop 10 CPC groups with best year 2022:")
    sorted_2022 = sorted(cpc_best_2022, key=lambda x: x['best_ema'], reverse=True)
    for i, item in enumerate(sorted_2022[:10]):
        print(f"{i+1}. {item['cpc_code']}: EMA={item['best_ema']:.2f}, Raw count={item['best_year_raw_count']}")

# Return just the CPC codes
answer_codes = [item['cpc_code'] for item in cpc_best_2022]
answer_codes.sort()

print(f"\nFinal answer - CPC codes with best year 2022:")
for code in answer_codes:
    print(code)

print('__RESULT__:')
print(json.dumps(answer_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'cpc_yearly_counts': {}, 'year_range': None, 'total_cpc_codes': 0, 'total_publications': 277813}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
