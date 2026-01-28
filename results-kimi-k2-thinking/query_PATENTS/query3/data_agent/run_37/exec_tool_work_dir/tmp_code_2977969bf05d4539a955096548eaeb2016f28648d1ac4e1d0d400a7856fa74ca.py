code = """import json
import pandas as pd
import re

# Load the UNIV CALIFORNIA patents data
var_name = 'var_functions.query_db:10'
result_file = locals().get(var_name)

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_data = json.load(f)
else:
    uc_data = result_file

# Extract publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = []
for record in uc_data:
    patents_info = record['Patents_info']
    # Extract publication number from Patents_info
    match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        uc_pub_numbers.append(match.group(1))

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_data),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_uc_pub_numbers': uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_records': 169, 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_count': 4, 'cpc_count': 9}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_count': 0, 'cpc_count': 37}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_count': 120, 'cpc_count': 15}]}, 'var_functions.query_db:14': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}]}

exec(code, env_args)
