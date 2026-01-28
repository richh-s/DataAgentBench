code = """import json
import re

# Load all UNIV CALIFORNIA patents from the previous query
file_path = locals().get('var_functions.query_db:5', '')
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract publication numbers for all UNIV CALIFORNIA patents
uc_pub_numbers = []
pub_number_pattern = r'pub\.|pub\. number|publication number|has pub\. number|number US-\d+[A-Z]?-\d+[A-Z]\d*'

for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Look for publication number patterns
    if 'pub. number' in patents_info:
        match = re.search(r'pub\. number\s*(\S+)', patents_info)
        if match:
            uc_pub_numbers.append(match.group(1))
    elif 'publication number' in patents_info:
        match = re.search(r'publication number\s*(\S+)', patents_info)
        if match:
            uc_pub_numbers.append(match.group(1))
    elif 'has pub.' in patents_info:
        match = re.search(r'has pub\.\s*(\S+)', patents_info)
        if match:
            uc_pub_numbers.append(match.group(1))

# Also extract from fields that might have US-XXXXX-XX format
us_pattern = r'(US-\d+[A-Z]?-\d+[A-Z]\d*)'
for patent in uc_patents:
    patents_info = patent['Patents_info']
    matches = re.findall(us_pattern, patents_info)
    uc_pub_numbers.extend(matches)

# Remove duplicates and clean
uc_pub_numbers = list(set(uc_pub_numbers))

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'uc_publication_numbers': uc_pub_numbers[:20],  # Show first 20
    'total_unique_pub_numbers': len(uc_pub_numbers)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 'Found 50 patents from UNIV CALIFORNIA', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_patents': 50, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)
