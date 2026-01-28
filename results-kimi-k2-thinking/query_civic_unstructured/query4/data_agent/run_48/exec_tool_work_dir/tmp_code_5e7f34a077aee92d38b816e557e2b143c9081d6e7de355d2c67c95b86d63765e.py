code = """import json, re

# Get the data from the stored file paths
funding_data = json.load(open('/tmp/tmp6n1m8z7u.json', 'r'))
civic_docs = json.load(open('/tmp/tmpz9j4h_69.json', 'r'))

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Find projects with 2022 in their names
projects_2022 = []
for f in funding_data:
    name = f.get('Project_Name', '')
    if '2022' in name:
        projects_2022.append({'name': name, 'funding': int(f.get('Amount', 0))})

total_funding = sum(p['funding'] for p in projects_2022)
count = len(projects_2022)

print('Found', count, '2022 projects')
for p in projects_2022:
    print('-', p['name'], ':', p['funding'])

result = {'project_count': count, 'total_funding': total_funding, 'projects': projects_2022}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': []}

exec(code, env_args)
