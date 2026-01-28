code = """import json
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Read the result from the file
file_path = locals()['var_functions.query_db:10']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        records = json.load(f)
else:
    records = locals()['var_functions.query_db:10']

# Function to extract year from publication_date

def extract_year(date_str):
    try:
        # Match pattern like "Aug 3rd, 2021", "Oct 6th, 2020", etc.
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group())
        return None
    except:
        return None

# Function to parse CPC codes and extract level 5 codes

def parse_cpc_level5(cpc_json_str):
    level5_codes = set()
    try:
        cpc_list = json.loads(cpc_json_str)
        for item in cpc_list:
            code = item.get('code', '')
            # Split by / and take the first part
            main_code = code.split('/')[0]
            # Count levels: Main groups (level 3) are like A01C
            # Level 5 should be like A01C, A01G (main groups)
            if len(main_code) == 4:  # Like A01C, A01G
                level5_codes.add(main_code)
    except:
        # Fallback for malformed JSON
        try:
            import ast
            cpc_list = ast.literal_eval(cpc_json_str)
            for item in cpc_list:
                code = item.get('code', '')
                main_code = code.split('/')[0]
                if len(main_code) == 4:
                    level5_codes.add(main_code)
        except:
            pass
    return list(level5_codes)

# Process records and extract data
cpc_yearly_counts = {}
years_available = set()

for record in records:
    # Parse CPC codes
    if record.get('cpc'):
        cpc_codes = parse_cpc_level5(record['cpc'])
    else:
        continue
    
    # Extract year from publication_date
    year = extract_year(record.get('publication_date', ''))
    if year:
        years_available.add(year)
        for cpc in cpc_codes:
            if cpc not in cpc_yearly_counts:
                cpc_yearly_counts[cpc] = {}
            cpc_yearly_counts[cpc][year] = cpc_yearly_counts[cpc].get(year, 0) + 1

# Find min and max years
min_year = min(years_available)
max_year = max(years_available)

# Create a comprehensive count for all years (0 for missing years)
all_years = range(min_year, max_year + 1)
cpc_full_counts = {}

for cpc in cpc_yearly_counts:
    cpc_full_counts[cpc] = {year: cpc_yearly_counts[cpc].get(year, 0) for year in all_years}

# Calculate EMA for each CPC code (smoothing factor alpha = 0.2)
def calculate_ema(counts_dict, alpha=0.2):
    # Sort by year
    sorted_years = sorted(counts_dict.keys())
    if not sorted_years:
        return {}
    
    # Initialize EMA
    ema_values = {}
    ema_prev = 0
    
    for year in sorted_years:
        current_value = counts_dict[year]
        ema_current = alpha * current_value + (1 - alpha) * ema_prev
        ema_values[year] = ema_current
        ema_prev = ema_current
    
    return ema_values

# Calculate EMAs and find best year for each CPC
cpc_best_years = {}
cpc_ema_values = {}

for cpc in cpc_full_counts:
    ema_vals = calculate_ema(cpc_full_counts[cpc], alpha=0.2)
    cpc_ema_values[cpc] = ema_vals
    
    # Find year with highest EMA
    best_year = max(ema_vals.items(), key=lambda x: x[1])[0]
    cpc_best_years[cpc] = {
        'best_year': best_year,
        'best_ema': ema_vals[best_year]
    }

# Filter CPC codes with best year 2022
cpc_best_2022 = [cpc for cpc, data in cpc_best_years.items() if data['best_year'] == 2022]

# Get rankings (optional) - sort by EMA value in 2022
if 2022 in all_years:
    cpc_2022_ranks = []
    for cpc in cpc_best_2022:
        if 2022 in cpc_ema_values[cpc]:
            cpc_2022_ranks.append((cpc, cpc_ema_values[cpc][2022]))
    cpc_2022_ranks.sort(key=lambda x: x[1], reverse=True)
    result_codes = [item[0] for item in cpc_2022_ranks]
else:
    result_codes = cpc_best_2022

print('__RESULT__:')
print(json.dumps({
    'total_cpc_codes': len(cpc_yearly_counts),
    'years_range': f'{min_year} to {max_year}',
    'cpc_codes_best_2022': result_codes,
    'count_2022': len(result_codes)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
