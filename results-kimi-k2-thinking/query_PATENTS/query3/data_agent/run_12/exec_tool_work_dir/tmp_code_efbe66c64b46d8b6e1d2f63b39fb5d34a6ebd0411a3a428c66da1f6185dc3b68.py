code = """import json

# Read the UC patents data
file_path = 'file_storage/functions.query_db:5.json'
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

print(f'Total UC patents: {len(uc_patents)}')

# Extract publication numbers from UC patents (the ones being cited)
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Extract publication number from the text
    # Looking for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    import re
    pub_match = re.search(r'(?:pub|publication)(?:\s+number)?\s+([A-Z]{2}-[\dA-Z-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        uc_pub_numbers.append(pub_match.group(1))

print(f'Extracted {len(uc_pub_numbers)} UC publication numbers')
print('Sample UC publication numbers:', uc_pub_numbers[:10])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'name': 'publicationinfo'}], 'var_functions.execute_python:10': 'File path: file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': [{'index': 0, 'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ...', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "...'}, {'index': 1, 'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation': '[]...', 'cpc': '[\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"...'}, {'index': 2, 'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",...', 'cpc': '[\n  {\n    "code": "Y02A50/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code...'}, {'index': 3, 'patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "ABU-AWWAD, F. M. \\"A QSAR STUDY of the Activity of Some Fluorinated Anesthetics\\" Der Pharma Chemica (...', 'cpc': '[\n  {\n    "code": "A61K31/357",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K31/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"...'}, {'index': 4, 'patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'citation': '[]...', 'cpc': '[\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "cod...'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
