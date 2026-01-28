code = """import json
import re
from datetime import datetime

# Read the query results file
data_file = var_functions.query_db:2
with open(data_file, 'r') as f:
    all_grants = json.load(f)

# Filter for second half of 2019 (July-December) and German patents
second_half_grants = []

for record in all_grants:
    grant_date = record.get('grant_date', '')
    patents_info = record.get('Patents_info', '')
    cpc_data = record.get('cpc', '')
    
    # Check if it's a German patent
    if 'DE-' not in patents_info and 'Germany' not in patents_info:
        continue
    
    # Parse grant date - extract month and year
    if '2019' not in grant_date:
        continue
    
    # Try to extract month from various date formats
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
    if not month_match:
        # Try numeric format
        numeric_match = re.search(r'(\d{1,2})[^\d]+2019', grant_date)
        if numeric_match:
            month = int(numeric_match.group(1))
        else:
            continue
    else:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month = month_map.get(month_name, 0)
    
    # Check if month is in second half (July-December)
    if month < 7 or month > 12:
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
                'grant_date': grant_date,
                'month': month,
                'cpc_code': code,
                'patents_info': patents_info
            })

print(f"Found {len(second_half_grants)} German patent grants in second half 2019 with CPC codes")

# Group by CPC codes and count
from collections import defaultdict

# Extract level 4 CPC groups (format: Section-Class-Subclass-Group)
# CPC codes look like: G06F9/45533, A61D1/00, etc.
# Level 4 would be the group level (first 4 characters after the section)
cpc_counts = defaultdict(lambda: defaultdict(int))  # cpc_code -> month -> count

cpc_code_mapping = {}  # Store the full code for each level 4 group

for grant in second_half_grants:
    full_code = grant['cpc_code']
    month = grant['month']
    
    # Extract level 4 group
    # Format: G06F9/45533 -> G06F9 is level 4
    level4_match = re.match(r'^([A-Z]\d{2}[A-Z]\d)', full_code)
    if level4_match:
        level4_code = level4_match.group(1)
        cpc_code_mapping[level4_code] = full_code
        cpc_counts[level4_code][month] += 1

print(f"Found {len(cpc_counts)} unique level 4 CPC groups")

# Calculate exponential moving average for each CPC group
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
# Where α = 0.1 (smoothing factor)

alpha = 0.1
ema_results = []

for level4_code, monthly_counts in cpc_counts.items():
    # Sort months chronologically
    months = sorted(monthly_counts.items())
    
    # Initialize EMA
    ema = None
    
    for month, count in months:
        if ema is None:
            ema = count  # First value
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        ema_results.append({
            'cpc_level4_code': level4_code,
            'month': month,
            'count': count,
            'ema': ema
        })

# Find the best month (highest EMA) for each CPC group
best_months = {}
for result in ema_results:
    code = result['cpc_level4_code']
    if code not in best_months or result['ema'] > best_months[code]['ema']:
        best_months[code] = {
            'month': result['month'],
            'count': result['count'],
            'ema': result['ema']
        }

print(f"Calculated EMA for {len(best_months)} CPC groups")

# Prepare data for CPC definition lookup
cpc_groups_for_query = list(best_months.keys())

# Print results in required format
result_data = {
    'cpc_groups': cpc_groups_for_query,
    'best_months': best_months,
    'code_mapping': cpc_code_mapping
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
