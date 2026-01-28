code = """import json

civic_docs = json.load(open('var_functions.query_db_32'))
funding_data = json.load(open('var_functions.query_db_8'))

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Bluffs Park Shade' in text and '2022' in text:
        park_projects.append('Bluffs Park Shade Structure')
    if 'Broad Beach Road Water Quality' in text and '2022' in text:
        park_projects.append('Broad Beach Road Water Quality Repair')

# Match with funding and calculate total
total_funding = 0
for fund in funding_data:
    name = fund['Project_Name']
    if name == 'Bluffs Park Shade Structure' or name == 'Broad Beach Road Water Quality Repair':
        total_funding += int(fund['Amount'])

result = {'total_funding': total_funding, 'projects': park_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': []}

exec(code, env_args)
