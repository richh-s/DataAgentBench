code = """import json
import pandas as pd
from collections import defaultdict
import re

# Get the file path from storage
result_file = locals()['var_functions.query_db:14']

# Read the data
with open(result_file, 'r') as f:
    data = json.load(f)

print('Number of records:', len(data))

# Step 1: Extract CPC codes and publication years
cpc_year_counts = defaultdict(lambda: defaultdict(int))
years_set = set()

cpc_pattern = re.compile(r'"code": "([^"]+)"')
year_pattern = re.compile(r'(\d{4})')

records_processed = 0
parse_errors = 0

for record in data:
    cpc_json = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
        
    year = int(year_match.group(1))
    if year < 1900 or year > 2100:
        continue
        
    years_set.add(year)
    
    # Extract CPC codes from the JSON string
    if not cpc_json or cpc_json == '[]':
        continue
        
    try:
        # Parse the JSON string
        cpc_list = json.loads(cpc_json)
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code or not isinstance(code, str):
                continue
                
            # Extract first 7 characters for level 5 CPC group
            # CPC format: Section-Class-Subclass-Group/Subgroup
            # Level 5 corresponds to Section-Class-Subclass-Main group
            # e.g., H01M04/13 -> H01M04 (7 chars)
            level5_code = code[:7]
            
            # Ensure it's a valid format (starts with letter, has 4 chars after)
            if len(level5_code) >= 5 and level5_code[0].isalpha():
                cpc_year_counts[level5_code][year] += 1
                
        records_processed += 1
        
    except json.JSONDecodeError as e:
        parse_errors += 1
        continue

print('Records processed:', records_processed)
print('Parse errors:', parse_errors)
print('Unique CPC level 5 groups:', len(cpc_year_counts))
print('Year range:', min(years_set), 'to', max(years_set))

# Show sample CPC groups
if cpc_year_counts:
    sample_items = list(cpc_year_counts.items())[:5]
    for cpc_code, year_counts in sample_items:
        print(f'{cpc_code}: {dict(sorted(list(year_counts.items())[:3]))}')

# Prepare output for next steps
output = {
    'cpc_year_counts': cpc_year_counts,
    'years': sorted(list(years_set))
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'num_records': 100, 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
