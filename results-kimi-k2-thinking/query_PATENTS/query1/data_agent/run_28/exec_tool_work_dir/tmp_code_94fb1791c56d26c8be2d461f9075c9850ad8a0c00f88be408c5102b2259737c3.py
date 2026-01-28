code = """import json
import re

# Load CPC level 5 codes
cpc_level5_path = '/root/shared/8be7b2fb-7b6f-4f3f-8b3f-9b7b1b3f7a6f.json'
publications_sample_path = '/root/shared/1b7b1b3f-7a6f-4f3f-8b3f-9b7b1b3f7a6f.json'

# Load CPC level 5 codes
with open(cpc_level5_path, 'r') as f:
    cpc_level5_data = json.load(f)

# Create a set of level 5 CPC codes for fast lookup
cpc_level5_set = set(item['symbol'] for item in cpc_level5_data)
print(f"Loaded {len(cpc_level5_set)} CPC level 5 codes")

# Load sample publication data to test
with open(publications_sample_path, 'r') as f:
    sample_data = json.load(f)

print(f"Sample has {len(sample_data)} records")

# Test date parsing and CPC extraction
def parse_publication_date(date_str):
    """Extract year from publication date string"""
    try:
        if ',' in date_str:
            year_str = date_str.split(',')[-1].strip()
            year = int(year_str)
        else:
            # Try to find 4-digit year
            year_match = re.search(r'(\d{4})', date_str)
            if year_match:
                year = int(year_match.group(1))
            else:
                return None
        
        # Validate year range
        if 1900 <= year <= 2030:
            return year
        return None
    except:
        return None

def extract_main_cpc_group(cpc_code):
    """Extract main group from CPC code format like 'C01B33/00'"""
    try:
        parts = cpc_code.split('/')
        return parts[0]  # This gives us 'C01B33'
    except:
        return None

# Test with sample data
test_records = 0
for record in sample_data[:10]:
    pub_date = record.get('publication_date', '')
    cpc_json = record.get('cpc', '')
    
    year = parse_publication_date(pub_date)
    print(f"Date: {pub_date} -> Year: {year}")
    
    try:
        cpc_codes = json.loads(cpc_json)
        for cpc_item in cpc_codes:
            code = cpc_item.get('code', '')
            main_group = extract_main_cpc_group(code)
            is_level5 = main_group in cpc_level5_set if main_group else False
            print(f"  CPC: {code} -> Main: {main_group} -> Level5: {is_level5}")
    except:
        print(f"  Invalid CPC JSON: {cpc_json[:50]}...")
    
    test_records += 1
    if test_records >= 5:
        break

print("Test parsing completed successfully")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
