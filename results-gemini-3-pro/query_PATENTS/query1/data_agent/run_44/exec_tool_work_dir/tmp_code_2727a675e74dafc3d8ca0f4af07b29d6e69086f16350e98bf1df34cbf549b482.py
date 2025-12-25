code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
with open(locals()['var_function-call-16702837744120307450'], 'r') as f:
    cpc_level5_data = json.load(f)

valid_cpc_level5 = set()
for item in cpc_level5_data:
    if 'symbol' in item:
        valid_cpc_level5.add(item['symbol'])

# Load Filings
with open(locals()['var_function-call-7782197232993617340'], 'r') as f:
    filings_data = json.load(f)

# Aggregate counts
# Structure: {cpc_code: {year: count}}
cpc_counts = {}
global_years = set()

for filing in filings_data:
    f_date = filing.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract year
    match = re.search(r'\b(18|19|20)\d{2}\b', f_date)
    if match:
        year = int(match.group(0))
    else:
        continue
    
    global_years.add(year)
    
    cpc_json_str = filing.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json_str)
    except:
        continue
    
    # Identify unique valid level 5 codes for this filing
    seen_codes_for_this_filing = set()
    
    for entry in cpc_list:
        code = entry.get('code', '')
        # Map to subclass (Level 5). 
        # Usually first 4 chars, e.g. A01B.
        # But sometimes code might be shorter? 
        # Check against valid_cpc_level5 set.
        # Try length 4 first
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_cpc_level5:
                seen_codes_for_this_filing.add(subclass)
        # Some level 5 codes might be 3 chars? No, standard is 4.
        # Let's stick to matching valid_cpc_level5.
    
    for code in seen_codes_for_this_filing:
        if code not in cpc_counts:
            cpc_counts[code] = {}
        cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1

if not global_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(global_years)
max_year = max(global_years)
all_years = sorted(list(range(min_year, max_year + 1)))

# Calculate EMA and find best year
alpha = 0.2
result_cpc_codes = []

for cpc, year_counts in cpc_counts.items():
    ema = 0
    # Initialization
    # Option 1: First value is the count of the first year (even if 0, start from min_year)
    # Option 2: Start from the first year this CPC appears?
    # Standard EMA usually runs on the full time series.
    # I'll run from min_year to max_year.
    
    best_ema = -1.0
    best_year = -1
    
    # Initialize EMA with the count of the first year
    first_count = year_counts.get(min_year, 0)
    ema = first_count
    
    if min_year == 2022:
        if ema > best_ema:
            best_ema = ema
            best_year = min_year
    elif min_year > 2022:
        pass # Should not happen if data is historic
    else:
        # Check year min_year
        if ema >= best_ema: # Using >= to capture if it's the only year or ties
             best_ema = ema
             best_year = min_year

    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_cpc_codes.append(cpc)

print("__RESULT__:")
print(json.dumps(result_cpc_codes))"""

env_args = {'var_function-call-15891582207541011171': 'file_storage/function-call-15891582207541011171.json', 'var_function-call-11737208954615889978': [{'count(*)': '277813'}], 'var_function-call-16702837744120307450': 'file_storage/function-call-16702837744120307450.json', 'var_function-call-1429926228084239010': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'level': '9.0', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'level': '9.0', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'level': '9.0', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'level': '9.0', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'level': '9.0', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_function-call-7073709861002867650': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_function-call-7782197232993617340': 'file_storage/function-call-7782197232993617340.json'}

exec(code, env_args)
