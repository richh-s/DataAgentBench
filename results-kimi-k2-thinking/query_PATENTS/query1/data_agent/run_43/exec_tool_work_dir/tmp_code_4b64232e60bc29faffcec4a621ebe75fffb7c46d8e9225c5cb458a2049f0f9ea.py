code = """import json
import re
from collections import defaultdict

# Get the file path from the storage
file_path = locals()['var_functions.query_db:18']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Initialize counters
year_cpc_counts = defaultdict(lambda: defaultdict(int))

# Pattern to extract the year from publication_date
year_pattern = re.compile(r'(\d{4})')

# Process each record - focus on recent years
for record in data:
    pub_date = record.get('publication_date', '')
    cpc_field = record.get('cpc', '[]')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if year_match:
        year = int(year_match.group(1))
        # Only process years from 2010 onwards
        if year >= 2010:
            # Parse CPC codes
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_entry in cpc_list:
                    full_code = cpc_entry.get('code', '')
                    if full_code and '/' in full_code:
                        # Extract level 5 CPC code (full format: Section+Class+Subclass+Group/Subgroup)
                        year_cpc_counts[year][full_code] += 1
            except:
                continue

# Get all years from recent data
all_years = sorted(year_cpc_counts.keys())
print(f"Years with data: {min(all_years)} to {max(all_years)}")

# Get all unique CPC codes
all_cpc_codes = set()
for year_counts in year_cpc_counts.values():
    all_cpc_codes.update(year_counts.keys())

print(f"Total unique level 5 CPC codes: {len(all_cpc_codes)}")

# Calculate EMA and find best year for each CPC code
alpha = 0.2
cpc_best_2022 = []

# For debugging: track a sample of codes
sample_codes = list(all_cpc_codes)[:5]
print(f"Sample CPC codes: {sample_codes}")

for cpc_code in all_cpc_codes:
    # Get all years data for this CPC code
    max_ema = 0
    best_year = None
    ema = 0
    first_year_processed = False
    
    # Process in chronological order
    for year in sorted(all_years):
        count = year_cpc_counts[year].get(cpc_code, 0)
        
        if not first_year_processed:
            ema = count
            first_year_processed = True
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track the best year
        if ema > max_ema:
            max_ema = ema
            best_year = year
    
    # If this CPC code's best year is 2022, add it to the list
    if best_year == 2022:
        cpc_best_2022.append(cpc_code)

print(f"CPC codes with best year 2022: {len(cpc_best_2022)}")

# Return the actual list of CPC codes
result = {
    'cpc_codes_best_2022': cpc_best_2022,
    'count': len(cpc_best_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total_records': 5, 'years_range': [2020, 2021], 'unique_cpc_groups': 18, 'sample_data_points': [[2021, {'C01B': 6, 'H01M': 25, 'C01G': 3, 'C01P': 3, 'Y02E': 1, 'B29C': 4, 'C08J': 7, 'B32B': 44, 'C09D': 1, 'B29L': 2, 'C08G': 5, 'B29K': 4, 'H01H': 11}], [2020, {'F16H': 22, 'A61K': 4, 'C12N': 12, 'A01K': 3, 'A61P': 1}]]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'total_records': '277813'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:24': {'years_analyzed': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'total_level5_codes_recent': 141687, 'codes_best_2022': 17241}}

exec(code, env_args)
