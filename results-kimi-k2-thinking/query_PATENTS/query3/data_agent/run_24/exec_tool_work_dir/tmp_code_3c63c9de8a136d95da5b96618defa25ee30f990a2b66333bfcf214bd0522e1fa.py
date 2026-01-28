code = """import json
import re

# Load the results from previous step
with open('file_storage/functions.execute_python:36.json', 'r') as f:
    results = json.load(f)

citing_patents = results.get('sample_citing_patent', [])

# If we only have one sample, let's get all citing patents
if not isinstance(citing_patents, list):
    # Re-run the analysis to get all citing patents
    with open('file_storage/functions.query_db:24.json', 'r') as f:
        uc_patents = json.load(f)
    
    # Extract publication numbers from UNIV CALIFORNIA patents
    uc_pub_numbers = set()
    for patent in uc_patents:
        patents_info = patent.get('Patents_info', '')
        pub_matches = re.findall(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', patents_info)
        for match in pub_matches:
            uc_pub_numbers.add(match)
    
    with open('file_storage/functions.query_db:30.json', 'r') as f:
        all_patents = json.load(f)
    
    citing_patents = []
    for patent in all_patents:
        if 'UNIV CALIFORNIA' in patent.get('Patents_info', ''):
            continue
        
        citations_str = patent.get('citation', '[]')
        try:
            citations = json.loads(citations_str) if citations_str else []
        except:
            continue
        
        for citation in citations:
            cited_pub = citation.get('publication_number', '')
            if cited_pub and cited_pub in uc_pub_numbers:
                citing_patents.append({
                    'patent_info': patent.get('Patents_info', ''),
                    'cited_uc_patent': cited_pub,
                    'cpc_codes': patent.get('cpc', '[]')
                })
                break

# Extract assignees and CPC codes
assignee_cpc_map = {}
for patent in citing_patents:
    # Extract assignee from patent_info
    patent_info = patent['patent_info']
    # Look for assignee patterns
    assignee_match = re.search(r'is assigned to ([A-Z\s\.&-]+) and has', patent_info)
    if not assignee_match:
        assignee_match = re.search(r'is owned by ([A-Z\s\.&-]+) and has', patent_info)
    if not assignee_match:
        assignee_match = re.search(r'assigned to ([A-Z\s\.&-]+)', patent_info)
    if not assignee_match:
        assignee_match = re.search(r'by ([A-Z\s\.&-]+) holds', patent_info)
    
    if assignee_match:
        assignee = assignee_match.group(1).strip()
        # Skip UNIV CALIFORNIA
        if 'UNIV CALIFORNIA' in assignee:
            continue
            
        # Parse CPC codes
        cpc_str = patent.get('cpc_codes', '[]')
        try:
            cpc_list = json.loads(cpc_str) if cpc_str else []
            cpc_codes = [cpc['code'] for cpc in cpc_list if isinstance(cpc, dict) and 'code' in cpc]
            
            if assignee not in assignee_cpc_map:
                assignee_cpc_map[assignee] = set()
            assignee_cpc_map[assignee].update(cpc_codes)
        except:
            continue

print('__RESULT__:')
print(json.dumps({
    'total_citing_assignees': len(assignee_cpc_map),
    'assignees': list(assignee_cpc_map.keys()),
    'assignee_cpc_map': {k: list(v) for k, v in assignee_cpc_map.items()}
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.execute_python:20': {'type': "<class 'str'>", 'length': 38, 'is_list': False}, 'var_functions.execute_python:22': {'total_records': 3, 'first_record_keys': ['Patents_info', 'citation', 'cpc'], 'sample_patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'sample_citation_first_200': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n ', 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_uc_patents': 169, 'sample_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:28': {'total_uc_patents': 169, 'found_pub_numbers': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_uc_patents': 169, 'unique_pub_numbers_found': 194, 'sample_pub_numbers': ['TW-107142982-A', 'US-68078803-A', 'US-11607427-B2', 'US-2022018060-A1', 'US-2019021660-W', 'US-2018304537-A1', 'US-11421276-B2', 'US-2022016812-W', 'US-10359432-B2', 'US-4541105-A', 'AU-2003247814-A1', 'US-2017015812-W', 'US-2006292670-A1', 'AU-5938296-A', 'US-2018243924-A1', 'US-2022123166-A1', 'US-6030830-A', 'US-10900049-B2', 'US-60880790-A', 'AU-2008329628-A']}, 'var_functions.execute_python:36': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'total_all_patents': 277813, 'citing_patents_found': 4, 'sample_citing_patent': {'patent_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'cited_uc_patent': 'US-6237292-B1', 'cpc_codes': '[\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)
