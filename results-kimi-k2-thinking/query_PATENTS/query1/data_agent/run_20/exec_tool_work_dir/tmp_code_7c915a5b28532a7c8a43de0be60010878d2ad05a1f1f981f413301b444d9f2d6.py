code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the CPC and publication_date data from the file
file_path = var_functions.query_db:8
with open(file_path, 'r') as f:
    records = json.load(f)

# Parse CPC codes and extract years
patent_data = []
for record in records:
    try:
        # Parse publication date
        pub_date_str = record.get('publication_date', '')
        if pub_date_str:
            # Extract year from date string like "Aug 3rd, 2021" or "Oct 6th, 2020"
            year_match = re.search(r'(\d{4})', pub_date_str)
            if year_match:
                year = int(year_match.group(1))
            else:
                continue
        else:
            continue
        
        # Parse CPC JSON string
        cpc_str = record.get('cpc', '[]')
        if cpc_str:
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code', '')
                    if cpc_code:
                        patent_data.append({
                            'cpc_code': cpc_code,
                            'year': year,
                            'full_cpc_item': cpc_item
                        })
            except json.JSONDecodeError:
                # Skip if CPC data can't be parsed
                continue
    except Exception as e:
        # Skip records with issues
        continue

print(f"Total patent records processed: {len(patent_data)}")
print(f"Sample records: {patent_data[:3]}")

# Count filings per year for each CPC code
cpc_year_counts = {}
for item in patent_data:
    cpc_code = item['cpc_code']
    year = item['year']
    
    if cpc_code not in cpc_year_counts:
        cpc_year_counts[cpc_code] = {}
    
    cpc_year_counts[cpc_code][year] = cpc_year_counts[cpc_code].get(year, 0) + 1

print(f"Number of unique CPC codes: {len(cpc_year_counts)}")
print(f"Sample CPC codes and counts: {list(cpc_year_counts.items())[:3]}")

# Extract level 5 CPC codes (format like A01H, B29C, etc.)
# Level 5 codes are typically the main group level (e.g., A01H, not A01H1/00 or A01H1/02)
def get_level_5_code(cpc_code):
    """Extract level 5 CPC code (main group level)"""
    # Remove any dots and split by /
    if not cpc_code:
        return None
    
    # Examples: "A01H1/00" -> "A01H", "B29C70/48" -> "B29C", "C01B33/00" -> "C01B"
    # Also handle cases like "A01H" which are already level 5
    
    if '/' in cpc_code:
        main_part = cpc_code.split('/')[0]
        # Remove digits from the end to get the group code
        # e.g., "A01H1" -> "A01H", "B29C70" -> "B29C"
        
        # Find where the digits start at the end
        i = len(main_part) - 1
        while i >= 0 and main_part[i].isdigit():
            i -= 1
        
        return main_part[:i+1]
    else:
        # Already a level 5 code (e.g., "A01H")
        return cpc_code

# Aggregate counts at level 5
level_5_counts = {}
for cpc_code, year_counts in cpc_year_counts.items():
    level_5_code = get_level_5_code(cpc_code)
    if level_5_code:
        if level_5_code not in level_5_counts:
            level_5_counts[level_5_code] = {}
        
        for year, count in year_counts.items():
            level_5_counts[level_5_code][year] = level_5_counts[level_5_code].get(year, 0) + count

print(f"Number of level 5 CPC codes: {len(level_5_counts)}")
print(f"Sample level 5 CPC codes: {list(level_5_counts.keys())[:10]}")

# Calculate EMA for each level 5 CPC code
alpha = 0.2  # smoothing factor
cpc_ema_data = {}

for cpc_code, year_counts in level_5_counts.items():
    # Get all years with data
    years = sorted(year_counts.keys())
    if not years:
        continue
    
    # Start with the first year as initial EMA value
    ema_values = {}
    first_year = years[0]
    ema_values[first_year] = year_counts[first_year]
    
    # Calculate EMA for subsequent years
    for i in range(1, len(years)):
        year = years[i]
        current_value = year_counts[year]
        prev_year = years[i-1]
        prev_ema = ema_values[prev_year]
        
        # EMA formula: EMA_t = alpha * value_t + (1 - alpha) * EMA_{t-1}
        ema_values[year] = alpha * current_value + (1 - alpha) * prev_ema
    
    cpc_ema_data[cpc_code] = ema_values

print(f"Calculated EMA for {len(cpc_ema_data)} CPC codes")

# Find best year for each CPC code (year with highest EMA)
cpc_best_year = {}
for cpc_code, ema_values in cpc_ema_data.items():
    if ema_values:
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        cpc_best_year[cpc_code] = {
            'best_year': best_year,
            'ema_values': ema_values
        }

# Filter for CPC codes whose best year is 2022
cpc_2022_best = [cpc_code for cpc_code, data in cpc_best_year.items() if data['best_year'] == 2022]

print(f"Number of CPC codes with best year 2022: {len(cpc_2022_best)}")
print(f"Sample CPC codes with best year 2022: {cpc_2022_best[:10]}")

# Ensure these are level 5 codes (they should be based on our extraction)
# Filter to make sure we return only valid level 5 codes
valid_level_5_codes = []
for cpc_code in cpc_2022_best:
    # Validate it's a proper level 5 code (4 characters starting with letter, followed by digits)
    if len(cpc_code) >= 3 and len(cpc_code) <= 5 and cpc_code[0].isalpha():
        valid_level_5_codes.append(cpc_code)

# Sort the results
valid_level_5_codes.sort()

result_json = json.dumps(valid_level_5_codes)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
