code = """import json

# Process the query results
file_path = 'var_functions.query_db:12'
with open(file_path, 'r') as f:
    content = f.read()
    publications = json.loads(content)

print('Total UNIV CALIFORNIA publications:', len(publications))

# Extract UC patent numbers
uc_patents = {}
for pub in publications:
    patents_info = pub['Patents_info']
    pub_num = ''
    if 'pub. number' in patents_info:
        parts = patents_info.split('pub. number')
        if len(parts) > 1:
            pub_num = parts[1].strip().rstrip('.')
    elif 'publication number' in patents_info:
        parts = patents_info.split('publication number')
        if len(parts) > 1:
            pub_num = parts[1].strip().rstrip('.')
    
    # Clean up publication number
    if pub_num.startswith('is'):
        pub_num = pub_num[2:].strip()
    
    uc_patents[pub_num] = {
        'patents_info': patents_info,
        'citation': pub['citation']
    }

print('UC Patents found:', list(uc_patents.keys())[:10])
print('__RESULT__:')
print(json.dumps({'uc_patent_count': len(uc_patents), 'first_five': list(uc_patents.keys())[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'test', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
