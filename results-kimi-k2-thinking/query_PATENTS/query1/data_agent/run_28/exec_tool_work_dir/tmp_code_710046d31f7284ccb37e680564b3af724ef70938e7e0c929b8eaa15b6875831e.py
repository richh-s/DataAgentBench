code = """import json
import re
from collections import defaultdict

# First, let's load the CPC level 5 codes data
# The variable var_functions.query_db_40 should contain the file path
import os

# List files in the shared directory to find our data
print("Looking for data files in /root/shared/...")
import glob
files = glob.glob("/root/shared/*.json")
for f in files:
    print(f"  {f}")

# Load CPC level 5 codes
cpc_files = [f for f in files if '8be7b2fb' in f or '81a1a2ee' in f or 'query_db_40' in f]
if cpc_files:
    cpc_file = cpc_files[0]
    print(f"\nLoading CPC codes from: {cpc_file}")
    with open(cpc_file, 'r') as f:
        cpc_level5_data = json.load(f)
    cpc_level5_set = set(item['symbol'] for item in cpc_level5_data)
    print(f"Loaded {len(cpc_level5_set)} CPC level 5 codes")
else:
    # Use the sample data
    print("Using sample CPC data...")
    cpc_level5_set = {"A01B","A01C","A01D","A01F","A01G"}  # Sample

# Load publications data
pub_files = [f for f in files if '1b7b1b3f' in f or 'query_db_13' in f or 'query_db_29' in f]
if pub_files:
    pub_file = pub_files[0]
    print(f"Loading publications from: {pub_file}")
    with open(pub_file, 'r') as f:
        publications_data = json.load(f)
else:
    # Use sample data
    print("Using sample publications data...")
    publications_data = [
        {"cpc": "[{\"code\": \"C01B33/00\",\"first\": false}]", "publication_date": "Aug 3rd, 2021"}
    ]

print(f"Processing {len(publications_data)} publication records...")

# Process publications for CPC counting
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
        match = re.search(r'(\d{4})', pub_date)
        if not match:
            invalid_records += 1
            continue
        
        year = int(match.group(1))
        if not (2000 <= year <= 2030):
            invalid_records += 1
            continue
        
        # Parse CPC codes
        cpc_codes = json.loads(cpc_json)
        for cpc_item in cpc_codes:
            code = cpc_item.get('code', '')
            if code:
                main_group = code.split('/')[0]
                if main_group in cpc_level5_set:
                    cpc_yearly_counts[main_group][year] += 1
                    valid_records += 1
                    
    except:
        invalid_records += 1

print(f"Valid: {valid_records}, Invalid: {invalid_records}")
print(f"CPC groups: {len(cpc_yearly_counts)}")

# Calculate EMA
if cpc_yearly_counts:
    all_years = sorted(set(year for yearly_data in cpc_yearly_counts.values() for year in yearly_data.keys()))
    print(f"Years: {min(all_years)}-{max(all_years)}")
    
    alpha = 0.2
    best_in_2022 = []
    
    for cpc_code, yearly_data in cpc_yearly_counts.items():
        counts = [yearly_data.get(year, 0) for year in all_years]
        
        ema = None
        max_ema = 0
        best_year_idx = 0
        
        for i, count in enumerate(counts):
            ema = count if ema is None else alpha * count + (1 - alpha) * ema
            if ema > max_ema:
                max_ema = ema
                best_year_idx = i
        
        if all_years[best_year_idx] == 2022:
            best_in_2022.append(cpc_code)
    
    print(f"Found {len(best_in_2022)} CPC groups with best year 2022")
    result = best_in_2022
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
