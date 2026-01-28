code = """import pandas as pd
import json
import re

# Load UNIV CALIFORNIA data
var_name = 'var_functions.query_db:10'
result_file = locals().get(var_name)
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_data = json.load(f)
else:
    uc_data = result_file

# Extract UC publication numbers
uc_pub_numbers = set()
for record in uc_data:
    patents_info = record['Patents_info']
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

print('__RESULT__:')
print(json.dumps({
    'uc_patents_total': len(uc_data),
    'uc_unique_pub_numbers': len(uc_pub_numbers)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_records': 169, 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_count': 4, 'cpc_count': 9}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_count': 0, 'cpc_count': 37}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_count': 120, 'cpc_count': 15}]}, 'var_functions.query_db:14': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:16': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:18': {'uc_patents_found': 114, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00', 'F25B21/00', 'F28D15/00', 'F25B21/00'], 'TW-201925402-A': ['C09J11/04', 'C09J9/02', 'C09D11/52', 'C09D11/322', 'C09J9/02', 'C09D11/037', 'C09J11/04', 'C09D11/52', 'C09D11/322', 'C09D11/037', 'C08K3/08', 'C09J9/02', 'C09D11/037', 'C08K3/042', 'C09J11/04', 'C09D11/322', 'C09D11/52'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883']}}, 'var_functions.execute_python:20': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'sample_uc_pub_numbers': ['WO-2010045542-A3', 'KR-20110004413-A', 'AU-3353000-A', 'US-2021039104-A1', 'US-2023155090-A1', 'JP-S6163700-A', 'RO-70061-A', 'US-2006292670-A1', 'US-2003112494-A1', 'US-11014955-B2']}}

exec(code, env_args)
