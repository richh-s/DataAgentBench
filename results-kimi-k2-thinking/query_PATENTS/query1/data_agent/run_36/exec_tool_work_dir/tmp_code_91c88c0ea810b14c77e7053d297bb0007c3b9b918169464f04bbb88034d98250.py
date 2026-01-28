code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load the data
file_path = var_functions.query_db:10

# Read the data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")
print("Sample record:")
print(data[0])

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
            # Extract level 5 group (first 4 characters + first digit after / if exists)
            # CPC format: Section (1 char), Class (2 digits), Subclass (1 letter), Group (1-3 digits), /, Subgroup (1-3 digits)
            # Level 5 is the group level (first 4 characters + first digit of the group number)
            
            # For codes like A01H or A01B35, they're already at group level
            # For codes like A01B35/00, we need to extract the group part
            
            if '/' in code:
                main_part, sub_part = code.split('/')
                # Main part has section+class+subclass+group
                # We want first 4 characters + first digit of the group number
                if len(main_part) >= 5:
                    level5_code = main_part[:5]  # First 5 characters gives us section+class+subclass+first group digit
                else:
                    level5_code = main_part
            else:
                # Handle codes without slash
                if len(code) >= 5:
                    level5_code = code[:5]
                else:
                    level5_code = code
            
            cpc_level5_set.add(level5_code)
            yearly_counts[level5_code][year] += 1
            
    except:
        # Skip malformed records
        continue

print(f"Unique level 5 CPC codes: {len(cpc_level5_set)}")
print(f"Year range: {min(y for cpc in yearly_counts for y in yearly_counts[cpc])} - {max(y for cpc in yearly_counts for y in yearly_counts[cpc])}")
print("Sample CPC level 5 codes:", list(cpc_level5_set)[:10])

# Calculate EMA for each CPC group
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
# where α = 0.2

alpha = 0.2
ema_results = {}

for cpc_code in cpc_level5_set:
    # Get sorted years and counts for this CPC
    years_counts = sorted(yearly_counts[cpc_code].items())
    
    if not years_counts:
        continue
    
    # Initialize EMA with the first value
    ema_values = []
    ema = years_counts[0][1]  # Start with the first year's count
    
    for year, count in years_counts:
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
if cpc_best_2022:
    print("Sample CPC codes:", cpc_best_2022[:10])

# Sort by best EMA value (descending)
sorted_cpc_2022 = sorted(cpc_best_2022, 
                        key=lambda x: ema_results[x]['best_ema'], 
                        reverse=True)

print(f"Top 20 CPC groups with best year 2022:")
for i, cpc in enumerate(sorted_cpc_2022[:20]):
    print(f"{i+1}. {cpc}: EMA = {ema_results[cpc]['best_ema']:.2f}")

# Prepare final result
result = sorted_cpc_2022

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
