code = """import json
import re
from collections import defaultdict

# Get the file path from storage
result_file = locals()['var_functions.query_db:14']

# Read the data
with open(result_file, 'r') as f:
    data = json.load(f)

print('Processing', len(data), 'records...')

# Data structures
cpc_year_counts = defaultdict(lambda: defaultdict(int))
years_set = set()
processed_records = 0
parse_errors = 0

year_pattern = re.compile(r'(\d{4})')

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
    
    # Parse CPC codes
    if not cpc_json or cpc_json == '[]':
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code or not isinstance(code, str):
                continue
            
            # Extract level 5 CPC code (first 7 characters)
            # Format: H01M04/1315 -> H01M04 (7 chars including position of slash)
            level5_code = code[:7]
            
            # Ensure it's a valid format (starts with letter)
            if len(level5_code) >= 4 and level5_code[0].isalpha():
                cpc_year_counts[level5_code][year] += 1
                
        processed_records += 1
        
    except json.JSONDecodeError:
        parse_errors += 1
        continue

# Calculate EMA
alpha = 0.2
all_years = sorted(list(years_set))
cpc_best_2022 = []

total_cpc_groups = len(cpc_year_counts)
print(f'Found {total_cpc_groups} CPC level 5 groups')
print(f'Year range: {min(years_set)} to {max(years_set)}')

# Process each CPC group
for cpc, year_counts in cpc_year_counts.items():
    # Only process groups with data in 2022 or near that period
    if 2022 not in year_counts and 2021 not in year_counts and 2023 not in year_counts:
        continue
    
    # Create yearly count series
    yearly_counts = [year_counts.get(year, 0) for year in all_years]
    
    # Calculate EMA
    if not yearly_counts:
        continue
        
    ema_prev = yearly_counts[0]
    max_ema = -1
    best_year = None
    
    for year, count in zip(all_years, yearly_counts):
        ema_current = alpha * count + (1 - alpha) * ema_prev
        
        if ema_current > max_ema:
            max_ema = ema_current
            best_year = year
            
        ema_prev = ema_current
    
    # Check if best year is 2022
    if best_year == 2022:
        cpc_best_2022.append((cpc, max_ema))

# Sort by EMA value descending
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)

print(f'Found {len(cpc_best_2022)} CPC groups with best year 2022')

if cpc_best_2022:
    print('Top 20 CPC groups with best year 2022:')
    for i, (cpc, ema) in enumerate(cpc_best_2022[:20]):
        print(f'  {i+1}. {cpc} (EMA: {ema:.2f})')

# Extract just the CPC codes
cpc_codes_result = [cpc for cpc, ema in cpc_best_2022]

output = {
    'total_cpc_groups_analyzed': total_cpc_groups,
    'cpc_groups_best_2022': len(cpc_best_2022),
    'cpc_codes': cpc_codes_result
}

print('__RESULT__:')
print(json.dumps(cpc_codes_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'num_records': 100, 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json'}

exec(code, env_args)
