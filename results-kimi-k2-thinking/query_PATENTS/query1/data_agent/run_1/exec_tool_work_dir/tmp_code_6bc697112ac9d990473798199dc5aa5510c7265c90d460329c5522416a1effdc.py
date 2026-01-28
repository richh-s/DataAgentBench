code = """import json, re
from collections import defaultdict

# Read the publication data file
pub_data_file = var_functions.query_db_6
with open(pub_data_file, 'r') as f:
    publications = json.load(f)

# Read the CPC level definitions file
cpc_def_file = var_functions.query_db_5
with open(cpc_def_file, 'r') as f:
    cpc_level_info = json.load(f)

# Extract CPC codes at level 5
cpc_level5_symbols = set(item['symbol'] for item in cpc_level_info)

# Parse and count CPC codes by year
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    # Extract year from publication date
    date_match = re.search(r'(\d{4})', pub['publication_date'])
    if not date_match:
        continue
    year = int(date_match.group(1))
    
    # Parse CPC codes
    cpc_str = pub['cpc']
    if not cpc_str or not cpc_str.strip():
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            full_code = cpc_entry['code']
            # Extract group code (level 5) by taking everything before the first /
            group_code = full_code.split('/')[0]
            # Only track codes that are at level 5
            if group_code in cpc_level5_symbols:
                cpc_yearly_counts[group_code][year] += 1
    except:
        continue

# Calculate EMA for each CPC code
ema_results = {}
smoothing_factor = 0.2

for cpc_code, yearly_counts in cpc_yearly_counts.items():
    # Need at least 2 years of data
    if len(yearly_counts) < 2:
        continue
    
    # Sort years chronologically
    sorted_years = sorted(yearly_counts.keys())
    ema_data = {}
    prev_ema = None
    
    for year in sorted_years:
        count = yearly_counts[year]
        if prev_ema is None:
            ema = count
        else:
            ema = (count * smoothing_factor) + (prev_ema * (1 - smoothing_factor))
        ema_data[year] = ema
        prev_ema = ema
    
    # Find year with highest EMA
    best_year = max(ema_data, key=ema_data.get)
    
    ema_results[cpc_code] = {
        'best_year': best_year,
        'yearly_ema': ema_data
    }

# Filter for CPC codes whose best year (with highest EMA) is 2022
cpc_best_2022 = sorted([code for code, data in ema_results.items() if data['best_year'] == 2022])

# Result JSON
result = json.dumps(cpc_best_2022)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'B21L', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A47F', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}, {'symbol': 'A45D', 'level': '5.0'}, {'symbol': 'A45B', 'level': '5.0'}, {'symbol': 'A46D', 'level': '5.0'}, {'symbol': 'A46B', 'level': '5.0'}, {'symbol': 'A47L', 'level': '5.0'}, {'symbol': 'B22C', 'level': '5.0'}, {'symbol': 'A47D', 'level': '5.0'}, {'symbol': 'A47G', 'level': '5.0'}, {'symbol': 'A47K', 'level': '5.0'}, {'symbol': 'A47H', 'level': '5.0'}, {'symbol': 'A47B', 'level': '5.0'}, {'symbol': 'A47C', 'level': '5.0'}, {'symbol': 'A47J', 'level': '5.0'}, {'symbol': 'A61M', 'level': '5.0'}, {'symbol': 'A61K', 'level': '5.0'}, {'symbol': 'A61B', 'level': '5.0'}, {'symbol': 'A61C', 'level': '5.0'}, {'symbol': 'A61F', 'level': '5.0'}, {'symbol': 'A61L', 'level': '5.0'}, {'symbol': 'A61J', 'level': '5.0'}, {'symbol': 'A61G', 'level': '5.0'}, {'symbol': 'A61Q', 'level': '5.0'}, {'symbol': 'A61P', 'level': '5.0'}, {'symbol': 'B60V', 'level': '5.0'}, {'symbol': 'A61H', 'level': '5.0'}, {'symbol': 'A61D', 'level': '5.0'}, {'symbol': 'A61N', 'level': '5.0'}, {'symbol': 'A62C', 'level': '5.0'}, {'symbol': 'A62D', 'level': '5.0'}, {'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}, {'symbol': 'B02B', 'level': '5.0'}, {'symbol': 'B03B', 'level': '5.0'}, {'symbol': 'B03D', 'level': '5.0'}, {'symbol': 'B03C', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
