code = """import json
import re
from collections import defaultdict

# Get the file path from the storage
file_path = locals()['var_functions.query_db:18']

# Read the data from the file efficiently
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Initialize counters - use simple dicts for better performance
year_cpc_counts = defaultdict(lambda: defaultdict(int))

# Pattern to extract the year from publication_date
year_pattern = re.compile(r'(\d{4})')

# Process each record - focus on recent years and level 5 CPC codes
for record in data:
    pub_date = record.get('publication_date', '')
    cpc_field = record.get('cpc', '[]')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if year_match:
        year = int(year_match.group(1))
        # Focus on recent years to reduce computation
        if year >= 2010:
            # Parse CPC codes
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_entry in cpc_list:
                    full_code = cpc_entry.get('code', '')
                    if full_code and '/' in full_code:
                        # Count level 5 codes
                        year_cpc_counts[year][full_code] += 1
            except:
                continue

# Get all years and CPC codes from recent data
all_years = sorted(year_cpc_counts.keys())
print(f"Years with data (2010+): {all_years}")

# Flatten and find unique CPC codes
all_cpc_codes = set()
for year_counts in year_cpc_counts.values():
    all_cpc_codes.update(year_counts.keys())

print(f"Unique level 5 CPC codes (2010+): {len(all_cpc_codes)}")

# Calculate EMA for each CPC code efficiently
alpha = 0.2
cpc_best_year = {}

for cpc_code in all_cpc_codes:
    # Get counts for each year for this CPC code
    max_ema = 0
    best_year = None
    ema = 0
    
    for year in sorted(all_years):
        count = year_cpc_counts[year].get(cpc_code, 0)
        if year == min(all_years):
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = year
    
    if best_year:
        cpc_best_year[cpc_code] = best_year

# Find CPC codes whose best year is 2022
cpc_best_2022 = [cpc_code for cpc_code, best_year in cpc_best_year.items() if best_year == 2022]

print(f"CPC codes with best year 2022: {len(cpc_best_2022)}")

result_summary = {
    'years_analyzed': all_years,
    'total_level5_codes_recent': len(all_cpc_codes),
    'codes_best_2022': len(cpc_best_2022)
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total_records': 5, 'years_range': [2020, 2021], 'unique_cpc_groups': 18, 'sample_data_points': [[2021, {'C01B': 6, 'H01M': 25, 'C01G': 3, 'C01P': 3, 'Y02E': 1, 'B29C': 4, 'C08J': 7, 'B32B': 44, 'C09D': 1, 'B29L': 2, 'C08G': 5, 'B29K': 4, 'H01H': 11}], [2020, {'F16H': 22, 'A61K': 4, 'C12N': 12, 'A01K': 3, 'A61P': 1}]]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'total_records': '277813'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
