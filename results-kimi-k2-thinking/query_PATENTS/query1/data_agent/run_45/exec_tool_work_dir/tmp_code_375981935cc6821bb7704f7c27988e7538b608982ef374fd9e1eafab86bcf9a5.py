code = """import json
import numpy as np
from collections import defaultdict

# Load the publication data
file_path = 'file_storage/functions.query_db:6.json'
with open(file_path, 'r') as f:
    publications = json.load(f)

# Extract CPC codes and years, counting at group level (level 5)
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    cpc_data = pub['cpc']
    year = pub['year']
    
    if cpc_data and year:
        try:
            cpc_list = json.loads(cpc_data)
            
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code:
                    # Extract group code (level 5) - part before the slash
                    group_code = code.split('/')[0]
                    # Count all valid group codes
                    if len(group_code) >= 3:
                        cpc_year_counts[group_code][year] += 1
        except:
            continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(all_years)

# Filter for level 5 CPC codes
level_5_codes = []
for code in cpc_year_counts.keys():
    # Level 5 codes typically have 4-7 characters and mix letters/digits
    if 4 <= len(code) <= 7 and code[0].isalpha() and any(c.isdigit() for c in code):
        level_5_codes.append(code)

result_info = {
    'total_publications': len(publications),
    'available_years': len(sorted_years),
    'first_10_years': sorted_years[:10],
    'last_10_years': sorted_years[-10:],
    'total_cpc_groups': len(cpc_year_counts),
    'level_5_codes_count': len(level_5_codes),
    'sample_level_5_codes': level_5_codes[:10]
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}, 'var_functions.execute_python:20': {'file_exists': True, 'num_records': 277813, 'first_record_keys': ['cpc', 'year']}}

exec(code, env_args)
