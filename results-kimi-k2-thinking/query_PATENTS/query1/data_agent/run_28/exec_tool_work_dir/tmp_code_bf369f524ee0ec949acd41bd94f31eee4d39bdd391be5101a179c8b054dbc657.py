code = """import json
import os
import re
from collections import defaultdict

# Get list of files in the shared directory
shared_dir = '/root/shared'
files = os.listdir(shared_dir)
print('Files in shared directory:')
for f in sorted(files):
    print(f'  {f}')

# Find the relevant data files
cpc_files = [f for f in files if 'query_db_40' in f or '8be7b2fb' in f]
pub_files = [f for f in files if 'query_db_13' in f or '1b7b1b3f' in f or 'query_db_29' in f]

print(f'\nCPC files found: {cpc_files}')
print(f'Publication files found: {pub_files}')

# Identify the files to use
cpc_file_path = None
pub_file_path = None

if cpc_files:
    cpc_file_path = os.path.join(shared_dir, cpc_files[0])
if pub_files:
    pub_file_path = os.path.join(shared_dir, pub_files[0])

print(f'\nUsing CPC file: {cpc_file_path}')
print(f'Using publication file: {pub_file_path}')

if cpc_file_path and pub_file_path:
    # Load CPC level 5 data
    with open(cpc_file_path, 'r') as f:
        cpc_data = json.load(f)
    
    # Load publication data in chunks to handle large file
    cpc_set = {item['symbol'] for item in cpc_data}
    print(f'Loaded {len(cpc_set)} CPC level 5 codes')
    
    # Process publications
    cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
    valid = 0
    invalid = 0
    
    with open(pub_file_path, 'r') as f:
        publications_data = json.load(f)
    
    print(f'Processing {len(publications_data)} publication records...')
    
    for record in publications_data:
        try:
            # Extract year from publication date
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
    
    print(f'Valid: {valid}, Invalid: {invalid}')
    print(f'CPC groups with data: {len(cpc_yearly_counts)}')
    
    if cpc_yearly_counts:
        # Get all years
        all_years = sorted({year for yearly_data in cpc_yearly_counts.values() for year in yearly_data.keys()})
        print(f'Years: {min(all_years)}-{max(all_years)}')
        
        # Calculate EMA for each CPC
        alpha = 0.2
        best_in_2022 = []
        
        for cpc_code, yearly_data in cpc_yearly_counts.items():
            years = sorted(yearly_data.keys())
            if len(years) < 2:
                continue
                
            counts = [yearly_data[year] for year in years]
            
            ema = counts[0]
            max_ema = ema
            best_year = years[0]
            
            for i in range(1, len(counts)):
                ema = alpha * counts[i] + (1 - alpha) * ema
                if ema > max_ema:
                    max_ema = ema
                    best_year = years[i]
            
            if best_year == 2022:
                best_in_2022.append(cpc_code)
        
        print(f'CPC groups with best year 2022: {len(best_in_2022)}')
        result = best_in_2022
    else:
        result = []
else:
    print('Could not find required files')
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:52': [{'symbol': 'A01B'}, {'symbol': 'A01C'}, {'symbol': 'A01D'}, {'symbol': 'A01F'}, {'symbol': 'A01G'}, {'symbol': 'A01H'}, {'symbol': 'A01J'}, {'symbol': 'A01K'}, {'symbol': 'A01L'}, {'symbol': 'A01M'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A21B'}, {'symbol': 'A21C'}, {'symbol': 'A21D'}, {'symbol': 'A22B'}, {'symbol': 'A22C'}, {'symbol': 'A23B'}, {'symbol': 'A23C'}, {'symbol': 'A23D'}, {'symbol': 'A23F'}, {'symbol': 'A23G'}, {'symbol': 'A23J'}, {'symbol': 'A23K'}, {'symbol': 'A23L'}, {'symbol': 'A23N'}, {'symbol': 'A23P'}, {'symbol': 'A23V'}, {'symbol': 'A24B'}, {'symbol': 'A24C'}, {'symbol': 'A24D'}, {'symbol': 'A24F'}, {'symbol': 'A41B'}, {'symbol': 'A41C'}, {'symbol': 'A41D'}, {'symbol': 'A41F'}, {'symbol': 'A41G'}, {'symbol': 'A41H'}, {'symbol': 'A42B'}, {'symbol': 'A42C'}, {'symbol': 'A43B'}, {'symbol': 'A43C'}, {'symbol': 'A43D'}, {'symbol': 'A44B'}, {'symbol': 'A44C'}, {'symbol': 'A44D'}, {'symbol': 'A45B'}, {'symbol': 'A45C'}, {'symbol': 'A45D'}, {'symbol': 'A45F'}], 'var_functions.query_db:53': 'file_storage/functions.query_db:53.json', 'var_functions.query_db:66': [{'total_level5': '677'}], 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
