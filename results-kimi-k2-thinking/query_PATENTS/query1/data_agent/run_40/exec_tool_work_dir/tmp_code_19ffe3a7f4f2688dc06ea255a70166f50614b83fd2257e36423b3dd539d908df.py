code = """import json
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Read the patent data from the full dataset
file_path = locals()['var_functions.query_db:20']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patent_records = json.load(f)
else:
    patent_records = locals()['var_functions.query_db:20']

# Function to extract year from publication_date
def extract_year(date_str):
    try:
        if not date_str:
            return None
        match = re.search(r'\d{4}', str(date_str))
        if match:
            return int(match.group())
        return None
    except:
        return None

# Function to extract level 5 CPC codes from the JSON string
# Level 5 codes are typically the first 4-6 characters of the main group
# For G06Q10/06313, the level 5 would be G06Q10
# For A01C1/00, the level 5 would be A01C

def extract_level5_cpc(cpc_json_str):
    if not cpc_json_str or pd.isna(cpc_json_str):
        return []
    
    level5_codes = set()
    try:
        cpc_list = json.loads(cpc_json_str)
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                if code and isinstance(code, str):
                    # Remove Y-codes and other metadata codes
                    if code.startswith('Y') or 'B01F' in code or 'B28' in code:
                        continue
                    
                    # Extract level 5: part before /, truncated to meaningful length
                    if '/' in code:
                        main_group = code.split('/')[0]
                        # For level 5, use the main group identifier (4-7 chars typically)
                        # This could be like A01C, G06Q10, H01M4, etc.
                        if len(main_group) >= 4:
                            level5_codes.add(main_group)
                    else:
                        # If no subgroup, use the code itself if it's long enough
                        if len(code) >= 4:
                            level5_codes.add(code)
    except:
        # Fallback parsing
        try:
            import ast
            cpc_list = ast.literal_eval(cpc_json_str)
            for item in cpc_list:
                if isinstance(item, dict) and 'code' in item:
                    code = item['code']
                    if code and isinstance(code, str):
                        if code.startswith('Y'):
                            continue
                        if '/' in code:
                            main_group = code.split('/')[0]
                            if len(main_group) >= 4:
                                level5_codes.add(main_group)
                        else:
                            if len(code) >= 4:
                                level5_codes.add(code)
        except:
            pass
    
    return list(level5_codes)

# Process all patent records
cpc_yearly_counts = {}
year_range = set()
processed = 0

for record in patent_records:
    year = extract_year(record.get('publication_date', ''))
    if not year:
        continue
    
    cpc_codes = extract_level5_cpc(record.get('cpc', ''))
    if not cpc_codes:
        continue
    
    year_range.add(year)
    for cpc in cpc_codes:
        if cpc not in cpc_yearly_counts:
            cpc_yearly_counts[cpc] = {}
        cpc_yearly_counts[cpc][year] = cpc_yearly_counts[cpc].get(year, 0) + 1
    
    processed += 1
    if processed % 50000 == 0:
        print(f"Processed {processed} records...")

# Determine year range
min_year = min(year_range)
max_year = max(year_range)
all_years = list(range(min_year, max_year + 1))

# Fill in missing years with 0 counts
for cpc in cpc_yearly_counts:
    for year in all_years:
        if year not in cpc_yearly_counts[cpc]:
            cpc_yearly_counts[cpc][year] = 0

# Calculate Exponential Moving Average for each CPC code
def calculate_ema(yearly_counts, alpha=0.2):
    # Sort by year
    sorted_years = sorted(yearly_counts.keys())
    if not sorted_years:
        return {}
    
    ema_values = {}
    ema_prev = 0  # Initial value
    
    for year in sorted_years:
        current_value = yearly_counts[year]
        ema_current = alpha * current_value + (1 - alpha) * ema_prev
        ema_values[year] = ema_current
        ema_prev = ema_current
    
    return ema_values

# Calculate EMAs and find best year for each CPC
cpc_best_years = {}
cpc_ema_data = {}

for cpc, yearly_counts in cpc_yearly_counts.items():
    ema_values = calculate_ema(yearly_counts, alpha=0.2)
    cpc_ema_data[cpc] = ema_values
    
    if ema_values:
        best_year = max(ema_values.items(), key=lambda x: x[1])[0]
        best_ema = ema_values[best_year]
        cpc_best_years[cpc] = {
            'best_year': best_year,
            'best_ema': best_ema
        }

# Filter CPC codes where best year is 2022
cpc_best_2022 = []
for cpc, data in cpc_best_years.items():
    if data['best_year'] == 2022:
        # Also have some minimum threshold to avoid noise
        if data['best_ema'] > 0.1:  # At least some meaningful activity
            cpc_best_2022.append((cpc, data['best_ema']))

# Sort by EMA value descending
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)

# Get top results
result_codes = [item[0] for item in cpc_best_2022]

print(f'Found {len(result_codes)} CPC codes with best year 2022')
print('Top codes:', result_codes[:20])

print('__RESULT__:')
print(json.dumps({
    'years_range': f'{min_year} to {max_year}',
    'total_cpc_codes': len(cpc_yearly_counts),
    'cpc_best_2022': result_codes,
    'count': len(result_codes),
    'sample_details': result_codes[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_cpc_codes': 0, 'years_range': '1971 to 2024', 'cpc_codes_best_2022': [], 'count_2022': 0}, 'var_functions.query_db:14': [{'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Loaded 1000 records for analysis', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'Ready to process full dataset', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_count': 677, 'patent_records_count': 277813, 'sample_level5': ['B67D', 'D10B', 'C05B', 'H04S', 'G02F', 'B64C', 'B61C', 'F21Y', 'B65G', 'B29L']}}

exec(code, env_args)
