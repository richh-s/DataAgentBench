code = """import json
import re
from collections import defaultdict

# Load the publication data
file_path = 'file_storage/functions.query_db:26.json'
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f"Loaded {len(publications)} publications")

# Extract CPC codes and years
cpc_year_counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r'(\d{4})\s*$')

for pub in publications:
    cpc_data = pub['cpc']
    pub_date = pub['publication_date']
    
    if cpc_data and pub_date:
        # Extract year
        match = year_pattern.search(pub_date.strip())
        if match:
            year = match.group(1)
            year_int = int(year)
            if 1970 <= year_int <= 2030:  # Reasonable patent year range
                try:
                    cpc_list = json.loads(cpc_data)
                    
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code', '')
                        if code:
                            # Get group code (part before slash)
                            group_code = code.split('/')[0]
                            # Filter for level 5 codes
                            if 4 <= len(group_code) <= 7:
                                cpc_year_counts[group_code][year] += 1
                except:
                    continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(all_years)

# Get level 5 CPC codes
level_5_codes = []
for code in cpc_year_counts.keys():
    if 4 <= len(code) <= 7:
        level_5_codes.append(code)

print('__RESULT__:')
print(json.dumps({
    'total_publications': len(publications),
    'available_years': len(sorted_years),
    'first_5_years': sorted_years[:5],
    'last_5_years': sorted_years[-5:],
    'total_cpc_groups': len(cpc_year_counts),
    'level_5_codes_count': len(level_5_codes)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}, 'var_functions.execute_python:20': {'file_exists': True, 'num_records': 277813, 'first_record_keys': ['cpc', 'year']}, 'var_functions.execute_python:24': {'total_publications': 277813, 'available_years': 218, 'first_10_years': [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th'], 'last_10_years': ['23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', 'Date'], 'total_cpc_groups': 9960, 'level_5_codes_count': 7247, 'sample_level_5_codes': ['C01B33', 'C01B35', 'H01M10', 'C01G45', 'Y02E60', 'H01M4', 'F16H47', 'F16H37', 'F16H3', 'B29C70']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
