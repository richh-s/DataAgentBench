code = """import json
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Read the result from the file
file_path = locals()['var_functions.query_db:20']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        records = json.load(f)
else:
    records = locals()['var_functions.query_db:20']

# Function to extract year from publication_date
def extract_year(date_str):
    try:
        if not date_str:
            return None
        # Match pattern like "Aug 3rd, 2021", "Oct 6th, 2020", "on September 9th, 2022"
        match = re.search(r'\d{4}', str(date_str))
        if match:
            return int(match.group())
        return None
    except Exception as e:
        return None

# Function to parse CPC codes and extract level 5 codes
# Level 5 CPC codes should be main groups like G06Q, H01M (4 characters typically)
def parse_cpc_level5(cpc_json_str):
    level5_codes = set()
    if not cpc_json_str or pd.isna(cpc_json_str):
        return list(level5_codes)
    
    try:
        cpc_list = json.loads(cpc_json_str)
        for item in cpc_list:
            if isinstance(item, dict):
                code = item.get('code', '')
                if code and isinstance(code, str):
                    # Extract main group - split by / and take the part before /
                    # For codes like "G06Q10/06313", we want "G06Q10"
                    # For codes like "G06Q", that's already at the right level
                    if '/' in code:
                        main_part = code.split('/')[0]
                        # For level 5, we want main groups (typically A01C, A01G, G06Q10)
                        # These can be 4-7 characters
                        # Let's use the part before / which is the main group
                        level5_codes.add(main_part)
                    else:
                        # No subgroup, use as is if reasonable length
                        if len(code) >= 3 and not code.startswith('Y'):
                            level5_codes.add(code)
    except Exception as e:
        # Fallback for malformed JSON
        try:
            import ast
            cpc_list = ast.literal_eval(cpc_json_str)
            for item in cpc_list:
                if isinstance(item, dict):
                    code = item.get('code', '')
                    if code and isinstance(code, str):
                        if '/' in code:
                            main_part = code.split('/')[0]
                            if len(main_part) >= 3 and not main_part.startswith(('Y', 'B01F')):
                                level5_codes.add(main_part)
                        else:
                            if len(code) >= 3 and not code.startswith('Y'):
                                level5_codes.add(code)
        except:
            pass
    
    # Filter out very short or obvious metadata codes
    result = [code for code in level5_codes if len(code) >= 3 and not code.startswith(('Y', 'B01F', 'B28'))]
    return result

print('__RESULT__:')
print(json.dumps('Ready to process full dataset'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_cpc_codes': 0, 'years_range': '1971 to 2024', 'cpc_codes_best_2022': [], 'count_2022': 0}, 'var_functions.query_db:14': [{'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Loaded 1000 records for analysis', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
