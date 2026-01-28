code = """import json
import re
import glob
import os

# Find the correct data files
files = glob.glob('/root/shared/*.json')
print("All files in shared directory:")
for f in sorted(files):
    print(f"  {os.path.basename(f)}")

# Identify CPC and publication files
cpc_files = [f for f in files if 'query_db_82' in f]
pub_files = [f for f in files if 'query_db_83' in f]

if not cpc_files or not pub_files:
    print("Could not find required data files")
    result = []
else:
    cpc_file = cpc_files[0]
    pub_file = pub_files[0]
    
    print(f"\nCPC file: {os.path.basename(cpc_file)}")
    print(f"Pub file: {os.path.basename(pub_file)}")
    
    # Load CPC level 5 codes
    with open(cpc_file, 'r') as f:
        cpc_data = json.load(f)
    
    cpc_set = {item['symbol'] for item in cpc_data}
    print(f"CPC level 5 codes: {len(cpc_set)}")
    
    # Process publications in batches
    cpc_yearly_counts = {}
    valid = 0
    invalid = 0
    
    print("\nProcessing publications...")
    with open(pub_file, 'r') as f:
        pub_data = json.load(f)
    
    print(f"Total publications: {len(pub_data)}")
    
    # Process all records
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
                        if main_group not in cpc_yearly_counts:
                            cpc_yearly_counts[main_group] = {}
                        cpc_yearly_counts[main_group][year] = cpc_yearly_counts[main_group].get(year, 0) + 1
                        valid += 1
                        
        except Exception as e:
            invalid += 1
            continue
        
        if i % 100000 == 0 and i > 0:
            print(f"  Processed {i:,} records...")
    
    print(f"\nValid records: {valid:,}")
    print(f"Invalid records: {invalid:,}")
    print(f"CPC groups with data: {len(cpc_yearly_counts)}")
    
    if cpc_yearly_counts:
        # Get year range
        all_years = sorted({year for yearly_data in cpc_yearly_counts.values() for year in yearly_data.keys()})
        print(f"Years: {min(all_years)}-{max(all_years)}")
        
        # Check for 2022 data
        has_2022 = sum(1 for data in cpc_yearly_counts.values() if 2022 in data)
        print(f"CPC groups with 2022 data: {has_2022}")
        
        # Calculate EMA and identify CPCs with best year 2022
        alpha = 0.2
        best_in_2022 = []
        
        for cpc_code, yearly_data in cpc_yearly_counts.items():
            years = sorted(yearly_data.keys())
            if len(years) < 2:
                continue
            
            # Create complete count series
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
                    'code': cpc_code,
                    'ema': max_ema,
                    'count_2022': yearly_data[2022]
                })
        
        print(f"\nCPC groups with best year 2022: {len(best_in_2022)}")
        
        # Sort and show top results
        best_in_2022.sort(key=lambda x: x['ema'], reverse=True)
        
        if best_in_2022:
            print("Top 20:")
            for i, item in enumerate(best_in_2022[:20]):
                print(f"  {i+1:3d}. {item['code']}: EMA={item['ema']:8.2f}, 2022={item['count_2022']}")
        
        # Extract just the CPC codes
        result = [item['code'] for item in best_in_2022]
    else:
        result = []
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:52': [{'symbol': 'A01B'}, {'symbol': 'A01C'}, {'symbol': 'A01D'}, {'symbol': 'A01F'}, {'symbol': 'A01G'}, {'symbol': 'A01H'}, {'symbol': 'A01J'}, {'symbol': 'A01K'}, {'symbol': 'A01L'}, {'symbol': 'A01M'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A21B'}, {'symbol': 'A21C'}, {'symbol': 'A21D'}, {'symbol': 'A22B'}, {'symbol': 'A22C'}, {'symbol': 'A23B'}, {'symbol': 'A23C'}, {'symbol': 'A23D'}, {'symbol': 'A23F'}, {'symbol': 'A23G'}, {'symbol': 'A23J'}, {'symbol': 'A23K'}, {'symbol': 'A23L'}, {'symbol': 'A23N'}, {'symbol': 'A23P'}, {'symbol': 'A23V'}, {'symbol': 'A24B'}, {'symbol': 'A24C'}, {'symbol': 'A24D'}, {'symbol': 'A24F'}, {'symbol': 'A41B'}, {'symbol': 'A41C'}, {'symbol': 'A41D'}, {'symbol': 'A41F'}, {'symbol': 'A41G'}, {'symbol': 'A41H'}, {'symbol': 'A42B'}, {'symbol': 'A42C'}, {'symbol': 'A43B'}, {'symbol': 'A43C'}, {'symbol': 'A43D'}, {'symbol': 'A44B'}, {'symbol': 'A44C'}, {'symbol': 'A44D'}, {'symbol': 'A45B'}, {'symbol': 'A45C'}, {'symbol': 'A45D'}, {'symbol': 'A45F'}], 'var_functions.query_db:53': 'file_storage/functions.query_db:53.json', 'var_functions.query_db:66': [{'total_level5': '677'}], 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:74': [], 'var_functions.query_db:76': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}], 'var_functions.query_db:77': [{'count_2022': '16012'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json', 'var_functions.execute_python:90': [], 'var_functions.execute_python:96': []}

exec(code, env_args)
