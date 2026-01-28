code = """import json
import pandas as pd
import re

# Load publication data if from file or direct
patents_info_key = 'var_functions.query_db:2'
patents_data = []
if isinstance(globals().get(patents_info_key), str):
    with open(globals()[patents_info_key], 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = globals().get(patents_info_key, [])

# Load CPC definitions if from file or direct
cpc_key = 'var_functions.query_db:12'
cpc_data = []
if isinstance(globals().get(cpc_key), str):
    with open(globals()[cpc_key], 'r') as f:
        cpc_data = json.load(f)
else:
    cpc_data = globals().get(cpc_key, [])

print(f'Loaded {len(patents_data)} patents and {len(cpc_data)} CPC definitions')

# Create CPC lookup dict for level 4 groups
cpc_level4_lookup = {}
for cpc_def in cpc_data:
    symbol = cpc_def.get('symbol', '')
    level = cpc_def.get('level')
    if level and symbol:
        try:
            level_num = float(level)
            if level_num == 4.0 and len(symbol) == 3:
                cpc_level4_lookup[symbol] = cpc_def.get('titleFull', '')
        except:
            pass

print(f'Found {len(cpc_level4_lookup)} level 4 CPC groups')

# Filter Germany patents granted in second half of 2019
germany_2019_patents = []

month_map = {
    'jan': 1, 'january': 1,
    'feb': 2, 'february': 2,
    'mar': 3, 'march': 3,
    'apr': 4, 'april': 4,
    'may': 5,
    'jun': 6, 'june': 6,
    'jul': 7, 'july': 7,
    'aug': 8, 'august': 8,
    'sep': 9, 'september': 9,
    'oct': 10, 'october': 10,
    'nov': 11, 'november': 11,
    'dec': 12, 'december': 12
}

for patent in patents_data:
    if not patent:
        continue
    
    # Check if Germany patent
    patents_info = patent.get('Patents_info', '')
    if not patents_info or 'DE-' not in str(patents_info):
        continue
    
    # Check grant date in second half of 2019
    grant_date = patent.get('grant_date', '')
    if not grant_date or '2019' not in str(grant_date):
        continue
    
    grant_str = str(grant_date).lower()
    month_num = None
    for month_name, num in month_map.items():
        if month_name in grant_str:
            month_num = num
            break
    
    if month_num is None or month_num < 7:
        continue
    
    # Extract CPC codes at level 4  
    cpc_str = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str
        if isinstance(cpc_list, list):
            level4_codes = set()
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and len(code) >= 3:
                    # Extract group at level 4 (first 3 characters)
                    group_code = code[:3]
                    if group_code in cpc_level4_lookup:
                        level4_codes.add(group_code)
            
            if level4_codes:
                germany_2019_patents.append({
                    'grant_month': month_num,
                    'cpc_groups': list(level4_codes)
                })
    except:
        continue

print(f'Filtered to {len(germany_2019_patents)} Germany patents with valid CPC groups')

# Count patents per CPC group per month
cpc_month_counts = {}
for patent in germany_2019_patents:
    month = patent['grant_month']
    for group in patent['cpc_groups']:
        if group not in cpc_month_counts:
            cpc_month_counts[group] = {}
        cpc_month_counts[group][month] = cpc_month_counts[group].get(month, 0) + 1

# Calculate EMA (smoothing factor 0.1) for each CPC group
# Formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
alpha = 0.1
results = []

for group, monthly_counts in cpc_month_counts.items():
    # Create ordered months (7-12)
    values = []
    for month in range(7, 13):
        values.append(monthly_counts.get(month, 0))
    
    # Calculate EMA
    ema_values = []
    ema_prev = 0  # Initial value
    
    for value in values:
        ema = alpha * value + (1 - alpha) * ema_prev
        ema_values.append(ema)
        ema_prev = ema
    
    # Find best month (highest EMA) - 0-indexed position + 7
    max_ema = max(ema_values)
    best_month_idx = ema_values.index(max_ema)
    best_month = best_month_idx + 7
    
    title_full = cpc_level4_lookup.get(group, '')
    
    results.append({
        'cpc_group': group,
        'title_full': title_full,
        'best_month': best_month,
        'max_ema': max_ema,
        'total_patents': sum(values),
        'monthly_counts': values,
        'ema_values': ema_values
    })

# Sort by EMA descending
results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)

print(f'Processed {len(results_sorted)} CPC groups')

# Return top results with details
output_results = []
for i, result in enumerate(results_sorted[:20]):
    output_results.append({
        'rank': i + 1,
        'cpc_group': result['cpc_group'],
        'title_full': result['title_full'],
        'best_month_2019': result['best_month'],
        'ema_value': round(result['max_ema'], 2),
        'total_patents_second_half_2019': result['total_patents']
    })

print('__RESULT__:')
print(json.dumps(output_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'total_germany_2019_second_half': 313, 'months_with_data': [11, 12, 8, 9, 10, 7]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
