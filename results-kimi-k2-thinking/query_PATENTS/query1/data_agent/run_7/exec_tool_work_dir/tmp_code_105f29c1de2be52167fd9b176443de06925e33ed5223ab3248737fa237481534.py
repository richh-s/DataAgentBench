code = """import json
import ast
from collections import Counter

file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    records = json.load(f)

patent_data = []
years_found = set()

for record in records:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '[]')
    
    # Parse publication year
    year = None
    if pub_date:
        try:
            parts = pub_date.split(', ')
            if len(parts) >= 2:
                year = int(parts[1])
                years_found.add(year)
        except:
            pass
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_data)
    except:
        try:
            cpc_list = ast.literal_eval(cpc_data)
        except:
            cpc_list = []
    
    # Extract CPC codes
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code and year:
            patent_data.append({'cpc_code': code, 'year': year})

# Get CPC codes at level 5 (e.g., A01B01/00, C01B33/00, H01M10/0525)
# Level 5 in CPC hierarchy is the subgroup level with format like C01B33/00 or H01M10/0565
# The part before / indicates the group/subgroup position

# Build yearly filing counts for each CPC code
cpc_yearly_counts = {}
for entry in patent_data:
    cpc = entry['cpc_code']
    year = entry['year']
    if cpc not in cpc_yearly_counts:
        cpc_yearly_counts[cpc] = {}
    cpc_yearly_counts[cpc][year] = cpc_yearly_counts[cpc].get(year, 0) + 1

# Calculate Exponential Moving Average (EMA) for each CPC code
# EMA formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
alpha = 0.2
years = sorted(years_found)

cpc_ema_data = {}
for cpc, yearly_counts in cpc_yearly_counts.items():
    ema_values = {}
    ema_prev = 0
    for year in years:
        value = yearly_counts.get(year, 0)
        ema_current = alpha * value + (1 - alpha) * ema_prev
        ema_values[year] = ema_current
        ema_prev = ema_current
    cpc_ema_data[cpc] = ema_values

# Find the best year for each CPC code (year with highest EMA)
cpc_best_year = {}
for cpc, ema_values in cpc_ema_data.items():
    best_year = max(ema_values.items(), key=lambda x: x[1])[0]
    cpc_best_year[cpc] = best_year

# Filter CPC codes whose best year is 2022 and are at level 5
cycl_codes_level5 = []
for cpc, best_year in cpc_best_year.items():
    if best_year == 2022:
        # Check if it's at level 5
        # CPC level 5 has pattern like: C01B33/00 (group), H01M10/0565 (subgroup)
        # Both have structure: [Section][Class][Subclass][MainGroup]/[Subgroup]
        # We want codes that have a main group and subgroup structure
        if '/' in cpc:
            parts = cpc.split('/')
            main_group_part = parts[0]
            subgroup_part = parts[1]
            # Level 5 should have digits in the main group part
            # and the subgroup part can be digits or empty
            if any(c.isdigit() for c in main_group_part):
                cycl_codes_level5.append(cpc)

print('__RESULT__:')
result = {
    'total_cpc_codes': len(cpc_best_year),
    'cpc_best_year_2022_count': len([c for c,y in cpc_best_year.items() if y == 2022]),
    'level5_cpc_best_year_2022_count': len(cycl_codes_level5),
    'sample_level5_cpc_2022': cycl_codes_level5[:10]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
