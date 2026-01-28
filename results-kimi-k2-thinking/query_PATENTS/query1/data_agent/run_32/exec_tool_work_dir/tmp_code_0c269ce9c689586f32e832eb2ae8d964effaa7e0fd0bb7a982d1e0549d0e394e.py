code = """import json, re
from collections import defaultdict

patent_file = globals()['var_functions.query_db:36']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

print('Processing {} records'.format(len(patent_data)))

# Count patent filings per CPC code per year
year_pattern = re.compile(r'(20\d{2})')

cpc_year_counts = defaultdict(lambda: defaultdict(int))
level5_mapping = defaultdict(set)
valid_records = 0

for record in patent_data:
    try:
        cpc_str = record.get('cpc', '')
        if not cpc_str or cpc_str == 'null':
            continue
        
        cpc_list = json.loads(cpc_str)
        pub_date = record.get('publication_date', '')
        
        # Extract year
        year_match = year_pattern.search(str(pub_date))
        if not year_match:
            continue
        
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:
            continue
        
        # Process each CPC code
        for cpc_item in cpc_list:
            full_code = cpc_item.get('code', '')
            if full_code and '/' in full_code:
                valid_records += 1
                cpc_year_counts[full_code][year] += 1
                
                # Extract level 5 group
                group = full_code.split('/')[0]
                if len(group) >= 4:
                    level5 = group[:4]
                    if re.match(r'^[A-Z]\d{2}[A-Z]$', level5):
                        level5_mapping[level5].add(full_code)
                        
    except:
        continue

print('Valid records: {}, Full CPC codes: {}, Level 5 groups: {}'.format(
    valid_records, len(cpc_year_counts), len(level5_mapping)))

# Calculate EMA for each level 5 group
alpha = 0.2
level5_ema = {}
years = range(2000, 2024)  # Up to 2023

for level5, full_codes in level5_mapping.items():
    # Aggregate counts for all full codes in this level 5 group
    group_yearly_counts = defaultdict(int)
    for full_code in full_codes:
        for year, count in cpc_year_counts[full_code].items():
            group_yearly_counts[year] += count
    
    # Calculate EMA
    ema_values = {}
    ema_prev = None
    for year in sorted(years):
        current_value = group_yearly_counts.get(year, 0)
        if ema_prev is None:
            ema_prev = current_value
        else:
            ema_prev = alpha * current_value + (1 - alpha) * ema_prev
        ema_values[year] = ema_prev
    
    level5_ema[level5] = ema_values

print('Calculated EMA for {} level 5 groups'.format(len(level5_ema)))

# Find best year for each level 5 group
best_years = {}
for level5, ema_values in level5_ema.items():
    if ema_values:
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        best_years[level5] = best_year

print('Found best years for {} groups'.format(len(best_years)))

# Filter groups with best year = 2022
level5_best_2022 = [level5 for level5, year in best_years.items() if year == 2022]

print('Groups with best year 2022: {}'.format(len(level5_best_2022)))
print('Sample results: {}'.format(level5_best_2022[:10]))

output = {
    'level5_best_2022': level5_best_2022,
    'count': len(level5_best_2022),
    'sample_codes': level5_best_2022[:10]
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'cpc_year_counts': {}, 'cpc_level5_to_full': {}, 'total_records': 277813}, 'var_functions.execute_python:46': {'records_checked': 1000, 'cpc_parse_success': 1000, 'year_match_success': 0, 'level5_patterns': 11181}}

exec(code, env_args)
