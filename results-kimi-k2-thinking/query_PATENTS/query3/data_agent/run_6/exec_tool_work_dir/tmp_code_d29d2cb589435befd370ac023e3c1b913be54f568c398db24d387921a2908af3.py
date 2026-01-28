code = """import json
import re

# Load all patent data
file_path = locals()['var_functions.query_db:28']
with open(file_path, 'r') as f:
    all_patents = json.load(f)

# Rebuild UNIV CALIFORNIA publication numbers list
univ_calif_pubs = set()
for rec in all_patents:
    patents_info = rec['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        match = re.search(r'pub\. number\s+([A-Z]{2,3}-[^,\s\]]+)', patents_info)
        if match:
            pub_num = match.group(1).rstrip('.')
            univ_calif_pubs.add(pub_num)

# Find all patents that cite UNIV CALIFORNIA patents
citing_patents = []

for rec in all_patents:
    # Skip UNIV CALIFORNIA patents themselves
    patents_info = rec['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Check citations
    citations_str = rec['citation']
    if not citations_str or citations_str == '[]':
        continue
    
    try:
        citations = json.loads(citations_str)
        for cite in citations:
            pub_num = cite.get('publication_number', '')
            if pub_num and pub_num in univ_calif_pubs:
                # Extract assignee from patent info
                assignee = None
                # Look for patterns like "is assigned to X" or "is owned by X" or "held by X"
                match = re.search(r'is assigned to\s+([^,]+)', patents_info)
                if match:
                    assignee = match.group(1).strip()
                else:
                    match = re.search(r'is owned by\s+([^,]+)', patents_info)
                    if match:
                        assignee = match.group(1).strip()
                    else:
                        match = re.search(r'held by\s+([^,]+)', patents_info)
                        if match:
                            assignee = match.group(1).strip()
                
                citing_patents.append({
                    'assignee': assignee,
                    'patent_info': patents_info,
                    'cites': pub_num,
                    'cpc_json': rec['cpc']
                })
                break
    except:
        pass

# Extract unique assignees (excluding UNIV CALIFORNIA)
assignees = set()
cpc_codes = set()

for patent in citing_patents:
    if patent['assignee'] and 'UNIV CALIFORNIA' not in patent['assignee']:
        assignees.add(patent['assignee'])
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(patent['cpc_json'])
        for cpc in cpc_list:
            cpc_codes.add(cpc['code'])
    except:
        pass

result = {
    'total_citing_patents': len(citing_patents),
    'unique_assignees': len(assignees),
    'sample_assignees': list(assignees),
    'cpc_codes_to_lookup': list(cpc_codes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}, 'var_functions.execute_python:38': {'total_cited_by_univ_calif': 1112, 'total_univ_calif_publications': 114, 'sample_univ_calif_pubs': ['US-11421276-B2.', 'EP-3668487-A4.', 'KR-20050085437-A.', 'US-2020283856-A1.', 'EP-0826155-A4.', 'WO-2021102420-A1.', 'US-2009031436-A1.', 'JP-2009260386-A.', 'US-11014955-B2.', 'PT-2970346-T.']}, 'var_functions.execute_python:42': {'total_patents': 277813, 'univ_calif_patents': 169, 'sample_pubs': ['US-2003112494-A1', 'KR-100228821-B1', 'IL-274176-A', 'US-2020025859-A1', 'US-2021000566-A1', 'US-6750960-B2', 'WO-2024112568-A1', 'AU-2015364602-B2', 'PE-20130764-A1', 'EP-3668487-A4']}, 'var_functions.execute_python:44': {'total_university_california_pubs': 114, 'citing_patents_found': 4, 'sample_citing_patent': {'patent_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'cites': 'US-6237292-B1', 'cpc': '[\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)
