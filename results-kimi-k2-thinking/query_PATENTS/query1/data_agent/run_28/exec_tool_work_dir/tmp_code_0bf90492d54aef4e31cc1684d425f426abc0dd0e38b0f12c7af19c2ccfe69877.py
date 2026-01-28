code = """import json
import re
import os
import glob
from collections import defaultdict

# Find data files
shared_files = glob.glob('/root/shared/*.json')
print("Found files:", len(shared_files))

# Load CPC level 5 data
cpc_file = [f for f in shared_files if 'query_db_82' in f][0]
print("CPC file:", cpc_file)
with open(cpc_file, 'r') as f:
    cpc_data = json.load(f)

cpc_set = {item['symbol'] for item in cpc_data}
print(f"CPC level 5 codes: {len(cpc_set)}")

# Load publication data
pub_file = [f for f in shared_files if 'query_db_83' in f][0]
print("Publication file:", pub_file)
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print(f"Publications: {len(pub_data)}")

# Process data
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
valid = 0
invalid = 0

for i, record in enumerate(pub_data):
    try:
        # Extract year
        pub_date = record.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            invalid += 1
            continue
        
        year = int(year_match.group(1))
        if not (2000 <= year <= 2030):
            invalid += 1
            continue
        
        # Extract CPC codes
        cpc_json = record.get('cpc', '')
        if not cpc_json:
            invalid += 1
            continue
        
        cpc_codes = json.loads(cpc_json)
        for cpc_item in cpc_codes:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                main_group = code.split('/')[0]
                if main_group in cpc_set:
                    cpc_yearly_counts[main_group][year] += 1
                    valid += 1
                    
    except Exception as e:
        invalid += 1
        continue

print(f"Valid records: {valid}, Invalid: {invalid}")
print(f"CPC groups with data: {len(cpc_yearly_counts)}")

# Calculate EMA and find best year
alpha = 0.2
best_in_2022 = []

for cpc_code, yearly_data in cpc_yearly_counts.items():
    # Get sorted years and counts
    years = sorted(yearly_data.keys())
    if len(years) < 2:
        continue
    
    counts = [yearly_data[year] for year in years]
    
    # Calculate EMA
    ema = counts[0]
    max_ema = ema
    best_year = years[0]
    
    for i in range(1, len(counts)):
        ema = alpha * counts[i] + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            best_year = years[i]
    
    if best_year == 2022:
        best_in_2022.append({
            'cpc_code': cpc_code,
            'max_ema': max_ema
        })

# Sort by max EMA descending
best_in_2022.sort(key=lambda x: x['max_ema'], reverse=True)

print(f"CPC groups with best year 2022: {len(best_in_2022)}")
for i, item in enumerate(best_in_2022[:10]):
    print(f"  {i+1}. {item['cpc_code']}: EMA={item['max_ema']:.2f}")

# Return only the CPC codes
result = [item['cpc_code'] for item in best_in_2022]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:52': [{'symbol': 'A01B'}, {'symbol': 'A01C'}, {'symbol': 'A01D'}, {'symbol': 'A01F'}, {'symbol': 'A01G'}, {'symbol': 'A01H'}, {'symbol': 'A01J'}, {'symbol': 'A01K'}, {'symbol': 'A01L'}, {'symbol': 'A01M'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A21B'}, {'symbol': 'A21C'}, {'symbol': 'A21D'}, {'symbol': 'A22B'}, {'symbol': 'A22C'}, {'symbol': 'A23B'}, {'symbol': 'A23C'}, {'symbol': 'A23D'}, {'symbol': 'A23F'}, {'symbol': 'A23G'}, {'symbol': 'A23J'}, {'symbol': 'A23K'}, {'symbol': 'A23L'}, {'symbol': 'A23N'}, {'symbol': 'A23P'}, {'symbol': 'A23V'}, {'symbol': 'A24B'}, {'symbol': 'A24C'}, {'symbol': 'A24D'}, {'symbol': 'A24F'}, {'symbol': 'A41B'}, {'symbol': 'A41C'}, {'symbol': 'A41D'}, {'symbol': 'A41F'}, {'symbol': 'A41G'}, {'symbol': 'A41H'}, {'symbol': 'A42B'}, {'symbol': 'A42C'}, {'symbol': 'A43B'}, {'symbol': 'A43C'}, {'symbol': 'A43D'}, {'symbol': 'A44B'}, {'symbol': 'A44C'}, {'symbol': 'A44D'}, {'symbol': 'A45B'}, {'symbol': 'A45C'}, {'symbol': 'A45D'}, {'symbol': 'A45F'}], 'var_functions.query_db:53': 'file_storage/functions.query_db:53.json', 'var_functions.query_db:66': [{'total_level5': '677'}], 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:74': [], 'var_functions.query_db:76': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}], 'var_functions.query_db:77': [{'count_2022': '16012'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
