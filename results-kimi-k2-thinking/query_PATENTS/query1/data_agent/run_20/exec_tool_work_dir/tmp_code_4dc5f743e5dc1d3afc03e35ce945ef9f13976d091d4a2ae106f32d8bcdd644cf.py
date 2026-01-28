code = """import json
import re

# Access the data from storage
storage_key = 'var_functions.query_db:8'
print(f"Available variables: {list(locals().keys())}")

# Get the actual data
if storage_key in locals():
    data_ref = locals()[storage_key]
    print(f"Data reference type: {type(data_ref)}")
    print(f"Data reference content preview: {str(data_ref)[:200]}")
else:
    print(f"Storage key {storage_key} not found")
    data_ref = None

# The data might be a JSON string that needs parsing
records = []
if data_ref is not None:
    if isinstance(data_ref, str):
        # Try to parse as JSON
        try:
            records = json.loads(data_ref)
            print(f"Parsed {len(records)} records from JSON string")
        except:
            # If it's a file path
            if 'file' in data_ref.lower() or data_ref.endswith('.json'):
                try:
                    with open(data_ref, 'r') as f:
                        records = json.load(f)
                    print(f"Loaded {len(records)} records from file: {data_ref}")
                except Exception as e:
                    print(f"Error loading file: {e}")
    elif isinstance(data_ref, list):
        records = data_ref
        print(f"Using {len(records)} records from list")

print(f"Total records: {len(records)}")

# Show first record if available
if records and len(records) > 0:
    print("First record preview:")
    print(json.dumps(records[0], indent=2)[:500] + "...")
else:
    print("No records found or error in data loading")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
