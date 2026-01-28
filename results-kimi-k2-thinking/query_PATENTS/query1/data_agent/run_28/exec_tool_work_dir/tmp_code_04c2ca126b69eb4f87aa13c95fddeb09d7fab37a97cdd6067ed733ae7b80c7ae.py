code = """import json
import pandas as pd
from datetime import datetime

# Load the CPC level 5 codes
cpc_level5_path = var_functions.query_db_16
with open(cpc_level5_path, 'r') as f:
    cpc_level5_data = json.load(f)

# Create a set of level 5 CPC codes for fast lookup
cpc_level5_set = set(item['symbol'] for item in cpc_level5_data)
print(f"Loaded {len(cpc_level5_set)} CPC level 5 codes")

# Load the publication data
publications_path = var_functions.query_db_13

# Process data
with open(publications_path, 'r') as f:
    data = json.load(f)

print(f"Processing {len(data)} publications...")

# Initialize CPC yearly counts
cpc_yearly_counts = {}
valid_records = 0
invalid_records = 0

for record in data:
    try:
        cpc_json = record.get('cpc', '')
        pub_date = record.get('publication_date', '')
        
        if not cpc_json or not pub_date:
            invalid_records += 1
            continue
        
        # Parse publication year
        try:
            # Extract year from natural language date
            if ',' in pub_date:
                year_str = pub_date.split(',')[-1].strip()
                year = int(year_str)
            else:
                # Try to find 4-digit year
                import re
                year_match = re.search(r'(\d{4})', pub_date)
                if year_match:
                    year = int(year_match.group(1))
                else:
                    invalid_records += 1
                    continue
        except:
            invalid_records += 1
            continue
        
        # Skip if year is not in reasonable range
        if year < 2000 or year > 2030:
            invalid_records += 1
            continue
        
        # Parse CPC codes
        try:
            # The CPC field contains JSON-like data
            cpc_codes = json.loads(cpc_json)
            
            for cpc_item in cpc_codes:
                code = cpc_item.get('code', '')
                if not code:
                    continue
                
                # Extract group code (level 5) - format like "C01B33/00"
                # The level 5 codes are like "A62B", "A63G", etc.
                parts = code.split('/')
                main_group = parts[0]
                
                # Check if this main group is in our level 5 set
                if main_group in cpc_level5_set:
                    # Count this occurrence
                    if main_group not in cpc_yearly_counts:
                        cpc_yearly_counts[main_group] = {}
                    if year not in cpc_yearly_counts[main_group]:
                        cpc_yearly_counts[main_group][year] = 0
                    cpc_yearly_counts[main_group][year] += 1
                    valid_records += 1
                    
        except json.JSONDecodeError:
            invalid_records += 1
            continue
        except Exception:
            invalid_records += 1
            continue
            
    except Exception:
        invalid_records += 1
        continue

print(f"Valid records: {valid_records}, Invalid: {invalid_records}")
print(f"Processed CPC counts for {len(cpc_yearly_counts)} CPC groups")

# Find all years present
all_years = set()
for cpc_data in cpc_yearly_counts.values():
    all_years.update(cpc_data.keys())

all_years = sorted(list(all_years))
print(f"Years range: {min(all_years)} - {max(all_years)}")
print(f"Total years: {len(all_years)}")

# Calculate Exponential Moving Average (EMA) for each CPC
alpha = 0.2
cpc_ema_results = {}

for cpc_code, yearly_data in cpc_yearly_counts.items():
    if not yearly_data:
        continue
    
    # Create a complete series for all years
    year_counts = []
    for year in all_years:
        year_counts.append(yearly_data.get(year, 0))
    
    # Calculate EMA
    ema_values = []
    ema = None
    
    for i, count in enumerate(year_counts):
        if ema is None:
            # Initialize with first value
            ema = count
        else:
            # EMA formula
            ema = alpha * count + (1 - alpha) * ema
        ema_values.append(ema)
    
    # Find year with highest EMA
    max_ema_idx = ema_values.index(max(ema_values))
    best_year = all_years[max_ema_idx]
    
    cpc_ema_results[cpc_code] = {
        'best_year': best_year,
        'max_ema': ema_values[max_ema_idx],
        'yearly_counts': dict(zip(all_years, year_counts)),
        'ema_values': dict(zip(all_years, ema_values))
    }

# Filter for CPCs with best year = 2022
best_in_2022 = []
for cpc_code, results in cpc_ema_results.items():
    if results['best_year'] == 2022:
        best_in_2022.append({
            'cpc_code': cpc_code,
            'max_ema': results['max_ema'],
            'yearly_counts': results['yearly_counts']
        })

# Sort by max_ema descending
best_in_2022.sort(key=lambda x: x['max_ema'], reverse=True)

print(f"Found {len(best_in_2022)} CPC groups with best year 2022")
if best_in_2022:
    print("Top 5 by EMA:")
    for i, item in enumerate(best_in_2022[:5]):
        print(f"{i+1}. {item['cpc_code']}: EMA={item['max_ema']:.2f}, 2022 count={item['yearly_counts'].get(2022, 0)}")
    
    # Print the result
    result = [item['cpc_code'] for item in best_in_2022]
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('No CPC groups with best year 2022 found')
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
