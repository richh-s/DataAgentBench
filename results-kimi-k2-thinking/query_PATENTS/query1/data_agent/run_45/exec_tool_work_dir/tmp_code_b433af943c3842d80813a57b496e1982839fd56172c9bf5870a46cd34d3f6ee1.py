code = """import json
import re
import numpy as np
from collections import defaultdict

# Load the publication data
file_path = 'file_storage/functions.query_db:26.json'
with open(file_path, 'r') as f:
    publications = json.load(f)

# Extract CPC codes and years, counting at group level
cpc_year_counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r'(\d{4})\s*$')

for pub in publications:
    cpc_data = pub['cpc']
    pub_date = pub['publication_date']
    
    if cpc_data and pub_date:
        match = year_pattern.search(pub_date.strip())
        if match:
            year = match.group(1)
            year_int = int(year)
            if 1970 <= year_int <= 2030:
                try:
                    cpc_list = json.loads(cpc_data)
                    
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code', '')
                        if code:
                            group_code = code.split('/')[0]
                            if 4 <= len(group_code) <= 7:
                                cpc_year_counts[group_code][year] += 1
                except:
                    continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(all_years)
year_to_idx = {year: idx for idx, year in enumerate(sorted_years)}

# Calculate EMA for each CPC code
ema_alpha = 0.2
cpc_best_year = {}
cpc_2022_max_ema = {}

for cpc_code, year_counts in cpc_year_counts.items():
    # Create time series
    counts = [0] * len(sorted_years)
    for year, count in year_counts.items():
        if year in year_to_idx:
            counts[year_to_idx[year]] = count
    
    # Calculate EMA
    ema_prev = 0
    ema_values = []
    for i, count in enumerate(counts):
        if i == 0:
            ema = count  # First EMA is the first value
        else:
            ema = (ema_alpha * count) + ((1 - ema_alpha) * ema_prev)
        ema_values.append(ema)
        ema_prev = ema
    
    # Find best year (year with highest EMA)
    max_ema_idx = np.argmax(ema_values)
    best_year = sorted_years[max_ema_idx]
    max_ema_value = ema_values[max_ema_idx]
    
    cpc_best_year[cpc_code] = best_year
    if best_year == '2022':
        cpc_2022_max_ema[cpc_code] = max_ema_value

# Get CPC codes with 2022 as best year, sorted by EMA value
cpc_2022_best = sorted(cpc_2022_max_ema.keys(), key=lambda x: cpc_2022_max_ema[x], reverse=True)

total_cpc_codes = len(cpc_best_year)
total_2022_best = len(cpc_2022_best)
highest_ema_2022 = cpc_2022_max_ema[cpc_2022_best[0]] if cpc_2022_best else 0

result = {
    'total_cpc_codes': total_cpc_codes,
    'num_2022_best': total_2022_best,
    'sample_2022_codes': cpc_2022_best[:20],
    'top_5_codes_with_ema': [(code, round(cpc_2022_max_ema[code], 2)) for code in cpc_2022_best[:5]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}, 'var_functions.execute_python:20': {'file_exists': True, 'num_records': 277813, 'first_record_keys': ['cpc', 'year']}, 'var_functions.execute_python:24': {'total_publications': 277813, 'available_years': 218, 'first_10_years': [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th'], 'last_10_years': ['23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', 'Date'], 'total_cpc_groups': 9960, 'level_5_codes_count': 7247, 'sample_level_5_codes': ['C01B33', 'C01B35', 'H01M10', 'C01G45', 'Y02E60', 'H01M4', 'F16H47', 'F16H37', 'F16H3', 'B29C70']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'total_publications': 277813, 'available_years': 55, 'first_5_years': ['1970', '1971', '1972', '1973', '1974'], 'last_5_years': ['2020', '2021', '2022', '2023', '2024'], 'total_cpc_groups': 6994, 'level_5_codes_count': 6994}}

exec(code, env_args)
