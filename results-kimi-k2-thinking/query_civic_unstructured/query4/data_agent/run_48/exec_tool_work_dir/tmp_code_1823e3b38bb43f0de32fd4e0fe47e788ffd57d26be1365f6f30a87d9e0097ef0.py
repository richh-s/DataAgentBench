code = """import json
import re

# Access data directly from storage using the variable names
# The query results are stored in variables we can access via locals()
funding_data = locals()['var_functions.query_db:8']
civic_docs = locals()['var_functions.query_db:14']

print('Funding records loaded:', len(funding_data))
print('Civic documents loaded:', len(civic_docs))

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    funding_lookup[name] = int(item.get('Amount', 0))

# Find projects with 2022 in their names (likely started in 2022)
projects_2022 = []
for item in funding_data:
    name = item.get('Project_Name', '')
    if '2022' in name:
        projects_2022.append({
            'name': name,
            'funding': int(item.get('Amount', 0))
        })

# Total up funding for these projects
total_funding = sum(p['funding'] for p in projects_2022)

result = {
    'project_count': len(projects_2022),
    'total_funding': total_funding,
    'projects': projects_2022
}

print('\n2022 Projects from funding data:')
for p in projects_2022:
    print('-', p['name'], ': $', p['funding'])

print('\nTotal:', len(projects_2022), 'projects, $', total_funding, 'funding')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': []}

exec(code, env_args)
