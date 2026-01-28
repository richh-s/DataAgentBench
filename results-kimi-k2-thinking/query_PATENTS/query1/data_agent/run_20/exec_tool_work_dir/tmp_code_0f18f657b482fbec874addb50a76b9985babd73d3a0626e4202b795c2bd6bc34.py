code = """import json
import re
import os

# Get the file path from storage using the correct key access
storage_key = 'var_functions.query_db:28'
if storage_key in locals():
    file_path = locals()[storage_key]
    print("File path from storage:", file_path)
else:
    print("Storage key not found directly in locals()")
    # List available keys to debug
    all_keys = [k for k in locals().keys() if 'query_db' in k]
    print("Available query_db keys:", all_keys)
    file_path = None

# Load records
if file_path and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        records = json.load(f)
    print("Successfully loaded {} records".format(len(records)))
else:
    print("Could not load data file")
    records = []

# Process the records
if records:
    # Show structure of first record
    first = records[0]
    print("First record keys:", list(first.keys()))
    print("Sample publication_date:", first.get('publication_date'))
    
    # Parse CPC codes and years
    patent_data = []
    for record in records:
        pub_date = record.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            cpc_str = record.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        patent_data.append({'code': code, 'year': year})
            except:
                continue
    
    print("Extracted {} CPC code entries".format(len(patent_data)))
    
    # Show unique codes
    if patent_data:
        unique_codes = set(item['code'] for item in patent_data)
        print("Unique CPC codes: {}".format(len(unique_codes)))
        print("Sample codes:", list(unique_codes)[:5])

print("__RESULT__:")
print(json.dumps("Data loaded: {} records".format(len(records)) if records else "No data"))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': 'initialized', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
