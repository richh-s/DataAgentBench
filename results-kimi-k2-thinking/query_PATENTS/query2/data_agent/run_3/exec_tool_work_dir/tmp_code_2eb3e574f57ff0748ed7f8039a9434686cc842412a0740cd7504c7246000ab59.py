code = """import json
import re
from collections import defaultdict

# Get the result from the previous query
query_result_key = 'var_functions.query_db:2'
result_file = locals()[query_result_key]

# Read the data
with open(result_file, 'r') as f:
    all_grants = json.load(f)

print(f"Total records loaded: {len(all_grants)}")

# Filter for German patents in second half of 2019
second_half_grants = []

for record in all_grants:
    grant_date = record.get('grant_date', '')
    patents_info = record.get('Patents_info', '')
    cpc_data = record.get('cpc', '')
    
    # Check for German patents (DE country code)
    if 'DE-' not in patents_info:
        continue
    
    # Check if grant date is in 2019
    if '2019' not in grant_date:
        continue
    
    # Extract month
    month = None
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
    if month_match:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month = month_map.get(month_name)
    else:
        # Try numeric month format
        numeric_match = re.search(r'(\d{1,2})[^\d]+2019', grant_date)
        if numeric_match:
            month = int(numeric_match.group(1))
    
    if month is None or month < 7 or month > 12:
        continue
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_data) if cpc_data else []
    except:
        cpc_list = []
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if code:
            second_half_grants.append({
                'month': month,
                'cpc_code': code
            })

print(f"German patents in second half 2019: {len(second_half_grants)}")

# Group by level 4 CPC codes
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))
cpc_code_mapping = {}

for grant in second_half_grants:
    full_code = grant['cpc_code']
    month = grant['month']
    
    # Extract level 4: e.g., G06F9 from G06F9/45533
    level4_match = re.match(r'^([A-Z]\d{2}[A-Z]\d)', full_code)
    if level4_match:
        level4_code = level4_match.group(1)
        cpc_code_mapping[level4_code] = full_code
        cpc_monthly_counts[level4_code][month] += 1

print(f"Unique level 4 CPC groups: {len(cpc_monthly_counts)}")

# Calculate EMA (Exponential Moving Average) for each CPC group
alpha = 0.1
best_months = {}

for level4_code, monthly_counts in cpc_monthly_counts.items():
    months = sorted(monthly_counts.items())
    
    ema = None
    max_ema = 0
    best_month_data = None
    
    for month, count in months:
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_month_data = {
                'month': month,
                'count': count,
                'ema': ema
            }
    
    if best_month_data:
        best_months[level4_code] = best_month_data

print(f"CPC groups with EMA data: {len(best_months)}")

# Get top results (sorted by EMA)
top_results = sorted(best_months.items(), key=lambda x: x[1]['ema'], reverse=True)

# Prepare final data
final_cpc_groups = []
for level4_code, data in top_results[:20]:  # Get top 20 for now
    final_cpc_groups.append({
        'cpc_level4_code': level4_code,
        'full_code': cpc_code_mapping.get(level4_code, ''),
        'best_month': data['month'],
        'best_month_count': data['count'],
        'ema': data['ema']
    })

result_data = {
    'cpc_groups': final_cpc_groups
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
