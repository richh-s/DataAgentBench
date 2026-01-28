code = """import json
import re
from collections import defaultdict

# Load all data
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

# Build UC publication map with CPC codes
uc_pub_map = {}  # pub_num -> set(cpc_codes)
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', patents_info, re.IGNORECASE)
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        
        cpc_str = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str or []
        except:
            cpc_list = []
            
        cpc_codes = set()
        for entry in cpc_list:
            code = entry.get('code', '')
            if code:
                cpc_codes.add(code)
        
        uc_pub_map[pub_num] = cpc_codes

# Find all unique CPC codes from cited UC patents
all_cpc_codes = set()
citations_by_assignee = defaultdict(lambda: defaultdict(int))  # assignee -> cpc_code -> count

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    citation_str = patent.get('citation', '[]')
    
    # Extract assignee
    assignee_match = re.search(r'([A-Z][A-Z\s\.]*?(?:CO|CORP|INC|LTD|LLC|GMBH|AG|SA|BV|NV|SPA|PLC)[A-Z\s]*)', patents_info, re.IGNORECASE)
    if not assignee_match:
        continue
        
    citing_assignee = assignee_match.group(1).strip()
    
    # Skip UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    
    # Parse citation
    try:
        citations_list = json.loads(citation_str) if isinstance(citation_str, str) else citation_str or []
    except:
        continue
    
    for citation in citations_list:
        cited_pub_num = citation.get('publication_number', '')
        if cited_pub_num in uc_pub_map:
            # This patent cites a UC patent
            cpc_codes = uc_pub_map[cited_pub_num]
            for cpc_code in cpc_codes:
                all_cpc_codes.add(cpc_code)
                citations_by_assignee[citing_assignee][cpc_code] += 1

# Prepare result as list of (assignee, cpc_code, count)
result = []
for assignee, cpc_counts in citations_by_assignee.items():
    for cpc_code, count in cpc_counts.items():
        result.append({
            'assignee': assignee,
            'cpc_code': cpc_code,
            'count': count
        })

print(f"Found {len(result)} (assignee, CPC) pairs")
print(f"Total unique CPC codes to look up: {len(all_cpc_codes)}")

# Now we need to get CPC titles from the database
# Let's just return the list of CPC codes we need to look up
final_result = {
    'assignee_cpc_pairs': result,
    'all_cpc_codes': list(all_cpc_codes)
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'uc_patents_count': 169, 'all_patents_count': 277813}, 'var_functions.execute_python:22': {'uc_pub_numbers': ['CA-2298540-A1', 'US-2023321419-A1', 'US-2023155090-A1', 'WO-2012158833-A3', 'TW-201925402-A', 'EP-2210307-A4', 'EP-4284234-A1', 'US-6980295-B2', 'AU-3353000-A', 'WO-2024044766-A3'], 'citation_count': 2, 'uc_patents_with_cpc': 114}, 'var_functions.execute_python:24': {'citing_assignees': ['is held by BLOOM ENERGY CORP and has publication no', 'is owned by CRYSTAL IS INC and has publication no'], 'total_cpc_codes': 23, 'cpc_sample': ['H01L33/50', 'H01L33/0093', 'H01M4/8885', 'Y02E60/50', 'H01L33/00', 'H01L33/32', 'H01L33/30', 'H01L33/007', 'H01M4/9066', 'H01M8/1246', 'H01L33/54', 'H01M4/0419', 'Y02P70/50', 'H01L2224/16225', 'H01M4/9016', 'H01M4/9033', 'Y02E60/10', 'H01M8/1226', 'H01L33/06', 'H01M2008/1293']}}

exec(code, env_args)
