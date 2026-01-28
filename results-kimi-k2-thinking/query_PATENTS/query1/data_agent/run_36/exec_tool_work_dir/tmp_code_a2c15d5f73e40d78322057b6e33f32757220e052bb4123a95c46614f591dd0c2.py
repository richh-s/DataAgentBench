code = """import json
from collections import defaultdict
import glob

# Find the query result file
query_files = glob.glob('*query_db*70*.json')
print('Query files found:', query_files)

if query_files:
    data_file = query_files[0]
    print('Loading from:', data_file)
    
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    print(f'Loaded {len(data)} records')
    
    # Process data
    yearly_counts = defaultdict(lambda: defaultdict(int))
    cpc_groups = set()
    
    for record in data:
        date_str = record.get('publication_date', '')
        year = None
        if date_str and len(date_str) >= 4:
            yr = date_str[-4:]
            if yr.isdigit():
                year = int(yr)
        
        if not year:
            continue
        
        cpc_str = record.get('cpc', '')
        if not cpc_str:
            continue
        
        try:
            cpc_list = json.loads(cpc_str)
            for item in cpc_list:
                code = item.get('code', '')
                if not code:
                    continue
                
                if '/' in code:
                    group_code = code.split('/')[0]
                else:
                    group_code = code
                
                if len(group_code) >= 4:
                    cpc_groups.add(group_code)
                    yearly_counts[group_code][year] += 1
        except:
            continue
    
    print(f'Found {len(cpc_groups)} CPC level 5 groups')
    
    # Calculate EMA
    alpha = 0.2
    cpc_best_2022 = []
    
    for group_code in cpc_groups:
        year_counts = sorted(yearly_counts[group_code].items())
        if not year_counts:
            continue
        
        ema = year_counts[0][1]
        best_year = year_counts[0][0]
        max_ema = ema
        
        for year, count in year_counts[1:]:
            ema = alpha * count + (1 - alpha) * ema
            if ema > max_ema:
                max_ema = ema
                best_year = year
        
        if best_year == 2022:
            cpc_best_2022.append((group_code, max_ema))
    
    cpc_best_2022.sort(key=lambda x: x[1], reverse=True)
    cpc_codes_2022 = [code for code, ema in cpc_best_2022]
    
    print(f'Found {len(cpc_codes_2022)} CPC groups with best year 2022')
    
    # Return result
    result_json = json.dumps(cpc_codes_2022)
    print('__RESULT__:')
    print(result_json)
else:
    print('No data file found')
    print('__RESULT__:')
    print('[]')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:60': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
