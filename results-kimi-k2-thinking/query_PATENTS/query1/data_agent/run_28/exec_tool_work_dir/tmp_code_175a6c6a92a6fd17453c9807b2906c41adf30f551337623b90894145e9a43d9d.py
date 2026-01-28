code = """import json
import os
import re
from collections import defaultdict

# Load CPC level 5 codes
with open('/root/shared/81a1a2ee-fb43-4bb2-bed1-3b8d1fc7f3f4.json', 'r') as f:
    cpc_level5_data = json.load(f)

cpc_level5_set = set(item['symbol'] for item in cpc_level5_data)
print(f'Loaded {len(cpc_level5_set)} CPC level 5 codes')

# Load publications data
with open('/root/shared/1b7b1b3f-7a6f-4f3f-8b3f-9b7b1b3f7a6f.json', 'r') as f:
    publications_data = json.load(f)

print(f'Loaded {len(publications_data)} publication records')

# Process data
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
valid_records = 0
invalid_records = 0

for record in publications_data:
    try:
        cpc_json = record.get('cpc', '')
        pub_date = record.get('publication_date', '')
        
        if not cpc_json or not pub_date:
            invalid_records += 1
            continue
        
        # Extract year
        if ',' in pub_date:
            year = int(pub_date.split(',')[-1].strip())
        else:
            match = re.search(r'(\d{4})', pub_date)
            if match:
                year = int(match.group(1))
            else:
                invalid_records += 1
                continue
        
        if year < 2000 or year > 2030:
            invalid_records += 1
            continue
        
        # Extract CPC codes
        cpc_codes = json.loads(cpc_json)
        for cpc_item in cpc_codes:
            code = cpc_item.get('code', '')
            if code:
                main_group = code.split('/')[0] if '/' in code else code
                if main_group in cpc_level5_set:
                    cpc_yearly_counts[main_group][year] += 1
                    valid_records += 1
                    
    except Exception as e:
        invalid_records += 1

print(f'Valid records: {valid_records}, Invalid: {invalid_records}')
print(f'CPC groups found: {len(cpc_yearly_counts)}')

# Get all years
all_years = sorted(set(year for yearly_data in cpc_yearly_counts.values() for year in yearly_data.keys()))
print(f'Years range: {min(all_years)}-{max(all_years)}')

# Calculate EMA
alpha = 0.2
best_in_2022 = []

for cpc_code, yearly_data in cpc_yearly_counts.items():
    # Create complete year series
    counts = [yearly_data.get(year, 0) for year in all_years]
    
    # Calculate EMA
    ema = None
    max_ema = 0
    best_year_idx = 0
    
    for i, count in enumerate(counts):
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year_idx = i
    
    best_year = all_years[best_year_idx]
    
    if best_year == 2022:
        best_in_2022.append({
            'cpc_code': cpc_code,
            'max_ema': max_ema,
            '2022_count': yearly_data.get(2022, 0)
        })

# Sort by max EMA descending
best_in_2022.sort(key=lambda x: x['max_ema'], reverse=True)

print(f'Found {len(best_in_2022)} CPC groups with best year 2022')
if best_in_2022:
    print('Top 10:')
    for i, item in enumerate(best_in_2022[:10]):
        print(f'  {i+1}. {item["cpc_code"]}: EMA={item["max_ema"]:.2f}, 2022 count={item["2022_count"]}')

result = [item['cpc_code'] for item in best_in_2022]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
