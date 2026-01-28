code = """import json
import pandas as pd
import numpy as np
import re

# Read the full patent data
file_path = locals()['var_functions.query_db:20']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patent_records = json.load(f)
else:
    patent_records = locals()['var_functions.query_db:20']

# Read the CPC level 5 definitions
file_path2 = locals()['var_functions.query_db:24']
if isinstance(file_path2, str) and file_path2.endswith('.json'):
    with open(file_path2, 'r') as f:
        cpc_level5_defs = json.load(f)
else:
    cpc_level5_defs = locals()['var_functions.query_db:24']

level5_symbols = set([item['symbol'] for item in cpc_level5_defs])

print('Total patent records:', len(patent_records))
print('Total level 5 symbols:', len(level5_symbols))
print('Sample level 5:', sorted(list(level5_symbols))[:5])

# Check first few records
for i in range(min(3, len(patent_records))):
    rec = patent_records[i]
    pub_date = rec.get('publication_date', 'MISSING')
    cpc = rec.get('cpc', 'MISSING')
    print(f'Record {i+1}: date={pub_date[:50] if pub_date else "MISSING"}, cpc_len={len(str(cpc)) if cpc else 0}')

    try:
        cpc_list = json.loads(cpc) if cpc and isinstance(cpc, str) else []
        for j, item in enumerate(cpc_list[:2]):
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                print(f'  CPC {j}: {code}')
    except:
        print(f'  CPC parsing failed')

print('__RESULT__:')
print(json.dumps({
    'status': 'debug_complete',
    'level5_count': len(level5_symbols),
    'record_count': len(patent_records)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_cpc_codes': 0, 'years_range': '1971 to 2024', 'cpc_codes_best_2022': [], 'count_2022': 0}, 'var_functions.query_db:14': [{'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Loaded 1000 records for analysis', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'Ready to process full dataset', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_count': 677, 'patent_records_count': 277813, 'sample_level5': ['B67D', 'D10B', 'C05B', 'H04S', 'G02F', 'B64C', 'B61C', 'F21Y', 'B65G', 'B29L']}, 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:30': {'sample_completed': True, 'years': 'None', 'cpc_codes_found': 0, 'sample_cpc': []}, 'var_functions.execute_python:34': {'level5_count': 677, 'patent_records': 277813, 'test_extraction': []}}

exec(code, env_args)
