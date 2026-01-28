code = """import json
import re

# Load UNIV CALIFORNIA data
var_name = 'var_functions.query_db:10'
result_file = locals().get(var_name)
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_data = json.load(f)
else:
    uc_data = result_file

# Build set of UC publication numbers
uc_pub_numbers = set()
for record in uc_data:
    patents_info = record['Patents_info']
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

# Load all patent data
var_name_all = 'var_functions.query_db:24'
result_file_all = locals().get(var_name_all)
if isinstance(result_file_all, str) and result_file_all.endswith('.json'):
    with open(result_file_all, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = result_file_all

# Extract citing relationships with better assignee detection
citing_relationships = []

def extract_assignee(patents_info):
    # Pattern 1: "ASSIGNEE holds the US patent"
    match = re.search(r'^([A-Z\s&\.,-]+?)\s+(?:holds|has)\s+(?:the\s+)?[A-Z]{2}\s+patent', patents_info)
    if match:
        return match.group(1).strip()
    
    # Pattern 2: "owned by ASSIGNEE"
    match = re.search(r'owned by\s+([A-Z\s&\.,-]+?)(?: and has|,)\s+', patents_info)
    if match:
        return match.group(1).strip()
    
    # Pattern 3: "assigned to ASSIGNEE"
    match = re.search(r'assigned to\s+([A-Z\s&\.,-]+?)(?: and has|,)\s+', patents_info)
    if match:
        return match.group(1).strip()
    
    # Pattern 4: extract from start until first verb
    match = re.search(r'^([A-Z\s&\.,-]+?)\s+(?:holds|owns|assigned|is assigned)', patents_info)
    if match:
        return match.group(1).strip()
    
    return None

sample_processed = []
for i, record in enumerate(all_patents[:10000]):  # Process first 10k to test
    patents_info = record['Patents_info']
    assignee = extract_assignee(patents_info)
    
    if assignee and 'UNIV CALIFORNIA' not in assignee:
        if record['citation']:
            try:
                citations = json.loads(record['citation'])
                for citation in citations:
                    cited_pub = citation.get('publication_number', '')
                    if cited_pub and cited_pub in uc_pub_numbers:
                        citing_relationships.append({
                            'citing_assignee': assignee,
                            'cited_uc_patent': cited_pub,
                            'patents_info': patents_info[:100]  # Truncate for sample
                        })
            except:
                pass

print('__RESULT__:')
print(json.dumps({
    'relationships_found': len(citing_relationships),
    'sample_relationships': citing_relationships[:10],
    'assignee_examples': list(set(r['citing_assignee'] for r in citing_relationships))[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_records': 169, 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_count': 4, 'cpc_count': 9}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_count': 0, 'cpc_count': 37}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_count': 120, 'cpc_count': 15}]}, 'var_functions.query_db:14': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:16': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:18': {'uc_patents_found': 114, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00', 'F25B21/00', 'F28D15/00', 'F25B21/00'], 'TW-201925402-A': ['C09J11/04', 'C09J9/02', 'C09D11/52', 'C09D11/322', 'C09J9/02', 'C09D11/037', 'C09J11/04', 'C09D11/52', 'C09D11/322', 'C09D11/037', 'C08K3/08', 'C09J9/02', 'C09D11/037', 'C08K3/042', 'C09J11/04', 'C09D11/322', 'C09D11/52'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883']}}, 'var_functions.execute_python:20': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'sample_uc_pub_numbers': ['WO-2010045542-A3', 'KR-20110004413-A', 'AU-3353000-A', 'US-2021039104-A1', 'US-2023155090-A1', 'JP-S6163700-A', 'RO-70061-A', 'US-2006292670-A1', 'US-2003112494-A1', 'US-11014955-B2']}, 'var_functions.execute_python:22': {'uc_patents_total': 169, 'uc_unique_pub_numbers': 114}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_relationships': 1, 'unique_citing_assignees': 1, 'unique_cited_uc_patents': 1, 'sample_relationships': [{'citing_assignee': 'SCHOWALTER LEO J', 'cited_uc_patent': 'US-2010025717-A1', 'cpc_codes': ['H01L33/0093', 'H01L33/007', 'H01L33/0093', 'H01L33/007', 'H01L33/22', 'H01L33/32', 'H01L33/60', 'H01L33/22', 'H01L33/32', 'H01L33/30']}]}, 'var_functions.execute_python:28': {'total_patents_loaded': 277813, 'sample_patent_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'sample_citation': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}}

exec(code, env_args)
