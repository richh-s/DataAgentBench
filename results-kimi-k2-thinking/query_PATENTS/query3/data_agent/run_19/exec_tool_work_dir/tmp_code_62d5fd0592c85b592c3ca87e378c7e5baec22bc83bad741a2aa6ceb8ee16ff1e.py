code = """import json
import re
from collections import defaultdict

# Load all publications
file_path = str(locals()['var_functions.query_db:24'])
with open(file_path, 'r') as f:
    all_publications = json.load(f)

# Load UNIV CALIFORNIA publications
uc_file_path = str(locals()['var_functions.query_db:16'])
with open(uc_file_path, 'r') as f:
    uc_publications = json.load(f)

# Extract UNIV CALIFORNIA publication numbers and their CPC codes
uc_pub_info = {}  # {pub_number: cpc_codes}
for pub in uc_publications:
    patents_info = pub['Patents_info']
    # Extract publication number
    pub_num_match = re.search(r'pub\. number ([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_num_match:
        pub_number = pub_num_match.group(1)
        # Parse CPC codes
        cpc_data = json.loads(pub['cpc']) if pub['cpc'] else []
        cpc_codes = [item['code'] for item in cpc_data if item.get('code')]
        uc_pub_info[pub_number] = cpc_codes

# Find patents that cite UNIV CALIFORNIA patents and extract assignees
assignee_citations = defaultdict(lambda: defaultdict(list))  # {assignee: {uc_pub_number: [cpc_codes]}}

for pub in all_publications:
    patents_info = pub['Patents_info']
    
    # Extract assignee from Patents_info
    # Pattern 1: "ASSIGNEE holds the ..."
    assignee_match = re.search(r'^(.+?) holds the', patents_info)
    if not assignee_match:
        # Pattern 2: "is owned by ASSIGNEE"
        assignee_match = re.search(r'is owned by (.+?)(?: and|$)', patents_info)
    if not assignee_match:
        # Pattern 3: "is assigned to ASSIGNEE"
        assignee_match = re.search(r'is assigned to (.+?)(?: and|$)', patents_info)
    
    if assignee_match:
        assignee = assignee_match.group(1).strip()
        # Skip UNIV CALIFORNIA
        if 'UNIV CALIFORNIA' in assignee:
            continue
    else:
        continue
    
    # Parse citations
    if pub['citation']:
        try:
            citations = json.loads(pub['citation'])
            for citation in citations:
                cited_pub_num = citation.get('publication_number')
                if cited_pub_num and cited_pub_num in uc_pub_info:
                    # This patent cites a UNIV CALIFORNIA patent
                    cpc_codes = uc_pub_info[cited_pub_num]
                    assignee_citations[assignee][cited_pub_num].extend(cpc_codes)
        except:
            continue

# Deduplicate CPC codes
for assignee in assignee_citations:
    for pub_num in assignee_citations[assignee]:
        assignee_citations[assignee][pub_num] = list(set(assignee_citations[assignee][pub_num]))

print('__RESULT__:')
print(json.dumps({
    'total_citing_assignees': len(assignee_citations),
    'citing_assignees_sample': list(assignee_citations.keys())[:10],
    'uc_patents_cited': len(uc_pub_info)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_records': 169, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': '2022, March 10th'}}, 'var_functions.query_db:22': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_uc_patents': 169, 'uc_pub_numbers_sample': ['US-2006292670-A1', 'US-2019328740-A1', 'US-2023279470-A1', 'AU-2010214112-B2', 'US-2017145219-A1', 'AU-2019275518-B2', 'CN-102067370-B', 'US-6767662-B2', 'AU-2015364602-B2', 'CN-102584712-A']}}

exec(code, env_args)
