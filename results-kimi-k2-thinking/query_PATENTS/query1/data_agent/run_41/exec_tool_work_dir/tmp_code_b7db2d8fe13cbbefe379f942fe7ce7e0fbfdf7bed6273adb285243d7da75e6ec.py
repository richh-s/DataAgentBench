code = """import json
import re
from collections import Counter

# Load publication data
pub_file = locals()['var_functions.query_db:12']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print(f'Analyzing {len(pub_data)} records...')

# Extract all years and analyze data distribution
year_counts = Counter()
all_years = set()

cpc_samples = []
cpc_count = 0

for item in pub_data:
    pub_date = item.get('publication_date', '')
    if not pub_date:
        continue
        
    year_match = re.search(r'(\d{4})', pub_date)
    if not year_match:
        continue
        
    year = int(year_match.group(1))
    year_counts[year] += 1
    all_years.add(year)
    
    # Also count CPC codes
    cpc_str = item.get('cpc', '[]')
    if cpc_str and cpc_str != '[]':
        try:
            cpc_list = json.loads(cpc_str)
            cpc_count += len(cpc_list)
            if len(cpc_samples) < 10:
                cpc_samples.extend([c.get('code', '') for c in cpc_list if c.get('code')])
        except:
            pass

sorted_years = sorted(all_years)
print(f'Years found: {sorted_years}')
print(f'Year counts: {dict(year_counts.most_common(10))}')
print(f'Total CPC code entries: {cpc_count}')
print(f'Sample CPC codes: {cpc_samples[:10]}')

# Check which years have most data
print('\nTop years by record count:')
for year, count in year_counts.most_common(10):
    print(f'{year}: {count} records')

result = {
    'years': sorted_years,
    'year_counts': dict(year_counts),
    'total_cpc_entries': cpc_count,
    'sample_cpcs': cpc_samples[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'count': 0, 'groups': []}}

exec(code, env_args)
