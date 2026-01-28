code = """import json
import pandas as pd
import re

# Load full dataset to process
var_name = 'var_functions.query_db:10'
result_file = locals().get(var_name)

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_records = json.load(f)
else:
    uc_records = result_file

# Create a mapping of UC publication numbers to their CPC codes
uc_pub_to_cpc = {}
for record in uc_records:
    patents_info = record['Patents_info']
    # Extract publication number
    match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        cpc_data = json.loads(record['cpc']) if record['cpc'] else []
        primary_cpc = [c['code'] for c in cpc_data if c.get('first', False) or c.get('inventive', False)]
        uc_pub_to_cpc[pub_num] = primary_cpc

print('__RESULT__:')
print(json.dumps({
    'uc_patents_found': len(uc_pub_to_cpc),
    'sample_mapping': {k: v for k, v in list(uc_pub_to_cpc.items())[:3]}
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_records': 169, 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_count': 4, 'cpc_count': 9}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_count': 0, 'cpc_count': 37}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_count': 120, 'cpc_count': 15}]}, 'var_functions.query_db:14': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:16': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}}

exec(code, env_args)
