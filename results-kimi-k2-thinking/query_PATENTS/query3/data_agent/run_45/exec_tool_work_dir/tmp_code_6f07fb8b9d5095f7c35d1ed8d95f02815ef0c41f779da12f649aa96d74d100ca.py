code = """import os
import json
import re
from collections import defaultdict

# Read UNIV CALIFORNIA patents
uc_file = 'var_functions.query_db:44'
uc_patents = []
if os.path.exists(uc_file):
    with open(uc_file, 'r') as f:
        uc_patents = json.load(f)

print(f"Loaded {len(uc_patents)} UNIV CALIFORNIA patents")

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    # Pattern to extract publication number
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.add(pub_num)

print(f"Extracted {len(uc_pub_numbers)} unique UC publication numbers")
print(f"Sample UC pub numbers: {list(uc_pub_numbers)[:5]}")

# Store UC patent CPC codes for later use
uc_cpc_codes = {}
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        cpc_data = patent.get('cpc', '[]')
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                codes = [item.get('code') for item in cpc_list if item.get('code')]
                uc_cpc_codes[pub_num] = codes
            except:
                uc_cpc_codes[pub_num] = []

print(f"Stored CPC codes for {len(uc_cpc_codes)} UC patents")

print('__RESULT__:')
print(json.dumps({
    'uc_patents_loaded': len(uc_patents),
    'uc_pub_numbers': len(uc_pub_numbers),
    'uc_cpc_codes_stored': len(uc_cpc_codes)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
