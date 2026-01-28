code = """import json
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Read the full patent data
file_path = locals()['var_functions.query_db:20']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patent_records = json.load(f)
else:
    patent_records = locals()['var_functions.query_db:20']

# Read the CPC level 5 definitions
file_path2 = locals()['var_functions.query_db:24']
if isinstance(file_path2, str) and file_path2.endswith('.json'):
    with open(file_path2, 'r') as f:
        cpc_level5_defs = json.load(f)
else:
    cpc_level5_defs = locals()['var_functions.query_db:24']

# Create set of valid level 5 symbols
level5_symbols = set([item['symbol'] for item in cpc_level5_defs])
print(f'Loaded {len(patent_records)} patent records')
print(f'Loaded {len(level5_symbols)} level 5 CPC symbols')

# Function to extract year
def extract_year(date_str):
    if not date_str or pd.isna(date_str):
        return None
    match = re.search(r'\d{4}', str(date_str))
    return int(match.group()) if match else None

# Function to extract level 5 CPC codes
def extract_cpc_level5(cpc_json_str):
    if not cpc_json_str or pd.isna(cpc_json_str) or str(cpc_json_str) == '[]':
        return []
    
    level5_codes = set()
    try:
        cpc_list = json.loads(cpc_json_str) if isinstance(cpc_json_str, str) else cpc_json_str
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                if code and isinstance(code, str) and not code.startswith('Y'):
                    # Get main group before /
                    main_group = code.split('/')[0] if '/' in code else code
                    # Find matching level 5 symbol by progressive shortening
                    test_code = main_group
                    while len(test_code) >= 3:
                        if test_code in level5_symbols:
                            level5_codes.add(test_code)
                            break
                        test_code = test_code[:-1]
    except:
        # Fallback for malformed JSON
        try:
            import ast
            cpc_list = ast.literal_eval(str(cpc_json_str))
            for item in cpc_list:
                if isinstance(item, dict) and 'code' in item:
                    code = item['code']
                    if code and isinstance(code, str) and not code.startswith('Y'):
                        main_group = code.split('/')[0] if '/' in code else code
                        test_code = main_group
                        while len(test_code) >= 3:
                            if test_code in level5_symbols:
                                level5_codes.add(test_code)
                                break
                            test_code = test_code[:-1]
        except:
            # Regex fallback
            codes = re.findall(r'"code"\s*:\s*"([^"]+)"', str(cpc_json_str))
            for code in codes:
                if not code.startswith('Y'):
                    main_group = code.split('/')[0] if '/' in code else code
                    test_code = main_group
                    while len(test_code) >= 3:
                        if test_code in level5_symbols:
                            level5_codes.add(test_code)
                            break
                        test_code = test_code[:-1]
    
    return list(level5_codes)

# Process all records
print('Processing patent records...')
cpc_yearly_counts = {}
years_observed = set()
processed = 0
valid_records = 0

for record in patent_records:
    year = extract_year(record.get('publication_date', ''))
    if not year:
        continue
    
    cpc_codes = extract_cpc_level5(record.get('cpc', ''))
    if not cpc_codes:
        continue
    
    years_observed.add(year)
    valid_records += 1
    
    for cpc in cpc_codes:
        if cpc not in cpc_yearly_counts:
            cpc_yearly_counts[cpc] = {}
        cpc_yearly_counts[cpc][year] = cpc_yearly_counts[cpc].get(year, 0) + 1
    
    processed += 1
    if processed % 50000 == 0:
        print(f'  Processed {processed} records...')

print(f'Completed processing {processed} records')
print(f'Valid records with CPC/year: {valid_records}')
print(f'Year range: {min(years_observed)} to {max(years_observed)}')
print(f'Sample CPC codes: {list(cpc_yearly_counts.keys())[:10]}')
print(f'Total unique CPC codes: {len(cpc_yearly_counts)}')

# Calculate Exponential Moving Average
def calculate_ema(yearly_counts, alpha=0.2):
    sorted_years = sorted(yearly_counts.keys())
    if not sorted_years:
        return {}
    
    ema_values = {}
    ema_prev = 0
    
    for year in sorted_years:
        current = yearly_counts[year]
        ema_current = alpha * current + (1 - alpha) * ema_prev
        ema_values[year] = ema_current
        ema_prev = ema_current
    
    return ema_values

# Find best year for each CPC code
print('Calculating EMA and finding best years...')
cpc_best_year = {}
cpc_ema_values = {}

for cpc, yearly_data in cpc_yearly_counts.items():
    # Skip if not enough data points (less than 3 years with data)
    non_zero_years = [y for y, c in yearly_data.items() if c > 0]
    if len(non_zero_years) < 3:
        continue
    
    ema = calculate_ema(yearly_data, alpha=0.2)
    best_year = max(ema.items(), key=lambda x: x[1])
    
    cpc_ema_values[cpc] = ema
    cpc_best_year[cpc] = {
        'best_year': best_year[0],
        'best_ema': best_year[1],
        'max_raw_count': max(yearly_data.values())
    }

# Filter for CPC codes with best year 2022 and minimum activity threshold
cpc_2022 = []
for cpc, data in cpc_best_year.items():
    if data['best_year'] == 2022 and data['max_raw_count'] >= 5:
        # Also check that 2022 is actually in the data
        if 2022 in cpc_yearly_counts.get(cpc, {}):
            cpc_2022.append((cpc, data['best_ema']))

# Sort by EMA value descending
cpc_2022.sort(key=lambda x: x[1], reverse=True)

result_codes = [item[0] for item in cpc_2022]

print(f'Found {len(result_codes)} CPC level 5 codes with best year 2022')
print(f'Top 20: {result_codes[:20]}')

print('__RESULT__:')
print(json.dumps({
    'year_range': f'{min(years_observed)} to {max(years_observed)}',
    'total_cpc_codes': len(cpc_yearly_counts),
    'cpc_with_best_2022': len(result_codes),
    'cpc_codes': result_codes,
    'top_10_emas': [(c, round(e, 2)) for c, e in cpc_2022[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_cpc_codes': 0, 'years_range': '1971 to 2024', 'cpc_codes_best_2022': [], 'count_2022': 0}, 'var_functions.query_db:14': [{'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Loaded 1000 records for analysis', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'Ready to process full dataset', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_count': 677, 'patent_records_count': 277813, 'sample_level5': ['B67D', 'D10B', 'C05B', 'H04S', 'G02F', 'B64C', 'B61C', 'F21Y', 'B65G', 'B29L']}, 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:30': {'sample_completed': True, 'years': 'None', 'cpc_codes_found': 0, 'sample_cpc': []}, 'var_functions.execute_python:34': {'level5_count': 677, 'patent_records': 277813, 'test_extraction': []}, 'var_functions.execute_python:38': {'status': 'debug_complete', 'level5_count': 677, 'record_count': 277813}}

exec(code, env_args)
