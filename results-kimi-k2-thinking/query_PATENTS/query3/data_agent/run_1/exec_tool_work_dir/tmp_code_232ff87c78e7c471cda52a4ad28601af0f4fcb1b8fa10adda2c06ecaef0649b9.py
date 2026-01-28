code = """import json
import re
from collections import defaultdict

# Load the full publication database
full_db_path = locals()['var_functions.query_db:30']

# Read the data in chunks to avoid memory issues
citing_assignees = defaultdict(set)
uc_pub_numbers = set()

# First, let's identify all UNIV CALIFORNIA patents and their publication numbers
print('Reading full database to find UNIV CALIFORNIA patents...')

with open(full_db_path, 'r') as f:
    patents_data = json.load(f)

print(f'Total patents in database: {len(patents_data)}')

# Extract UC patents and their publication numbers
uc_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        uc_patents.append(patent)
        # Extract publication number
        pub_match = re.search(r'pub[\.\s]*number[\s:]+([A-Z0-9-]+[A-Z0-9])', patents_info)
        if pub_match:
            uc_pub_numbers.add(pub_match.group(1))

print(f'Found {len(uc_patents)} UNIV CALIFORNIA patents')
print(f'Found {len(uc_pub_numbers)} unique UC publication numbers: {list(uc_pub_numbers)}')

# Now find all patents that cite these UC patents (excluding UNIV CALIFORNIA itself)
citing_patents = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    
    # Skip if this is a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Check citations
    citation_text = patent.get('citation', '')
    if citation_text and citation_text != '[]':
        try:
            citations = json.loads(citation_text)
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub in uc_pub_numbers:
                    citing_patents.append(patent)
                    # Extract assignee from Patents_info
                    assignee_match = re.search(r'^([A-Z][A-Z\s&\-]+) holds', patents_info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                        citing_assignees[assignee].add(cited_pub)
        except:
            continue

print(f'Found {len(citing_patents)} patents that cite UNIV CALIFORNIA patents')
print(f'Found {len(citing_assignees)} unique citing assignees')

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers': list(uc_pub_numbers),
    'citing_patents_count': len(citing_patents),
    'citing_assignees_count': len(citing_assignees),
    'top_citing_assignees': list(citing_assignees.items())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_patents': 5, 'uc_patents': 10, 'sample_structure': ['Patents_info', 'cpc', 'citation'], 'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.execute_python:12': {'uc_patents_count': 10, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.execute_python:16': {'uc_patents_analyzed': 10, 'uc_pub_numbers_found': 5, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}, 'var_functions.execute_python:20': {'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1'], 'count': 5}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'uc_pub_numbers': ['TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2022074631-A1', 'US-2017281687-A1'], 'count': 5}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
