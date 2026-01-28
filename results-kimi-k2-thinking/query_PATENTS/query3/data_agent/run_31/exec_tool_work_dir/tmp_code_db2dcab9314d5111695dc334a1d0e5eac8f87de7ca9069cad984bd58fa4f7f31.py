code = """import json
import re
import os

# Read the UNIV CALIFORNIA patents data
uc_data = var_functions.query_db:44

# Extract publication numbers and CPC codes from UC patents
uc_pub_numbers = []
uc_cpc_codes = {}

for patent in uc_data:
    patents_info = patent['Patents_info']
    cpc_data = patent.get('cpc', '[]')
    
    # Extract publication number
    match = re.search(r'(?:pub\. number|publication number|publication no\.)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)
        
        # Extract CPC codes for this patent
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                codes = [item['code'] for item in cpc_list if 'code' in item]
                uc_cpc_codes[pub_num] = codes
            except:
                uc_cpc_codes[pub_num] = []
        else:
            uc_cpc_codes[pub_num] = []

print('UNIV CALIFORNIA publication numbers extracted:', len(uc_pub_numbers))
print('Sample publication numbers:', uc_pub_numbers[:10])

# Save the publication numbers to a file for the next step
with open('/tmp/uc_pub_numbers.json', 'w') as f:
    json.dump(uc_pub_numbers, f)

result = {
    'uc_patents_count': len(uc_data),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_pub_numbers': uc_pub_numbers[:10],
    'cpc_codes_sample': {k: uc_cpc_codes.get(k, []) for k in uc_pub_numbers[:3]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation': '[]', 'cpc': '[\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J2463/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:8': [{'total': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': {'status': 'ready', 'files': ['/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Universal', '/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Etc/Universal', '/usr/local/lib/python3.12/site-packages/tzdata/zoneinfo/Universal']}, 'var_functions.query_db:42': [{'total': '169'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}]}

exec(code, env_args)
