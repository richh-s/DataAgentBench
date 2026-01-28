code = """import json
import re

# Load all patent data
file_path = locals()['var_functions.query_db:28']

with open(file_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents in database:', len(all_patents))
print('First record keys:', list(all_patents[0].keys()))

# Extract UNIV CALIFORNIA publication numbers
univ_calif_pubs = set()
for rec in all_patents:
    patents_info = rec['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        match = re.search(r'pub\. number\s+([A-Z]{2}-[^,\s\]]+)', patents_info)
        if match:
            pub_num = match.group(1).rstrip('.')
            univ_calif_pubs.add(pub_num)
        else:
            match2 = re.search(r'publication number\s+([A-Z]{2}-[^,\s\]]+)', patents_info, re.IGNORECASE)
            if match2:
                pub_num = match2.group(1).rstrip('.')
                univ_calif_pubs.add(pub_num)

print('UNIV CALIFORNIA patents found:', len(univ_calif_pubs))
print('Sample:', list(univ_calif_pubs)[:10])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}, 'var_functions.execute_python:38': {'total_cited_by_univ_calif': 1112, 'total_univ_calif_publications': 114, 'sample_univ_calif_pubs': ['US-11421276-B2.', 'EP-3668487-A4.', 'KR-20050085437-A.', 'US-2020283856-A1.', 'EP-0826155-A4.', 'WO-2021102420-A1.', 'US-2009031436-A1.', 'JP-2009260386-A.', 'US-11014955-B2.', 'PT-2970346-T.']}}

exec(code, env_args)
