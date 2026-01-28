code = """import json, re
from collections import defaultdict

# Load data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Loaded ' + str(len(all_patents)) + ' patents')

# Find UNIV CALIFORNIA patents
uc_patents = []
for patent in all_patents:
    if 'UNIV CALIFORNIA' in patent.get('Patents_info', '').upper():
        uc_patents.append(patent)

print('Found ' + str(len(uc_patents)) + ' UC patents')

# Print first UC patent info
if uc_patents:
    print('\nFirst UC patent info:')
    print(uc_patents[0]['Patents_info'])

result = {'total_patents': len(all_patents), 'uc_patents': len(uc_patents)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
