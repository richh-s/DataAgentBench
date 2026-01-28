code = """import json
from collections import defaultdict

# Load data from the query result
file_path = var_functions.query_db:46

# Read the data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Step 1: Extract CPC codes and years
yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_level5_set = set()

for record in data:
    cpc_str = record['cpc']
    date_str = record['publication_date']
    
    # Extract year from date string (format: "Aug 3rd, 2021")
    year = None
    if date_str and len(date_str) >= 4:
        # Get last 4 characters
        year_candidate = date_str[-4:]
        if year_candidate.isdigit():
            year = int(year_candidate)
    
    if not year:
        continue
    
    # Parse CPC JSON
    try:
        cpc_list = json.loads(cpc_str)
        
        for cpc_item in cpc_list:
            code = cpc_item['code']
            
            # Extract level 5 group code
            # Format can be: "A61K31/00", "A61K31", "H01L21/336", etc.
            # Level 5 is the group level (main group, before the slash)
            if '/' in code:
                main_part = code.split('/')[0]
            else:
                main_part = code
            
            # Add to set and count
            if len(main_part) >= 4:  # Ensure it's a valid code
                cpc_level5_set.add(main_part)
                yearly_counts[main_part][year] += 1
                
    except:
        continue

print(f"Unique level 5 CPC codes: {len(cpc_level5_set)}")
print(f"Year range: {min(y for cpc in yearly_counts for y in yearly_counts[cpc])} - {max(y for cpc in yearly_counts for y in yearly_counts[cpc])}")

# Step 2: Calculate EMA for each CPC group
alpha = 0.2
ema_results = {}

for cpc_code in cpc_level5_set:
    years_counts = sorted(yearly_counts[cpc_code].items())
    
    if not years_counts:
        continue
    
    # Calculate EMA
    ema_values = []
    # Initialize with first value
    ema = years_counts[0][1]
    ema_values.append((years_counts[0][0], ema))
    
    for year, count in years_counts[1:]:
        ema = alpha * count + (1 - alpha) * ema
        ema_values.append((year, ema))
    
    # Find year with highest EMA
    best_year, best_ema = max(ema_values, key=lambda x: x[1])
    
    ema_results[cpc_code] = {
        'best_year': best_year,
        'best_ema': best_ema,
        'all_ema': ema_values
    }

# Step 3: Filter for CPC groups with best year 2022
cpc_best_2022 = []
for cpc_code, data in ema_results.items():
    if data['best_year'] == 2022:
        cpc_best_2022.append((cpc_code, data['best_ema']))

# Step 4: Sort by EMA value (highest first)
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)

print(f"CPC groups with best year 2022: {len(cpc_best_2022)}")
print(f"Top 10:")
for i, (code, ema) in enumerate(cpc_best_2022[:10]):
    print(f"  {i+1}. {code}: EMA = {ema:.2f}")

# Step 5: Extract just the CPC codes
result_codes = [code for code, ema in cpc_best_2022]

print(f"\nTotal CPC level 5 group codes to return: {len(result_codes)}")

# Step 6: Return the result
print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
