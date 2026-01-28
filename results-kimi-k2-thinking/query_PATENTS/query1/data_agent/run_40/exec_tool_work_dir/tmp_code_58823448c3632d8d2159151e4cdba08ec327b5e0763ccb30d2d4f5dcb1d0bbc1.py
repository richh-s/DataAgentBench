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
print(f'Total level 5 symbols in definitions: {len(level5_symbols)}')
print(f'Sample level 5 symbols: {sorted(list(level5_symbols))[:20]}')

# Function to extract year from publication_date
def extract_year(date_str):
    if not date_str or pd.isna(date_str):
        return None
    match = re.search(r'\d{4}', str(date_str))
    return int(match.group()) if match else None

# Test year extraction
sample_dates = [
    "Aug 3rd, 2021",
    "Oct 6th, 2020", 
    "on September 9th, 2022"
]
for date in sample_dates:
    print(f'Date: "{date}" -> Year: {extract_year(date)}')

# Function to extract and map CPC codes to level 5
def extract_cpc_level5(cpc_json_str):
    if not cpc_json_str or pd.isna(cpc_json_str) or cpc_json_str == '[]':
        return []
    
    level5_codes = set()
    
    try:
        # Parse JSON
        if isinstance(cpc_json_str, str):
            cpc_list = json.loads(cpc_json_str)
        else:
            cpc_list = cpc_json_str
            
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                if code and isinstance(code, str):
                    # Skip Y-codes and metadata
                    if code.startswith('Y'):
                        continue
                    
                    # Extract main group before /
                    if '/' in code:
                        main_group = code.split('/')[0]
                    else:
                        main_group = code
                    
                    # Map to level 5: find parent by progressively shortening
                    # Example: G06Q10 → G06Q (level 5)
                    # Example: H01L21 → H01L (level 5)
                    # Example: A01C1 → A01C (level 5)
                    test_code = main_group
                    while len(test_code) > 3:
                        if test_code in level5_symbols:
                            level5_codes.add(test_code)
                            break
                        # Remove last character and try again
                        test_code = test_code[:-1]
                    
    except Exception as e:
        # Fallback parsing for malformed JSON
        # print(f'JSON parse error: {e}')
        try:
            import ast
            cpc_list = ast.literal_eval(str(cpc_json_str))
            for item in cpc_list:
                if isinstance(item, dict) and 'code' in item:
                    code = item['code']
                    if code and isinstance(code, str) and not code.startswith('Y'):
                        if '/' in code:
                            main_group = code.split('/')[0]
                        else:
                            main_group = code
                        test_code = main_group
                        while len(test_code) > 3:
                            if test_code in level5_symbols:
                                level5_codes.add(test_code)
                                break
                            test_code = test_code[:-1]
        except:
            # Last resort: regex extraction
            codes = re.findall(r'"code":\s*"([^"]+)"', str(cpc_json_str))
            for code in codes:
                if not code.startswith('Y'):
                    if '/' in code:
                        main_group = code.split('/')[0]
                    else:
                        main_group = code
                    test_code = main_group
                    while len(test_code) > 3:
                        if test_code in level5_symbols:
                            level5_codes.add(test_code)
                            break
                        test_code = test_code[:-1]
    
    return list(level5_codes)

# Test CPC extraction on sample data
sample_cpc = '[
  {"code": "G06Q10/06313", "first": false, "inventive": true, "tree": []},
  {"code": "B01F2215/0495", "first": false, "inventive": false, "tree": []},
  {"code": "H01L21/02", "first": true, "inventive": true, "tree": []}
]'

extracted = extract_cpc_level5(sample_cpc)
print(f'Sample CPC extraction: {sample_cpc}')
print(f'Extracted level 5 codes: {extracted}')

# Test on real data
if patent_records:
    print(f"\nTesting on first 5 patent records:")
    for i, record in enumerate(patent_records[:5]):
        cpc = record.get('cpc', '')
        year = extract_year(record.get('publication_date', ''))
        extracted_codes = extract_cpc_level5(cpc)
        print(f"Record {i+1}: Year={year}, CPC codes={len(extracted_codes)}: {extracted_codes[:5]}")

print('__RESULT__:')
print(json.dumps({
    'status': 'debugging complete',
    'level5_symbols_count': len(level5_symbols),
    'sample_symbols': sorted(list(level5_symbols))[:10],
    'sample_extraction': extracted
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'first_record_keys': ['Patents_info', 'cpc', 'publication_date', 'title_localized'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_pub_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_cpc_codes': 0, 'years_range': '1971 to 2024', 'cpc_codes_best_2022': [], 'count_2022': 0}, 'var_functions.query_db:14': [{'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Loaded 1000 records for analysis', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'Ready to process full dataset', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_count': 677, 'patent_records_count': 277813, 'sample_level5': ['B67D', 'D10B', 'C05B', 'H04S', 'G02F', 'B64C', 'B61C', 'F21Y', 'B65G', 'B29L']}, 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:30': {'sample_completed': True, 'years': 'None', 'cpc_codes_found': 0, 'sample_cpc': []}}

exec(code, env_args)
