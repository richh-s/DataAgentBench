code = """import json
import re
from collections import defaultdict
import glob
import os

# Find the data files
shared_files = glob.glob('/root/shared/*.json')
print(f"Found {len(shared_files)} data files")

# Identify CPC level 5 file and publications file
cpc_candidates = [f for f in shared_files if 'query_db_' in f and any(code in f for code in ['82', '40'])]
pub_candidates = [f for f in shared_files if 'query_db_' in f and any(code in f for code in ['83', '13', '29'])]

if cpc_candidates and pub_candidates:
    cpc_file = cpc_candidates[0]
    pub_file = pub_candidates[0]
    
    print(f"CPC file: {os.path.basename(cpc_file)}")
    print(f"Pub file: {os.path.basename(pub_file)}")
    
    # Load CPC level 5 data
    with open(cpc_file, 'r') as f:
        cpc_data = json.load(f)
    
    cpc_set = set(item['symbol'] for item in cpc_data)
    print(f"CPC level 5 codes loaded: {len(cpc_set)}")
    
    # Process publications in chunks
    cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
    valid = 0
    invalid = 0
    
    print("Processing publications...")
    with open(pub_file, 'r') as f:
        pub_data = json.load(f)
    
    for record in pub_data:
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
        
        except Exception:
            invalid += 1
            continue
    
    print(f"Valid: {valid}, Invalid: {invalid}")
    print(f"CPC groups: {len(cpc_yearly_counts)}")
    
    if cpc_yearly_counts:
        # Get year range
        all_years = sorted({y for yearly in cpc_yearly_counts.values() for y in yearly.keys()})
        print(f"Years: {min(all_years)}-{max(all_years)}")
        
        # Calculate EMA
        alpha = 0.2
        best_in_2022_codes = []
        processed = 0
        
        for cpc_code, yearly_data in cpc_yearly_counts.items():
            processed += 1
            if processed % 1000 == 0:
                print(f"  Processed {processed} CPC codes...")
            
            years = sorted(yearly_data.keys())
            if len(years) < 2 or 2022 not in yearly_data:
                continue
            
            counts = [yearly_data[year] for year in years]
            
            # EMA calculation
            ema = counts[0]
            max_ema = ema
            best_year = years[0]
            
            for i in range(1, len(counts)):
                ema = alpha * counts[i] + (1 - alpha) * ema
                if ema > max_ema:
                    max_ema = ema
                    best_year = years[i]
            
            if best_year == 2022:
                best_in_2022_codes.append({
                    'code': cpc_code,
                    'ema': max_ema,
                    'count_2022': yearly_data[2022]
                })
        
        # Sort by EMA
        best_in_2022_codes.sort(key=lambda x: x['ema'], reverse=True)
        print(f"Found {len(best_in_2022_codes)} CPC groups with best year 2022")
        
        if best_in_2022_codes:
            print("Top 10:")
            for i, item in enumerate(best_in_2022_codes[:10]):
                print(f"  {i+1}. {item['code']}: EMA={item['ema']:.2f}, 2022 count={item['count_2022']}")
        
        result = [item['code'] for item in best_in_2022_codes]
    else:
        result = []
else:
    print("Required files not found")
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:52': [{'symbol': 'A01B'}, {'symbol': 'A01C'}, {'symbol': 'A01D'}, {'symbol': 'A01F'}, {'symbol': 'A01G'}, {'symbol': 'A01H'}, {'symbol': 'A01J'}, {'symbol': 'A01K'}, {'symbol': 'A01L'}, {'symbol': 'A01M'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A21B'}, {'symbol': 'A21C'}, {'symbol': 'A21D'}, {'symbol': 'A22B'}, {'symbol': 'A22C'}, {'symbol': 'A23B'}, {'symbol': 'A23C'}, {'symbol': 'A23D'}, {'symbol': 'A23F'}, {'symbol': 'A23G'}, {'symbol': 'A23J'}, {'symbol': 'A23K'}, {'symbol': 'A23L'}, {'symbol': 'A23N'}, {'symbol': 'A23P'}, {'symbol': 'A23V'}, {'symbol': 'A24B'}, {'symbol': 'A24C'}, {'symbol': 'A24D'}, {'symbol': 'A24F'}, {'symbol': 'A41B'}, {'symbol': 'A41C'}, {'symbol': 'A41D'}, {'symbol': 'A41F'}, {'symbol': 'A41G'}, {'symbol': 'A41H'}, {'symbol': 'A42B'}, {'symbol': 'A42C'}, {'symbol': 'A43B'}, {'symbol': 'A43C'}, {'symbol': 'A43D'}, {'symbol': 'A44B'}, {'symbol': 'A44C'}, {'symbol': 'A44D'}, {'symbol': 'A45B'}, {'symbol': 'A45C'}, {'symbol': 'A45D'}, {'symbol': 'A45F'}], 'var_functions.query_db:53': 'file_storage/functions.query_db:53.json', 'var_functions.query_db:66': [{'total_level5': '677'}], 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:74': [], 'var_functions.query_db:76': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}], 'var_functions.query_db:77': [{'count_2022': '16012'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
