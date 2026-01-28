code = """import json

# Access the file path from storage
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    records = json.load(f)

# Process records to extract CPC codes and years
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
            cpc_list = __import__('ast').literal_eval(cpc_data)
        except:
            cpc_list = []
    
    # Extract CPC codes
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code and year:
            patent_data.append({'cpc_code': code, 'year': year})

# Build yearly filing counts for each CPC code
cpc_yearly_counts = {}
for entry in patent_data:
    cpc = entry['cpc_code']
    year = entry['year']
    if cpc not in cpc_yearly_counts:
        cpc_yearly_counts[cpc] = {}
    cpc_yearly_counts[cpc][year] = cpc_yearly_counts[cpc].get(year, 0) + 1

# Calculate Exponential Moving Average (EMA) for each CPC code
alpha = 0.2
years = sorted(years_found)

# EMA formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
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

# Filter CPC codes whose best year is 2022 and are at exactly level 5
# CPC Level 5: Pattern [Section][Class][Subclass][MainGroup]/[Subgroup]
# Examples: A01B01/00 (level 5), H01M10/0565 (level 5)
# We need to exclude codes with additional digits beyond the standard level 5 format

level5_cpc_2022 = []
for cpc, best_year in cpc_best_year.items():
    if best_year == 2022:
        if '/' in cpc:
            parts = cpc.split('/')
            main_group = parts[0]
            subgroup = parts[1] if len(parts) > 1 else ''
            
            # Check if it's at level 5 (group level)
            # Level 5 has:
            # - Non-empty main group with mixed letters and digits
            # - Subgroup is typically 2-4 digits (possibly with leading zeros)
            main_group_has_letters = any(c.isalpha() for c in main_group)
            main_group_has_digits = any(c.isdigit() for c in main_group)
            subgroup_is_valid = len(subgroup) >= 2 and len(subgroup) <= 4 and subgroup.isdigit()
            
            if main_group_has_letters and main_group_has_digits and subgroup_is_valid:
                level5_cpc_2022.append(cpc)

# Return the filtered list of CPC codes
print('__RESULT__:')
print(json.dumps(level5_cpc_2022))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_cpc_codes': 143452, 'cpc_best_year_2022_count': 12036, 'level5_cpc_best_year_2022_count': 12036, 'sample_level5_cpc_2022': ['C01P2002/76', 'H01M10/0525', 'F16H2200/2007', 'F16H2200/2041', 'B29C70/48', 'C09D175/08', 'B32B27/34', 'B32B2260/021', 'B32B2307/50', 'B32B27/302']}}

exec(code, env_args)
