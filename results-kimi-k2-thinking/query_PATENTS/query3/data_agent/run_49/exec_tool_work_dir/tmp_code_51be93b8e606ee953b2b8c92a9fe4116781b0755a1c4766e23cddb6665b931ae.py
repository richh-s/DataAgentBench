code = """import json
import re
import os

# Read UC patents from file
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

print(f"Debug: Loaded {len(uc_data)} UC patent records")

# Extract publication numbers from UC patents
uc_pub_numbers = []
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        # Normalize: remove spaces around hyphens
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers.append(pub_num)

print(f"Debug: Extracted {len(uc_pub_numbers)} UC publication numbers")
print(f"Debug: Sample UC pub nums: {uc_pub_numbers[:5]}")

# Read citation data from file
citation_file_path = locals()['var_functions.query_db:26']
print(f"Debug: Citation file path type: {type(citation_file_path)}")
print(f"Debug: Citation file path value: {str(citation_file_path)[:100]}")
print('__RESULT__:')
print(json.dumps('Proceed to loading citation data'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
