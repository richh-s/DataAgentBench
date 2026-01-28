code = """import json
import re

# Load UC publication numbers
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

# Extract UC publication numbers into a set for fast lookup
uc_pub_numbers = set()
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

uc_cpc_mapping = {}  # Map UC pub num to its CPC codes
for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers.add(pub_num)
        
        # Also extract CPC codes for this UC patent
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            primary_cpc_codes = []
            for cpc_item in cpc_data:
                if isinstance(cpc_item, dict):
                    code = cpc_item.get('code')
                    if code and len(code) >= 6:  # Get subclass (first 4 chars) or group
                        # Extract subclass (e.g., C09J from C09J9/02)
                        subclass_match = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                        if subclass_match:
                            subclass = subclass_match.group(1)
                            if subclass not in primary_cpc_codes:
                                primary_cpc_codes.append(subclass)
            uc_cpc_mapping[pub_num] = primary_cpc_codes
        except:
            uc_cpc_mapping[pub_num] = []

print(f"Debug: Found {len(uc_pub_numbers)} UC publication numbers")
print(f"Debug: UC CPC mapping has {len(uc_cpc_mapping)} entries")
print(f"Debug: Sample UC pub nums: {list(uc_pub_numbers)[:5]}")

# Debug: Show some CPC codes
for pub_num in list(uc_pub_numbers)[:3]:
    print(f"Debug: CPC for {pub_num}: {uc_cpc_mapping.get(pub_num, [])}")

print('__RESULT__:')
print(json.dumps('UC data loaded successfully'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data'}

exec(code, env_args)
