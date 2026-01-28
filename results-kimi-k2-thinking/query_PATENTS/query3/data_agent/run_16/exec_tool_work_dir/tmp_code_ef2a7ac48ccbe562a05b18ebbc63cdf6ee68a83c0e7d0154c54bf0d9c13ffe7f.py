code = """import json
import re

# Step 1: Extract all UC publication numbers
uc_file_key = 'var_functions.query_db:28'
uc_file_path = locals()[uc_file_key]

with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC publication numbers from Patents_info
uc_pub_numbers = []
for patent in uc_patents:
    info = patent['Patents_info']
    # Extract all publication-like numbers and take the last one
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', info)
    if matches:
        uc_pub_numbers.append(matches[-1])

print('Extracted UC publication numbers:', len(uc_pub_numbers))
print('Examples:', uc_pub_numbers[:10])

# Create a pattern for SQL LIKE queries looking for citations
# We'll build a query that searches for each UC publication number individually
total_citing_patents = []
citing_assignees = set()

result = {
    'uc_patents': len(uc_pub_numbers),
    'uc_pub_numbers': uc_pub_numbers[:20]  # Save first 20 for debugging
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_patents': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'uc_patents_count': 169, 'uc_pub_numbers_count': 169, 'first_10_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1']}, 'var_functions.query_db:34': [], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}], 'var_functions.query_db:40': [{'Patents_info': 'In US, the application (ID US-202117502422-A) is belonging to APPLE INC and has publication no. US-2022110100-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2012039285-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-8565254-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015189633-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2019215098-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2019254025-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-10448389-B1",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "H04W72/23",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L25/0204",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/0053",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/11",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/27",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04W24/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W24/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W72/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/11",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/27",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:42': [], 'var_functions.query_db:44': [], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': {'citing_patents_count': 0, 'uc_patents_count': 169}, 'var_functions.execute_python:52': {'next_step': 'Fetch all patents with citations and identify those citing UC patents', 'uc_patent_count': 169}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
