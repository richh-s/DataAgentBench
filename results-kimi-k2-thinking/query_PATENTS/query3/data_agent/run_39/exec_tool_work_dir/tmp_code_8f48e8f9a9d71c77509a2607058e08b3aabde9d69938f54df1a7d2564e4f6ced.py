code = """import json
import re

# Access the UNIV CALIFORNIA patents data
uc_data_file = var_functions.query_db:16
with open(uc_data_file, 'r') as f:
    uc_patents = json.load(f)

print(f"Loaded {len(uc_patents)} UNIV CALIFORNIA patents")

# Extract publication numbers and create a mapping to CPC codes
uc_pub_to_cpc = {}

for patent in uc_patents:
    patents_info = patent['Patents_info']
    
    # Extract publication number
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\.|publication|pub\s+no|publication\s+no|pub\s+number|has\s+publication\s+no)\s+(?:[A-Z]+-)?([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        # Store the publication number
        uc_pub_to_cpc[pub_num] = patent.get('cpc', '[]')

print(f"Successfully extracted {len(uc_pub_to_cpc)} UNIV CALIFORNIA publication numbers")
print("First few entries:", list(uc_pub_to_cpc.items())[:3])

# Export the mapping
result = uc_pub_to_cpc
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
