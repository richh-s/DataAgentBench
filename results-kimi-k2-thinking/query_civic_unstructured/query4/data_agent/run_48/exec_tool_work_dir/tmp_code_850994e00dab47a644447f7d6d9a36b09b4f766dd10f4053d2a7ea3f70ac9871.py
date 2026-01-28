code = """# Use the stored results directly without file operations
# The variables are available in the locals() dictionary

import json

# Get funding data - it's a list, not a file path
funding_data = locals()['var_functions.query_db:8']
civic_docs = locals()['var_functions.query_db:14']

print('Got funding data:', type(funding_data), len(funding_data))
print('Got civic docs:', type(civic_docs), len(civic_docs))

# Find projects with 2022 in their names (indicates they started in 2022)
projects_2022 = []
for item in funding_data:
    name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    if '2022' in name:
        projects_2022.append({
            'name': name,
            'funding': amount
        })

# Calculate totals
total_funding = sum(p['funding'] for p in projects_2022)
project_count = len(projects_2022)

print('Found', project_count, 'projects from 2022')
print('Total funding:', total_funding)

for p in projects_2022:
    print('-', p['name'], ': $', p['funding'])

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs']}

exec(code, env_args)
