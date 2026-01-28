code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load the data from the file
data_file = locals()['var_functions.query_db:10']

# Read the data
with open(data_file, 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")

# Extract CPC codes and years
yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_level5_set = set()

for record in data:
    cpc_str = record['cpc']
    year = record['year']
    
    if not year or not year.isdigit():
        continue
        
    year = int(year)
    
    # Parse CPC JSON-like string
    try:
        cpc_list = json.loads(cpc_str)
        
        for cpc_item in cpc_list:
            code = cpc_item['code']
            # Extract level 5 group code
            # Level 5 is the group level (section + class + subclass + group)
            # For format like A01B35/00, we want A01B35
            # For format like A01H, we want A01H
            
            if '/' in code:
                main_part = code.split('/')[0]
                level5_code = main_part  # Take everything before the slash
            else:
                level5_code = code
            
            # Ensure we have at least section+class+subclass (4 chars)
            if len(level5_code) >= 4:
                cpc_level5_set.add(level5_code)
                yearly_counts[level5_code][year] += 1
            
    except:
        continue

print(f"Unique level 5 CPC codes: {len(cpc_level5_set)}")
print(f"Year range: {min(y for cpc in yearly_counts for y in yearly_counts[cpc])} - {max(y for cpc in yearly_counts for y in yearly_counts[cpc])}")

# Calculate EMA for each CPC group
alpha = 0.2
ema_results = {}

for cpc_code in cpc_level5_set:
    years_counts = sorted(yearly_counts[cpc_code].items())
    
    if not years_counts:
        continue
    
    # Initialize EMA with the first value
    ema = years_counts[0][1]
    ema_values = [(years_counts[0][0], ema)]
    
    for year, count in years_counts[1:]:
        ema = alpha * count + (1 - alpha) * ema
        ema_values.append((year, ema))
    
    # Find the year with the highest EMA
    if ema_values:
        best_year, best_ema = max(ema_values, key=lambda x: x[1])
        ema_results[cpc_code] = {
            'best_year': best_year,
            'best_ema': best_ema,
            'all_ema': ema_values
        }

# Filter for CPC groups whose best year is 2022
cpc_best_2022 = [cpc for cpc, data in ema_results.items() if data['best_year'] == 2022]

print(f"CPC groups with best year 2022: {len(cpc_best_2022)}")

# Sort by best EMA value (descending) and get top results
sorted_cpc_2022 = sorted(cpc_best_2022, 
                        key=lambda x: ema_results[x]['best_ema'], 
                        reverse=True)

print(f"Top 10 CPC groups with best year 2022:")
for i, cpc in enumerate(sorted_cpc_2022[:10]):
    print(f"{i+1}. {cpc}: EMA = {ema_results[cpc]['best_ema']:.2f}")

# Return final result
result = sorted_cpc_2022

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
