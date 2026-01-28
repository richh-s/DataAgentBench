code = """import json
import re

# Get the full UNIV CALIFORNIA patents data
file_path = var_functions.query_db:26
with open(file_path, 'r') as f:
    uc_data = json.load(f)

print('Total UNIV CALIFORNIA records:', len(uc_data))

# Extract UC patent publication numbers
uc_pub_numbers = set()
uc_patents = {}

for record in uc_data:
    patents_info = record.get('Patents_info', '')
    
    # Extract UC publication number
    match = re.search(r'(US|WO|EP|JP|CN|TW|KR|DE|GB|FR)-[A-Z0-9-]+-A[0-9]*', patents_info)
    if match:
        pub_num = match.group(0)
        uc_pub_numbers.add(pub_num)
        uc_patents[pub_num] = {
            'patents_info': patents_info,
            'citations': json.loads(record.get('citation', '[]'))
        }

print('UNIV CALIFORNIA patent publication numbers:', len(uc_pub_numbers))
print('Sample:', list(uc_pub_numbers)[:5])

# Extract all citations from UC patents
all_cited_pubs = set()
for pub_num, data in uc_patents.items():
    for citation in data['citations']:
        cited_pub = citation.get('publication_number')
        if cited_pub:
            all_cited_pubs.add(cited_pub)

print('\nTotal unique patents cited by UC patents:', len(all_cited_pubs))
print('Sample cited patents:', list(all_cited_pubs)[:10])

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_pub_numbers),
    'total_cited_patents': len(all_cited_pubs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'test', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patent_count': 3}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
