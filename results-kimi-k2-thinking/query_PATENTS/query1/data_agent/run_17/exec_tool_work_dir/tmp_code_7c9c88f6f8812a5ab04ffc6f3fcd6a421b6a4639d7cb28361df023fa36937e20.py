code = """import json
import re
from collections import defaultdict
import statistics

# Get the file path from storage
result_file = locals()['var_functions.query_db:14']

# Read the data
with open(result_file, 'r') as f:
    data = json.load(f)

# Process CPC codes and dates
print('Processing', len(data), 'records...')

# Key data structures
cpc_year_counts = defaultdict(lambda: defaultdict(int))  # CPC -> year -> count
year_min = 9999
year_max = 0
processed_records = 0
parse_errors = 0

year_pattern = re.compile(r'(\d{4})')

for record in data:
    cpc_json = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    # Extract year from publication date
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
        
    year = int(year_match.group(1))
    if year < 1900 or year > 2100:
        continue
    
    year_min = min(year_min, year)
    year_max = max(year_max, year)
    
    # Parse CPC codes
    if not cpc_json or cpc_json == '[]':
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code or not isinstance(code, str):
                continue
            
            # Extract level 5 CPC (first 7 characters)
            # Format: H01M04/1315 -> H01M04 (7 chars)
            level5_code = code[:7]
            
            # Validate format (should start with letter, contain alphanumeric)
            if len(level5_code) >= 4 and level5_code[0].isalpha():
                cpc_year_counts[level5_code][year] += 1
        
        processed_records += 1
        
    except json.JSONDecodeError:
        parse_errors += 1
        continue

print('Data processed. Records:', processed_records, 'Errors:', parse_errors)
print('Year range:', year_min, 'to', year_max)
print('Unique CPC level 5 groups:', len(cpc_year_counts))

# Generate complete year range for EMA calculation
all_years = list(range(year_min, year_max + 1))
print('Complete year range:', len(all_years), 'years')

# Filter to only CPC groups with sufficient data (at least 3 years)
valid_cpc_groups = {}
for cpc, year_counts in cpc_year_counts.items():
    unique_years = len(year_counts)
    if unique_years >= 3:
        valid_cpc_groups[cpc] = year_counts

print('CPC groups with >=3 years:', len(valid_cpc_groups))

# Calculate Exponential Moving Average (EMA) for each CPC group
# EMA formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
alpha = 0.2  # Smoothing factor

cpc_ema_data = {}  # CPC -> year -> EMA
cpc_best_years = {}  # CPC -> (best_year, max_ema)

for cpc, year_counts in valid_cpc_groups.items():
    # Create yearly count series (0 for missing years)
    yearly_counts = [year_counts.get(year, 0) for year in all_years]
    
    # Calculate EMA
    ema_values = []
    ema_prev = yearly_counts[0]  # Initialize with first value
    
    for count in yearly_counts:
        ema_current = alpha * count + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Store EMA per year
    ema_per_year = {year: ema for year, ema in zip(all_years, ema_values)}
    cpc_ema_data[cpc] = ema_per_year
    
    # Find best year (max EMA)
    best_year = max(ema_per_year, key=ema_per_year.get)
    max_ema = ema_per_year[best_year]
    cpc_best_years[cpc] = (best_year, max_ema)

# Find CPC groups where best year is 2022
cpc_best_2022 = []
for cpc, (best_year, max_ema) in cpc_best_years.items():
    if best_year == 2022:
        cpc_best_2022.append((cpc, max_ema))

# Sort by EMA value descending
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)

print('CPC groups with best year 2022:', len(cpc_best_2022))
print('Top 10 CPC groups:')
for i, (cpc, ema) in enumerate(cpc_best_2022[:10]):
    print(f'  {i+1}. {cpc}: EMA={ema:.2f}')

# Prepare final output
output_cpc_codes = [cpc for cpc, ema in cpc_best_2022]

print('__RESULT__:')
print(json.dumps(output_cpc_codes))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'num_records': 100, 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)
