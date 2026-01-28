code = """import json
from collections import defaultdict
import os
import glob

# Clean up and find the correct data file
print('Looking for data file...')
json_files = glob.glob('*.json')
print('Available files:', json_files)

# Find the most recent query_db file with data
query_file = None
for f in sorted(json_files, reverse=True):
    if 'query_db' in f:
        query_file = f
        break

if not query_file:
    print('ERROR: No query result file found')
    result = []
else:
    print('Loading from:', query_file)
    
    with open(query_file, 'r') as f:
        data = json.load(f)
    
    print(f'Loaded {len(data)} records')
    
    # Analyze data structure
    if len(data) > 0:
        print('Sample record structure:')
        print('  Keys:', list(data[0].keys()))
        print('  Date sample:', data[0].get('publication_date', 'N/A'))
        print('  CPC sample:', str(data[0].get('cpc', ''))[:100])
    
    # Process patent data
    yearly_counts = defaultdict(lambda: defaultdict(int))
    cpc_groups = set()
    
    records_processed = 0
    for record in data:
        # Extract year
        date_str = record.get('publication_date', '')
        year = None
        if date_str and len(date_str) >= 4:
            year_part = date_str[-4:]
            if year_part.isdigit():
                year = int(year_part)
        
        if not year:
            continue
        
        # Parse CPC codes
        cpc_str = record.get('cpc', '')
        if not cpc_str:
            continue
        
        try:
            cpc_list = json.loads(cpc_str)
            for item in cpc_list:
                code = item.get('code', '')
                if not code:
                    continue
                
                # Extract level 5 group code (main group before slash)
                if '/' in code:
                    group_code = code.split('/')[0]
                else:
                    group_code = code
                
                # Ensure it's a valid CPC code (at least section+class+subclass)
                if len(group_code) >= 4:
                    cpc_groups.add(group_code)
                    yearly_counts[group_code][year] += 1
        except:
            continue
        
        records_processed += 1
    
    print(f'Processed {records_processed} valid records')
    print(f'Found {len(cpc_groups)} unique CPC level 5 groups')
    
    # Show sample CPC groups
    if cpc_groups:
        print('Sample CPC groups:', list(sorted(cpc_groups))[:10])
    
    # Calculate EMA (Exponential Moving Average) for each CPC group
    alpha = 0.2  # smoothing factor
    cpc_best_2022 = []
    
    for group_code in cpc_groups:
        # Get sorted year-count pairs for this group
        year_counts = sorted(yearly_counts[group_code].items())
        if not year_counts:
            continue
        
        # Calculate EMA
        ema = year_counts[0][1]  # Initialize with first year's count
        best_year = year_counts[0][0]
        max_ema = ema
        
        for year, count in year_counts[1:]:
            ema = alpha * count + (1 - alpha) * ema
            if ema > max_ema:
                max_ema = ema
                best_year = year
        
        # Check if the best year is 2022
        if best_year == 2022:
            cpc_best_2022.append((group_code, max_ema))
    
    # Sort by EMA value (descending) to get highest EMA values
    cpc_best_2022.sort(key=lambda x: x[1], reverse=True)
    
    print(f'Found {len(cpc_best_2022)} CPC groups with best year 2022')
    
    # Show top 10
    if cpc_best_2022:
        print('Top 10 CPC groups with best year 2022:')
        for i, (code, ema) in enumerate(cpc_best_2022[:10]):
            print(f'  {i+1}. {code} (EMA: {ema:.2f})')
    
    # Extract just the CPC codes
    result = [code for code, ema in cpc_best_2022]

# Return the final result as JSON array
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:60': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:74': []}

exec(code, env_args)
