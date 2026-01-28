code = """import json

# Load funding data
with open('/mnt/data/funding.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('/mnt/data/civic.json', 'r') as f:
    civic_docs = json.load(f)

# Find projects with 2022 in name (indicates 2022 projects)
projects_2022 = []
for item in funding_data:
    name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    if '2022' in name and amount > 0:
        projects_2022.append({'name': name, 'funding': amount})

# Calculate totals
total_funding = sum(p['funding'] for p in projects_2022)
project_count = len(projects_2022)

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': projects_2022
}

print('Project count:', project_count)
print('Total funding:', total_funding)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': []}

exec(code, env_args)
