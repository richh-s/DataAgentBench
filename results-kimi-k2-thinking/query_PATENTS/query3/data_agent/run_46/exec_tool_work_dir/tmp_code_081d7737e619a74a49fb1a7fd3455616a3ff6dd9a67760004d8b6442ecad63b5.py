code = """import json
import re

# Access the full result from the previous query
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f'Total publications found: {len(publications)}')

# Extract UNIV CALIFORNIA patents and their publication numbers
uc_patents = []
for pub in publications:
    patents_info = pub.get('Patents_info', '')
    match = re.search(r'(US|WO|EP|JP|CN|TW|KR|DE|GB|FR)-[A-Z0-9-]+-A[0-9]*', patents_info)
    if match:
        pub_num = match.group(0)
        uc_patents.append({
            'pub_num': pub_num,
            'patents_info': patents_info,
            'citation': pub.get('citation', '[]'),
            'cpc': pub.get('cpc', '[]')
        })

print(f'Total UNIV CALIFORNIA patents identified: {len(uc_patents)}')
print('First 5 publications:')
for i in range(min(5, len(uc_patents))):
    patent = uc_patents[i]
    print(f'  {i+1}. {patent["pub_num"]}')
    print(f'     {patent["patents_info"][:80]}...')

print('\nChecking citation structure...')
if uc_patents and uc_patents[0]['citation']:
    citations = json.loads(uc_patents[0]['citation'])
    print(f'First patent has {len(citations)} citations')
    if citations:
        print(f'  Sample: {citations[0]}')

print('\nChecking CPC structure...')
if uc_patents and uc_patents[0]['cpc']:
    cpc_codes = json.loads(uc_patents[0]['cpc'])
    print(f'First patent has {len(cpc_codes)} CPC codes')
    if cpc_codes:
        print(f'  Sample: {cpc_codes[0]}')

print('__RESULT__:')
print(json.dumps({'total_publications': len(publications), 'uc_patents_count': len(uc_patents)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
