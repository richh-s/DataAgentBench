code = """import json
import os

# Check what variables are available in locals()
print('Variables containing query_db:')
for key in locals().keys():
    if 'query_db' in key:
        print(f'  {key}')

# Try to find our data files
pub_key = None
cpc_key = None

for key in locals().keys():
    if 'query_db:10' in key:
        pub_key = key
    if 'query_db:12' in key:
        cpc_key = key

print(f'\nPub key: {pub_key}')
print(f'CPC key: {cpc_key}')

if pub_key and cpc_key:
    pub_file = locals()[pub_key]
    cpc_file = locals()[cpc_key]
    print(f'\nPublication file: {pub_file}')
    print(f'CPC file: {cpc_file}')
    print(f'Pub file exists: {os.path.exists(str(pub_file))}')
    print(f'CPC file exists: {os.path.exists(str(cpc_file))}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:32': [{'symbol': 'A01H', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES', 'level': '5.0'}, {'symbol': 'A01F', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE', 'level': '5.0'}, {'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING', 'level': '5.0'}, {'symbol': 'A01G', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING', 'level': '5.0'}, {'symbol': 'A23J', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS', 'level': '5.0'}, {'symbol': 'A01N', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS', 'level': '5.0'}, {'symbol': 'A01P', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS', 'level': '5.0'}, {'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING', 'level': '5.0'}, {'symbol': 'A01L', 'titleFull': 'SHOEING OF ANIMALS', 'level': '5.0'}, {'symbol': 'A01K', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS', 'level': '5.0'}]}

exec(code, env_args)
