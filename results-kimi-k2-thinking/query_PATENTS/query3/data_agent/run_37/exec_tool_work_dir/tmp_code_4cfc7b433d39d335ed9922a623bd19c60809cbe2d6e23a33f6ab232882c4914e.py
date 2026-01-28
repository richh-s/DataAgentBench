code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load UNIV CALIFORNIA data
var_name = 'var_functions.query_db:10'
result_file = locals().get(var_name)
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_data = json.load(f)
else:
    uc_data = result_file

# Build mapping of UC publication numbers to CPC codes
uc_pub_to_cpc = {}
for record in uc_data:
    patents_info = record['Patents_info']
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        if record['cpc']:
            cpc_data = json.loads(record['cpc'])
            primary_codes = [c['code'] for c in cpc_data if c.get('first') or c.get('inventive')]
            uc_pub_to_cpc[pub_num] = primary_codes

# Now let's load all patent data and find citations to UC patents
var_name_all = 'var_functions.query_db:24'
result_file_all = locals().get(var_name_all)
if isinstance(result_file_all, str) and result_file_all.endswith('.json'):
    with open(result_file_all, 'r') as f:
        all_data = json.load(f)
else:
    all_data = result_file_all

# Find patents that cite UC patents and extract their assignees
uc_citing_relationships = []  # List of (citing_assignee, cited_uc_patent, cpc_codes)

for record in all_data:
    patents_info = record['Patents_info']
    match = re.search(r'^([A-Z\s&\.,-]+)\s+(?:holds|owns|is assigned to|assigned to)\s+(?:the\s+)?(?:[A-Z]{2}\s+)?patent', patents_info)
    if not match:
        match = re.search(r'^([A-Z\s&\.,-]+)\s+holds', patents_info)
    
    if match:
        assignee = match.group(1).strip()
        # Skip UNIV CALIFORNIA itself
        if 'UNIV CALIFORNIA' in assignee:
            continue
            
        # Check citations
        if record['citation']:
            citations = json.loads(record['citation'])
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub and cited_pub in uc_pub_to_cpc:
                    cpc_codes = uc_pub_to_cpc[cited_pub]
                    if cpc_codes:  # Only add if there are CPC codes
                        uc_citing_relationships.append({
                            'citing_assignee': assignee,
                            'cited_uc_patent': cited_pub,
                            'cpc_codes': cpc_codes
                        })

print('__RESULT__:')
print(json.dumps({
    'total_relationships': len(uc_citing_relationships),
    'unique_citing_assignees': len(set(r['citing_assignee'] for r in uc_citing_relationships)),
    'unique_cited_uc_patents': len(set(r['cited_uc_patent'] for r in uc_citing_relationships)),
    'sample_relationships': uc_citing_relationships[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_records': 169, 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_count': 4, 'cpc_count': 9}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_count': 0, 'cpc_count': 37}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_count': 120, 'cpc_count': 15}]}, 'var_functions.query_db:14': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:16': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:18': {'uc_patents_found': 114, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00', 'F25B21/00', 'F28D15/00', 'F25B21/00'], 'TW-201925402-A': ['C09J11/04', 'C09J9/02', 'C09D11/52', 'C09D11/322', 'C09J9/02', 'C09D11/037', 'C09J11/04', 'C09D11/52', 'C09D11/322', 'C09D11/037', 'C08K3/08', 'C09J9/02', 'C09D11/037', 'C08K3/042', 'C09J11/04', 'C09D11/322', 'C09D11/52'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883']}}, 'var_functions.execute_python:20': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'sample_uc_pub_numbers': ['WO-2010045542-A3', 'KR-20110004413-A', 'AU-3353000-A', 'US-2021039104-A1', 'US-2023155090-A1', 'JP-S6163700-A', 'RO-70061-A', 'US-2006292670-A1', 'US-2003112494-A1', 'US-11014955-B2']}, 'var_functions.execute_python:22': {'uc_patents_total': 169, 'uc_unique_pub_numbers': 114}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
