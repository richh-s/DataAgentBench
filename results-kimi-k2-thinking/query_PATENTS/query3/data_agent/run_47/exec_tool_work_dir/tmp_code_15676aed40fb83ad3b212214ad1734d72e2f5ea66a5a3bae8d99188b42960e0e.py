code = """import json
import re

# Load UNIV CALIFORNIA patents
california_patents_path = locals()['var_functions.query_db:14']
with open(california_patents_path, 'r') as f:
    california_patents = json.load(f)

# Parse patents info to extract publication numbers for California patents
california_pub_nums = []
for patent in california_patents:
    patents_info = patent['Patents_info']
    # Look for publication number patterns like US-2022074631-A1
    pub_num_match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_num_match:
        california_pub_nums.append(pub_num_match.group(1))

print('__RESULT__:')
print(json.dumps({
    'total_california_patents': len(california_patents),
    'extracted_publication_numbers': california_pub_nums[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_california_patents': 169, 'sample_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ', 'sample_cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "'}, 'var_functions.query_db:20': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}]}

exec(code, env_args)
