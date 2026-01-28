code = """import json
import re
import os

# Load all UNIV CALIFORNIA patents
uc_file = locals().get('var_functions.query_db:5', '')
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Extract publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = set()

for patent in uc_patents:
    patents_info = patent['Patents_info']
    
    # Pattern to match publication numbers in various formats
    # Look for patterns like: pub. number XXXXX, publication number XXXXX, has pub. XXXXX
    patterns = [
        r'pub\. number\s*([A-Z]{2}-\d+[A-Z]?-\d+[A-Z]\d*)',
        r'publication number\s*([A-Z]{2}-\d+[A-Z]?-\d+[A-Z]\d*)',
        r'has pub\.\s*([A-Z]{2}-\d+[A-Z]?-\d+[A-Z]\d*)',
        r'pub\. number\s*([A-Z]{2}-\d+-\d+)',
        r'with pub\. number\s*([A-Z]{2}-\d+-\d+)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, patents_info, re.IGNORECASE)
        uc_pub_numbers.update(matches)
    
    # Also look for any US-, EP-, WO-, etc. patterns in the text
    general_pattern = r'\b([A-Z]{2}-\d+[A-Z]?-\d+[A-Z]\d*)\b'
    matches = re.findall(general_pattern, patents_info)
    uc_pub_numbers.update(matches)

# Clean up any trailing punctuation
uc_pub_numbers = {num.rstrip('.') for num in uc_pub_numbers}

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'uc_publication_numbers': sorted(list(uc_pub_numbers)),
    'count': len(uc_pub_numbers)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 'Found 50 patents from UNIV CALIFORNIA', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_patents': 50, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:16': {'total_uc_patents': 50, 'uc_publication_numbers': ['AU-2005269556-A1.', 'US-2020283856-A1.', 'US-2017281687-A1.', 'KR-20050085437-A.', 'EP-0826155-A4.', 'CN-103189548-A.', 'US-2021002329-A1.', 'WO-2017136335-A1.', 'AU-2019275518-B2.', 'US-2022074631-A1.', 'PT-2970346-T.', 'KR-20160119166-A.', 'US-7745569-B2.', 'AU-2898989-A.', 'KR-20200041324-A.', 'US-2006051790-A1.', 'US-2017145219-A1.', 'US-6237292-B1.', 'WO-2012162563-A2.', 'US-9061071-B2.'], 'total_unique_pub_numbers': 36}, 'var_functions.list_db:18': ['cpc_definition'], 'var_functions.execute_python:20': 'Preparing to search for citing patents...', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
