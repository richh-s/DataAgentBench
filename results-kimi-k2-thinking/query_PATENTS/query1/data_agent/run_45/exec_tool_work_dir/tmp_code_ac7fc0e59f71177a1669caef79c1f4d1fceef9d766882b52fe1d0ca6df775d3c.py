code = """import json
import re
import numpy as np
from collections import defaultdict

# Load the publication data
with open('file_storage/functions.query_db:58.json', 'r') as f:
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
                            if 4 <= len(group_code) <= 7 and group_code[0].isalpha() and any(c.isdigit() for c in group_code):
                                cpc_year_counts[group_code][year] += 1
                except:
                    continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(all_years)
year_to_idx = {year: idx for idx, year in enumerate(sorted_years)}

# Calculate EMA for each CPC code with smoothing factor 0.2
ema_alpha = 0.2
cpc_best_year = {}

for cpc_code, year_counts in cpc_year_counts.items():
    counts = [0] * len(sorted_years)
    for year, count in year_counts.items():
        if year in year_to_idx:
            counts[year_to_idx[year]] = count
    
    ema_prev = 0
    max_ema = -1
    best_year = sorted_years[0]
    
    for i, count in enumerate(counts):
        if i == 0:
            ema = count
        else:
            ema = (ema_alpha * count) + ((1 - ema_alpha) * ema_prev)
        
        if ema > max_ema:
            max_ema = ema
            best_year = sorted_years[i]
        
        ema_prev = ema
    
    cpc_best_year[cpc_code] = best_year

# Filter for CPC codes with best year = 2022
cpc_2022_best = [
    cpc_code for cpc_code, best_year in cpc_best_year.items()
    if best_year == '2022'
]

# Sort alphabetically
cpc_2022_best_sorted = sorted(cpc_2022_best)

# Write to a temp file for return_answer to read
with open('/tmp/cpc_2022_codes.txt', 'w') as f:
    for code in cpc_2022_best_sorted:
        f.write(code + '\n')

print('__RESULT__:')
print(json.dumps({'count': len(cpc_2022_best_sorted), 'file': '/tmp/cpc_2022_codes.txt'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}, 'var_functions.execute_python:20': {'file_exists': True, 'num_records': 277813, 'first_record_keys': ['cpc', 'year']}, 'var_functions.execute_python:24': {'total_publications': 277813, 'available_years': 218, 'first_10_years': [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th'], 'last_10_years': ['23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', 'Date'], 'total_cpc_groups': 9960, 'level_5_codes_count': 7247, 'sample_level_5_codes': ['C01B33', 'C01B35', 'H01M10', 'C01G45', 'Y02E60', 'H01M4', 'F16H47', 'F16H37', 'F16H3', 'B29C70']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'total_publications': 277813, 'available_years': 55, 'first_5_years': ['1970', '1971', '1972', '1973', '1974'], 'last_5_years': ['2020', '2021', '2022', '2023', '2024'], 'total_cpc_groups': 6994, 'level_5_codes_count': 6994}, 'var_functions.execute_python:34': {'total_cpc_codes': 6994, 'num_2022_best': 1089, 'sample_2022_codes': ['A61K31', 'H01L21', 'A61B5', 'H01L29', 'A61K9', 'G06F16', 'H04N21', 'H01L23', 'H04L67', 'A61B17', 'C22C38', 'G01N33', 'H04L63', 'G06F9', 'H04W4', 'C12N15', 'A61P35', 'H04L9', 'H01L24', 'G06Q20'], 'top_5_codes_with_ema': [['A61K31', 1602.45], ['H01L21', 1487.21], ['A61B5', 1230.51], ['H01L29', 838.8], ['A61K9', 793.19]]}, 'var_functions.execute_python:36': {'cpc_codes_2022_best': []}, 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
