code = """import json, re

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded:', len(all_patents))

# Print first few UC patents to see the format
print('First 5 UC patents:')
for i, patent in enumerate(all_patents):
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        print('\nPatent ' + str(i) + ':')
        print(patents_info)
        if i >= 5:
            break"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
