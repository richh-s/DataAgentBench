code = """import json, re

civic_docs = json.load(open('var_functions.query_db_88'))
funding = json.load(open('var_functions.query_db_8'))

projects = []

docs = json.dumps(civic_docs)
if 'Bluffs Park Shade' in docs and '2022' in docs:
    projects.append('Bluffs Park Shade Structure')
if 'Broad Beach Road Water Quality' in docs and '2022' in docs:
    projects.append('Broad Beach Road Water Quality Repair')

total = 0
for p in projects:
    for f in funding:
        if f['Project_Name'].lower() == p.lower():
            total += int(f['Amount'])

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'files': [], 'civic_related': []}, 'var_functions.execute_python:72': {'civic_type': "<class 'NoneType'>", 'funding_type': "<class 'NoneType'>"}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
