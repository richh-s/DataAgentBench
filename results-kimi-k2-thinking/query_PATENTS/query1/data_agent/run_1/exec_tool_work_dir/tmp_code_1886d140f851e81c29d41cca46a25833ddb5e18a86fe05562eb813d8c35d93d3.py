code = """import json
import re
from collections import defaultdict
import pandas as pd

# Load the full results file
result_path = var_functions.query_db:6
with open(result_path, 'r') as f:
    publications = json.load(f)

# Parse CPC codes and extract year from publication dates
year_regex = r'(\d{4})'
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_all_codes = {}

for pub in publications:
    # Parse publication year
    date_match = re.search(year_regex, pub['publication_date'])
    if date_match:
        year = int(date_match.group(1))
    else:
        continue
    
    # Parse CPC JSON
    cpc_str = pub['cpc']
    if cpc_str and cpc_str.strip():
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_entry in cpc_list:
                # Remove subgroups to get level 5 group codes (e.g., G01N29/02 becomes G01N29/02, G01N29 becomes G01N29)
                full_code = cpc_entry['code']
                # Group code (level 5) - extract up to first / character
                group_code = full_code.split('/')[0]
                cpc_yearly_counts[group_code][year] += 1
                if group_code not in cpc_all_codes:
                    cpc_all_codes[group_code] = []
                cpc_all_codes[group_code].append(full_code)
        except:
            continue

# Get list of CPC codes and years
all_years = sorted(set(year for cpc_dict in cpc_yearly_counts.values() for year in cpc_dict.keys()))
all_cpc_codes = list(cpc_yearly_counts.keys())

# Calculate EMA for each CPC code
ema_results = {}
smoothing_factor = 0.2

for cpc_code in all_cpc_codes:
    yearly_counts = cpc_yearly_counts[cpc_code]
    
    # Create sorted list of all years with counts (0 for missing years)
    sorted_years = sorted(yearly_counts.keys())
    if len(sorted_years) < 2:
        continue
    
    # Initialize EMA calculation
    ema_data = {}
    prev_ema = None
    
    for year in sorted_years:
        count = yearly_counts[year]
        if prev_ema is None:
            # First EMA is just the first value
            ema = count
        else:
            # EMA = (current_value * smoothing) + (previous_ema * (1 - smoothing))
            ema = (count * smoothing_factor) + (prev_ema * (1 - smoothing_factor))
        
        ema_data[year] = ema
        prev_ema = ema
    
    # Find year with highest EMA
    best_year = max(ema_data, key=ema_data.get)
    max_ema = ema_data[best_year]
    
    ema_results[cpc_code] = {
        'best_year': best_year,
        'max_ema': max_ema,
        'yearly_ema': ema_data,
        'total_appearances': sum(yearly_counts.values())
    }

# Filter for CPC codes with best year = 2022
cpc_best_2022 = {code: data for code, data in ema_results.items() if data['best_year'] == 2022}

# Load CPC level information
cpc_def_path = var_functions.query_db:5
with open(cpc_def_path, 'r') as f:
    cpc_level_info = json.load(f)

cpc_level5_symbols = set(item['symbol'] for item in cpc_level_info)

# Filter CPC codes to only level 5 codes
cpc_level5_best_2022 = {code: data for code, data in cpc_best_2022.items() if code in cpc_level5_symbols}

# Print results in required format
result_json = json.dumps({
    'total_cpc_codes': len(all_cpc_codes),
    'codes_with_data': len(ema_results),
    'best_in_2022': len(cpc_best_2022),
    'level5_best_in_2022': len(cpc_level5_best_2022),
    'level5_codes': sorted(list(cpc_level5_best_2022.keys()))
})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'B21L', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A47F', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}, {'symbol': 'A45D', 'level': '5.0'}, {'symbol': 'A45B', 'level': '5.0'}, {'symbol': 'A46D', 'level': '5.0'}, {'symbol': 'A46B', 'level': '5.0'}, {'symbol': 'A47L', 'level': '5.0'}, {'symbol': 'B22C', 'level': '5.0'}, {'symbol': 'A47D', 'level': '5.0'}, {'symbol': 'A47G', 'level': '5.0'}, {'symbol': 'A47K', 'level': '5.0'}, {'symbol': 'A47H', 'level': '5.0'}, {'symbol': 'A47B', 'level': '5.0'}, {'symbol': 'A47C', 'level': '5.0'}, {'symbol': 'A47J', 'level': '5.0'}, {'symbol': 'A61M', 'level': '5.0'}, {'symbol': 'A61K', 'level': '5.0'}, {'symbol': 'A61B', 'level': '5.0'}, {'symbol': 'A61C', 'level': '5.0'}, {'symbol': 'A61F', 'level': '5.0'}, {'symbol': 'A61L', 'level': '5.0'}, {'symbol': 'A61J', 'level': '5.0'}, {'symbol': 'A61G', 'level': '5.0'}, {'symbol': 'A61Q', 'level': '5.0'}, {'symbol': 'A61P', 'level': '5.0'}, {'symbol': 'B60V', 'level': '5.0'}, {'symbol': 'A61H', 'level': '5.0'}, {'symbol': 'A61D', 'level': '5.0'}, {'symbol': 'A61N', 'level': '5.0'}, {'symbol': 'A62C', 'level': '5.0'}, {'symbol': 'A62D', 'level': '5.0'}, {'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}, {'symbol': 'B02B', 'level': '5.0'}, {'symbol': 'B03B', 'level': '5.0'}, {'symbol': 'B03D', 'level': '5.0'}, {'symbol': 'B03C', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
