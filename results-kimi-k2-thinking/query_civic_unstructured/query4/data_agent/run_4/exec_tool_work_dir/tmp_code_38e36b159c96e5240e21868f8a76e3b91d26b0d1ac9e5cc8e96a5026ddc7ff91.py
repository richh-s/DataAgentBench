code = """import json

# Load civic documents from file
civic_file = var_functions.query_db_50
civic_data = []
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_data = json.load(f)
else:
    civic_data = civic_file if isinstance(civic_file, list) else []

# Load funding data from file
funding_file = var_functions.query_db_60
funding_data = []
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file if isinstance(funding_file, list) else []

print(f'Loaded {len(civic_data)} civic docs and {len(funding_data)} funding records')

# Build funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(fund.get('Amount', 0))

print(f'Created funding lookup with {len(funding_lookup)} projects')

# Find Spring 2022 projects
spring_2022_found = []

for doc in civic_data:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring_2022_found.append(doc)

print(f'Found {len(spring_2022_found)} documents mentioning Spring 2022')

result = {
    'civic_docs': len(civic_data),
    'funding_records': len(funding_data),
    'funding_projects': len(funding_lookup),
    'spring_2022_docs': len(spring_2022_found)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
