code = """import json
import pandas as pd
from collections import defaultdict

# Load data file from query
file_path = vars().get('var_functions.query_db:30') or 'query_result.json'

if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    # Try to find the variable directly
    data = None
    for key, value in locals().items():
        if 'query_db' in str(key) and '30' in str(key):
            if isinstance(value, str) and value.endswith('.json'):
                with open(value, 'r') as f:
                    data = json.load(f)
                break
            else:
                data = value
                break

if data is None:
    print('Could not load data')
    exit()

print('Records:', len(data))
print('First record keys:', list(data[0].keys()))

# Analyze CPC codes
from collections import Counter
code_format = Counter()

cpc_examples = []
for record in data[:20]:
    date_str = record.get('publication_date', '')
    
    # Extract year
    year_match = date_str.split(',')[-1].strip() if date_str else ''
    year = year_match[-4:] if year_match and year_match[-4:].isdigit() else None
    
    try:
        cpc_list = json.loads(record['cpc'])
        for item in cpc_list:
            code = item['code']
            cpc_examples.append(code)
            
            # Analyze format
            if '/' in code:
                main = code.split('/')[0]
                code_format[f'group_{len(main)}'] += 1
            else:
                code_format[f'symbol_{len(code)}'] += 1
                
    except:
        continue

print('\nCPC code examples:', cpc_examples[:15])
print('\nCode format distribution:', dict(code_format))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
