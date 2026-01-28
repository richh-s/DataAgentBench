code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load data again
uc_patents_key = 'var_functions.query_db:14'
uc_patents_data = locals().get(uc_patents_key)
uc_patents = []
if isinstance(uc_patents_data, str) and uc_patents_data.endswith('.json'):
    with open(uc_patents_data, 'r') as f:
        uc_patents = json.load(f)
elif isinstance(uc_patents_data, list):
    uc_patents = uc_patents_data

all_patents_key = 'var_functions.query_db:12'
all_patents_data = locals().get(all_patents_key)
all_patents = []
if isinstance(all_patents_data, str) and all_patents_data.endswith('.json'):
    with open(all_patents_data, 'r') as f:
        all_patents = json.load(f)
elif isinstance(all_patents_data, list):
    all_patents = all_patents_data

# Build mapping of publication numbers to UC patents
uc_pub_map = {}
uc_pub_numbers = set()

for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', patents_info, re.IGNORECASE)
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        uc_pub_numbers.add(pub_num)
        uc_pub_map[pub_num] = {
            'patent': patent,
            'cpc_codes': set()
        }
        
        # Extract CPC codes for this UC patent
        cpc_str = patent.get('cpc', '[]')
        try:
            if isinstance(cpc_str, str):
                cpc_list = json.loads(cpc_str)
            else:
                cpc_list = cpc_str or []
        except:
            cpc_list = []
            
        for cpc_entry in cpc_list:
            cpc_code = cpc_entry.get('code', '')
            if cpc_code:
                uc_pub_map[pub_num]['cpc_codes'].add(cpc_code)

# Find citations and collect all CPC codes from cited patents
all_cpc_codes = set()
citations_by_assignee = defaultdict(lambda: defaultdict(int))  # assignee -> cpc_code -> count

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    citation_str = patent.get('citation', '[]')
    
    # Extract assignee
    assignee_match = re.search(r'([A-Z][A-Z\s\.]*(?:CO|CORP|INC|LTD|LLC|GMBH|AG|SA|BV|NV|SPA|PLC)[A-Z\s]*)', patents_info, re.IGNORECASE)
    if not assignee_match:
        continue
        
    citing_assignee = assignee_match.group(1).strip()
    
    # Skip UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    
    # Parse citation
    try:
        if isinstance(citation_str, str):
            citations_list = json.loads(citation_str)
        else:
            citations_list = citation_str or []
    except:
        continue
    
    for citation in citations_list:
        cited_pub_num = citation.get('publication_number', '')
        if cited_pub_num in uc_pub_map:
            # This patent cites a UC patent
            cpc_codes = uc_pub_map[cited_pub_num]['cpc_codes']
            for cpc_code in cpc_codes:
                all_cpc_codes.add(cpc_code)
                citations_by_assignee[citing_assignee][cpc_code] += 1

# Get sample of CPC codes to check in database
cpc_sample = list(all_cpc_codes)[:20] if all_cpc_codes else []

result = {
    'citing_assignees': list(citations_by_assignee.keys()),
    'total_cpc_codes': len(all_cpc_codes),
    'cpc_sample': cpc_sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'uc_patents_count': 169, 'all_patents_count': 277813}, 'var_functions.execute_python:22': {'uc_pub_numbers': ['CA-2298540-A1', 'US-2023321419-A1', 'US-2023155090-A1', 'WO-2012158833-A3', 'TW-201925402-A', 'EP-2210307-A4', 'EP-4284234-A1', 'US-6980295-B2', 'AU-3353000-A', 'WO-2024044766-A3'], 'citation_count': 2, 'uc_patents_with_cpc': 114}}

exec(code, env_args)
