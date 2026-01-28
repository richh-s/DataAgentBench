code = """import json
import re
from collections import defaultdict

# Load data
cal_pats_file = 'file_storage/functions.query_db:80.json'
all_patents_file = 'file_storage/functions.query_db:74.json'

with open(cal_pats_file, 'r') as f:
    cal_pats = json.load(f)

with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Extract California publication numbers
cal_pub_numbers = set()
for patent in cal_pats:
    patents_info = patent['Patents_info']
    
    # Extract publication number with multiple patterns
    pub_num = None
    for pattern in [r'pub\. number ([A-Z0-9-]+)', r'publication number ([A-Z0-9-]+)', r'publication no\. ([A-Z0-9-]+)']:
        match = re.search(pattern, patents_info)
        if match:
            pub_num = match.group(1)
            break
    
    if pub_num:
        cal_pub_numbers.add(pub_num)

# Extract CPC codes for California patents (up to subclass level)
cal_pub_cpc = {}
for patent in cal_pats:
    patents_info = patent['Patents_info']
    
    pub_num = None
    for pattern in [r'pub\. number ([A-Z0-9-]+)', r'publication number ([A-Z0-9-]+)', r'publication no\. ([A-Z0-9-]+)']:
        match = re.search(pattern, patents_info)
        if match:
            pub_num = match.group(1)
            break
    
    if pub_num and 'cpc' in patent and patent['cpc']:
        try:
            cpc_data = json.loads(patent['cpc'])
            primary_cpcs = []
            for cpc in cpc_data:
                if cpc.get('inventive', False):
                    code = cpc['code']
                    # Get up to subclass (before slash)
                    subclass = code.split('/')[0] if '/' in code else code[:4]
                    primary_cpcs.append(subclass)
            # Deduplicate
            cal_pub_cpc[pub_num] = list(dict.fromkeys(primary_cpcs))
        except:
            cal_pub_cpc[pub_num] = []

# Find citing patents and assignees
citations_by_assignee = defaultdict(list)  # assignee -> list of (cal_pub, cpc_codes)
citations_found = 0

for patent in all_patents[:5000]:  # Process first 5000 to start
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        continue
    
    # Extract assignee
    assignee_match = re.search(r'^([A-Z][A-Z\s&\-]+?)\s+(holds|hold the|assigned to|is owned by|from US, owned by|from WO, assigned to|from CA, assigned to|from JP, assigned to|from KR, assigned to|from AU, owned by)', patent['Patents_info'])
    if not assignee_match:
        assignee_match = re.search(r'^([A-Z][A-Z\s&\-]+?)\s+', patent['Patents_info'])
    
    if assignee_match:
        assignee = assignee_match.group(1).strip()
    else:
        continue
    
    # Check citations
    if patent.get('citation'):
        try:
            citations = json.loads(patent['citation'])
            for cit in citations:
                cit_pub = cit.get('publication_number', '')
                if cit_pub in cal_pub_numbers:
                    cpc_codes = cal_pub_cpc.get(cit_pub, [])
                    citations_by_assignee[assignee].append({
                        'cited_cal_pub': cit_pub,
                        'cpc_codes': cpc_codes
                    })
                    citations_found += 1
                    break  # Only count one citation per patent
        except:
            pass

result = {
    'citations_found': citations_found,
    'unique_assignees': len(citations_by_assignee),
    'top_assignees': dict(list(citations_by_assignee.items())[:10])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'name': 'publicationinfo'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'Found the file path variable', 'var_functions.query_db:32': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'titleFull': 'Hand tools'}, {'symbol': 'A01B1/02', 'titleFull': 'Spades; Shovels'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': 'File path retrieved: file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': 'Loaded 169 California patents', 'var_functions.execute_python:44': 'Total California patents loaded: 169', 'var_functions.execute_python:46': "Found 59 California publication numbers: ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']...", 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': 'Total patents to analyze: 5000', 'var_functions.execute_python:58': 'Loaded 169 California patents and 5000 total patents', 'var_functions.execute_python:60': 'Found 59 California publication numbers', 'var_functions.execute_python:62': 'Found 0 citing patents from 5000 records', 'var_functions.execute_python:64': 'Found 169 California publication numbers', 'var_functions.execute_python:68': {'cal_pub_numbers_count': 59, 'cpc_mapping_count': 0, 'sample_cpc': []}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:71': {'total_cal_pubs': 169, 'total_with_cpc': 169, 'sample_entries': [['US-2022074631-A1', ['F25B21/00', 'F28D15/00', 'F25B21/00']], ['TW-201925402-A', ['C09J11/04', 'C09J9/02', 'C09D11/52']], ['US-11421276-B2', ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883']], ['AU-2019275518-B2', ['A61K31/357', 'A61K31/34', 'A61K31/08']], ['US-2017194630-A1', ['H01M10/0525', 'H01M4/386', 'H01M4/0469']]]}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.execute_python:76': {'total_cal_pubs': 169, 'total_with_cpc': 169, 'sample': {'US-2022074631-A1': ['F25B21', 'F28D15'], 'TW-201925402-A': ['C09J11', 'C09J9', 'C09D11', 'C08K3'], 'US-11421276-B2': ['C12Q1'], 'AU-2019275518-B2': ['A61K31', 'A61D7', 'A61P43', 'A61P25', 'A61P23'], 'US-2017194630-A1': ['H01M10', 'H01M4']}}, 'var_functions.execute_python:78': 'California publication numbers: 169', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.execute_python:82': {'total_california_pubs': 169, 'sample_cpc_mapping': [['US-2022074631-A1', ['F25B21', 'F28D15']], ['TW-201925402-A', ['C09J11', 'C09J9', 'C09D11', 'C08K3']], ['US-11421276-B2', ['C12Q1']], ['AU-2019275518-B2', ['A61K31', 'A61D7', 'A61P43', 'A61P25', 'A61P23', 'A61K9', 'A61M16', 'A61P11']], ['US-2017194630-A1', ['H01M10', 'H01M4']]]}, 'var_functions.execute_python:84': {'total_citations_found': 0, 'citing_assignees': 0, 'sample_citations': {}}, 'var_functions.query_db:86': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:88': 'Loaded 169 California patents and 10000 total patents'}

exec(code, env_args)
