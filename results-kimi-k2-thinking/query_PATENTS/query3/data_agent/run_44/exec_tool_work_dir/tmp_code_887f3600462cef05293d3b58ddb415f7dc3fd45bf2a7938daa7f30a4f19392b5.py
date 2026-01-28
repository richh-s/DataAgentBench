code = """import json
import re

# Load UNIV CALIFORNIA patents and extract their publication numbers
uc_file = locals().get('var_functions.query_db:30')
with open(uc_file) as f:
    uc_data = json.load(f)

uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    # Extract publication numbers like US-2022074631-A1
    matches = re.findall(r'\b[A-Z]{2}-\d{6,12}-[A-Z]\d?\b', info)
    uc_pub_numbers.update(matches)

# Load non-UNIV CALIFORNIA patents data
nonuc_file = locals().get('var_functions.query_db:28')
with open(nonuc_file) as f:
    nonuc_data = json.load(f)

# Find patents that cite UNIV CALIFORNIA patents
citing_patents = []
for record in nonuc_data:
    # Get assignee from Patents_info
    info = record.get('Patents_info', '')
    assignee_match = re.search(r'^([^,]+)', info)
    assignee = assignee_match.group(1) if assignee_match else 'Unknown'
    
    # Skip if it's still UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in assignee.upper() or 'UNIVERSITY OF CALIFORNIA' in assignee.upper():
        continue
    
    # Check citations
    citations = record.get('citation', '[]')
    try:
        citation_list = json.loads(citations) if citations else []
    except:
        citation_list = []
    
    # Check if any citation is a UNIV CALIFORNIA patent
    cites_uc = False
    cited_uc_numbers = []
    for citation in citation_list:
        pub_num = citation.get('publication_number')
        if pub_num and pub_num in uc_pub_numbers:
            cites_uc = True
            cited_uc_numbers.append(pub_num)
    
    if cites_uc:
        citing_patents.append({
            'assignee': assignee,
            'patent_info': info,
            'cited_uc_numbers': cited_uc_numbers,
            'cpc': record.get('cpc', '[]')
        })

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_data),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'nonuc_patents_checked': len(nonuc_data),
    'citing_patents_found': len(citing_patents),
    'sample_citations': citing_patents[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}, 'var_functions.execute_python:26': {'uc_patents_count': 169, 'uc_pub_numbers_count': 322, 'nonuc_patents_checked': 1000, 'citing_patents_found': 0}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_patents': 169, 'uc_pub_numbers': 322, 'sample_numbers': ['US-6980295-B2', 'US-201515329526-A', 'CN-200380105631-A', 'US-37750473-A', 'US-58729205-A', 'US-11607427-B2', 'US-2017031596-W', 'US-6750960-B2', 'KR-20087016723-A', 'IL-236725-A']}}

exec(code, env_args)
