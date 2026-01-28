code = """import json
import re
import os

# The data is stored in a file - let's access it
# Use the key from storage to get the actual file path
data_file = var_functions.query_db:28
records = []

# Check if it's a file path string
if isinstance(data_file, str) and os.path.exists(data_file):
    with open(data_file, 'r') as f:
        records = json.load(f)
    print(f"Loaded {len(records)} records from file")
else:
    print("Could not access data file")
    # Fallback: use the preview data from the last response if available
    records = []

# If we have records, process them
if records:
    # Parse CPC codes and years
    patent_data = []
    for record in records:
        # Extract year from publication_date
        pub_date = record.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
        else:
            continue
            
        # Parse CPC codes
        cpc_str = record.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code', '')
                if cpc_code:
                    patent_data.append({
                        'cpc_code': cpc_code,
                        'year': year
                    })
        except:
            continue
    
    print(f"Parsed {len(patent_data)} CPC-year entries")
    
    # Show some sample data
    if patent_data:
        print("Sample entries:", patent_data[:5])
        
        # Get unique CPC codes
        unique_cpcs = set(item['cpc_code'] for item in patent_data)
        print(f"Unique CPC codes: {len(unique_cpcs)}")
        print("Sample CPC codes:", list(unique_cpcs)[:10])

print("__RESULT__:")
print('"Processing setup complete"')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': 'initialized', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
