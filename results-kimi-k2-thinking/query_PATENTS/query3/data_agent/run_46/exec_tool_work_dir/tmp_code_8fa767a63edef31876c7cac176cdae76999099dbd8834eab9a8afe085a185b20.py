code = """import json
import re

# Get UC patents data with citations and CPC codes
file_path = var_functions.query_db:40
with open(file_path, 'r') as f:
    uc_data = json.load(f)

print('Total UC patent records:', len(uc_data))

uc_patents = {}
cited_patents = set()

for record in uc_data:
    patents_info = record.get('Patents_info', '')
    # Extract UC publication number
    match = re.search(r'(US|WO|EP|JP|CN|TW|KR|DE|GB|FR)-[A-Z0-9-]+-A[0-9]*', patents_info)
    if match:
        pub_num = match.group(0)
        citations = json.loads(record.get('citation', '[]'))
        cpc_codes = [c['code'] for c in json.loads(record.get('cpc', '[]'))]
        
        uc_patents[pub_num] = {
            'citations': citations,
            'cpc_codes': cpc_codes
        }
        
        # Collect cited patent numbers
        for citation in citations:
            cited_pub = citation.get('publication_number')
            if cited_pub:
                cited_patents.add(cited_pub)

print('UC patents extracted:', len(uc_patents))
print('Unique cited patents:', len(cited_patents))

# Show first UC patent
sample = list(uc_patents.keys())[0] if uc_patents else ''
if sample:
    print('\nSample UC patent:', sample)
    print('Citations:', len(uc_patents[sample]['citations']))
    print('CPC codes:', len(uc_patents[sample]['cpc_codes']))

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_patents),
    'unique_citations': len(cited_patents),
    'sample_cpc': uc_patents[sample]['cpc_codes'][:5] if sample else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'test', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patent_count': 3}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:32': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
