code = """import json
import re
from collections import defaultdict
import pandas as pd

# Get the file path from the storage
file_path = locals()['var_functions.query_db:18']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Initialize counters
year_cpc_counts = defaultdict(lambda: defaultdict(int))

# Pattern to extract the year from publication_date
year_pattern = re.compile(r'(\d{4})')

# Process each record
for record in data:
    pub_date = record.get('publication_date', '')
    cpc_field = record.get('cpc', '[]')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if year_match:
        year = int(year_match.group(1))
        
        # Parse CPC codes
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_entry in cpc_list:
                full_code = cpc_entry.get('code', '')
                if full_code and '/' in full_code:
                    # This is a level 5 (subgroup) code
                    year_cpc_counts[year][full_code] += 1
        except:
            continue

# Get all years and CPC codes
all_years = sorted(year_cpc_counts.keys())
all_cpc_codes = set()
for year_counts in year_cpc_counts.values():
    all_cpc_codes.update(year_counts.keys())

print(f"Years range: {min(all_years) if all_years else 'None'} to {max(all_years) if all_years else 'None'}")
print(f"Total CPC level 5 codes: {len(all_cpc_codes)}")

# Now we need to filter for level 5 codes specifically
# Level 5 CPC codes have the format: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Group (1-3 digits) + "/" + Subgroup (2-6 digits)
# For level 5, we need the full code with subgroup

# Calculate EMA for each CPC code
alpha = 0.2  # smoothing factor

cpc_ema_data = {}

for cpc_code in all_cpc_codes:
    # Get counts for each year for this CPC code
    yearly_counts = []
    for year in all_years:
        count = year_cpc_counts[year].get(cpc_code, 0)
        yearly_counts.append((year, count))
    
    # Calculate EMA for each year
    ema_values = []
    ema = None
    for year, count in yearly_counts:
        if ema is None:
            ema = count  # Initialize with first value
        else:
            ema = alpha * count + (1 - alpha) * ema
        ema_values.append((year, ema))
    
    cpc_ema_data[cpc_code] = ema_values

# Find the highest EMA for each year
year_top_ema = {}
for year in all_years:
    max_ema = 0
    top_cpc = None
    for cpc_code, ema_values in cpc_ema_data.items():
        for ema_year, ema_value in ema_values:
            if ema_year == year and ema_value > max_ema:
                max_ema = ema_value
                top_cpc = cpc_code
    if top_cpc:
        year_top_ema[year] = (top_cpc, max_ema)

# Find CPC codes whose best year is 2022
cpc_best_2022 = []
for cpc_code, ema_values in cpc_ema_data.items():
    # Find the year with maximum EMA
    max_ema_year = None
    max_ema_value = 0
    for year, ema_value in ema_values:
        if ema_value > max_ema_value:
            max_ema_value = ema_value
            max_ema_year = year
    
    # If the best year is 2022
    if max_ema_year == 2022:
        cpc_best_2022.append(cpc_code)

print(f"CPC codes with best year 2022: {len(cpc_best_2022)}")
print(f"Sample: {cpc_best_2022[:10]}")

result_summary = {
    'years_range': [min(all_years), max(all_years)],
    'total_level5_codes': len(all_cpc_codes),
    'codes_best_2022': len(cpc_best_2022),
    'sample_codes_2022': cpc_best_2022[:10]
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total_records': 5, 'years_range': [2020, 2021], 'unique_cpc_groups': 18, 'sample_data_points': [[2021, {'C01B': 6, 'H01M': 25, 'C01G': 3, 'C01P': 3, 'Y02E': 1, 'B29C': 4, 'C08J': 7, 'B32B': 44, 'C09D': 1, 'B29L': 2, 'C08G': 5, 'B29K': 4, 'H01H': 11}], [2020, {'F16H': 22, 'A61K': 4, 'C12N': 12, 'A01K': 3, 'A61P': 1}]]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'total_records': '277813'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
