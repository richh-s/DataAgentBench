code = """import json
import os

# The query results are stored as file paths when too large
# Load the actual data from those file paths

funding_file_path = locals()['var_functions.query_db:8']
civic_file_path = locals()['var_functions.query_db:14']

print('Funding file path:', funding_file_path)
print('Civic docs file path:', civic_file_path)

# Check if files exist and load them
if os.path.exists(funding_file_path):
    with open(funding_file_path, 'r') as f:
        funding_data = json.load(f)
    print('Loaded funding data, count:', len(funding_data))
else:
    print('Funding file not found')
    funding_data = []

if os.path.exists(civic_file_path):
    with open(civic_file_path, 'r') as f:
        civic_docs = json.load(f)
    print('Loaded civic docs, count:', len(civic_docs))
else:
    print('Civic docs file not found')
    civic_docs = []

# Find projects with 2022 in their names
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

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': projects_2022
}

print('\nResult:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs']}

exec(code, env_args)
