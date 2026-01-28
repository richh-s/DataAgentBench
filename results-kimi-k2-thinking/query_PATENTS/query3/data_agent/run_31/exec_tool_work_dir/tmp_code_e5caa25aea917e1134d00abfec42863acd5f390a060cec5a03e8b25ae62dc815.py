code = """import json
import os
import re

# Find the file containing UNIV CALIFORNIA patents
# Check the tmp directory for query_db_44.json
file_path = '/tmp/query_db_44.json'

if not os.path.exists(file_path):
    # Find all json files in /tmp
    files = [f for f in os.listdir('/tmp') if f.endswith('.json')]
    print('JSON files in /tmp:', files)
    # Look for the most recent one that might contain our data
    for f in files:
        if 'query_db' in f:
            file_path = os.path.join('/tmp', f)
            break

print('Using file:', file_path)

# Read the UNIV CALIFORNIA patents data
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

print(f'Loaded {len(uc_patents)} UNIV CALIFORNIA patents')

# Extract publication numbers from Patents_info
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)
    else:
        # Alternative pattern: look for publication numbers in various formats
        match2 = re.search(r'([A-Z]{2}-\d+-[A-Z]\d*)', patents_info)
        if match2:
            uc_pub_numbers.append(match2.group(1))

print(f'Extracted {len(uc_pub_numbers)} publication numbers from UNIV CALIFORNIA patents')
print('Sample publication numbers:', uc_pub_numbers[:10])

# Now we need to find all patents that cite these UNIV CALIFORNIA patents
# This is a large query, so let's first check the total number of patents
total_patents = 277813  # From previous query

# We'll query in batches or use a more targeted approach
# First, save the publication numbers to a file for reference
with open('/tmp/uc_pub_numbers.json', 'w') as f:
    json.dump(uc_pub_numbers, f)

print('Saved publication numbers to /tmp/uc_pub_numbers.json')

# Return the publication numbers as a compact list
result = {'uc_patents_count': len(uc_patents), 'uc_pub_numbers_count': len(uc_pub_numbers), 'sample_numbers': uc_pub_numbers[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation': '[]', 'cpc': '[\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J2463/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:8': [{'total': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': {'status': 'ready', 'files': ['/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Universal', '/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Etc/Universal', '/usr/local/lib/python3.12/site-packages/tzdata/zoneinfo/Universal']}, 'var_functions.query_db:42': [{'total': '169'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
