code = """import json
import re

# Get the UNIV CALIFORNIA patents from the storage variable
uc_patents = locals()['var_functions.query_db:44']

print(f"Loaded {len(uc_patents)} UNIV CALIFORNIA patents from storage")

# Extract publication numbers from Patents_info
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)

print(f'Extracted {len(uc_pub_numbers)} publication numbers from UNIV CALIFORNIA patents')
print('Sample publication numbers:', uc_pub_numbers[:10])

# Extract all citations from UC patents
cited_patents = []
for patent in uc_patents:
    citation_str = patent.get('citation', '[]')
    if citation_str and len(citation_str) > 2:
        try:
            citations = json.loads(citation_str)
            for cit in citations:
                pub_num = cit.get('publication_number')
                if pub_num:
                    cited_patents.append(pub_num)
        except:
            pass

print(f'\nUNIV CALIFORNIA patents cite {len(set(cited_patents))} unique patents')
print('Sample cited patents:', list(set(cited_patents))[:10])

# Prepare result
result = {
    'uc_patents_count': len(uc_patents),
    'uc_publication_numbers': uc_pub_numbers,
    'cited_patents_count': len(set(cited_patents)),
    'sample_cited': list(set(cited_patents))[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation': '[]', 'cpc': '[\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J2463/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K7/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09J9/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/037",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/042",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2003/0806",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C09D11/322",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C09D11/52",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K2201/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B82Y40/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:8': [{'total': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': {'status': 'ready', 'files': ['/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Universal', '/usr/local/lib/python3.12/site-packages/pytz/zoneinfo/Etc/Universal', '/usr/local/lib/python3.12/site-packages/tzdata/zoneinfo/Universal']}, 'var_functions.query_db:42': [{'total': '169'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
