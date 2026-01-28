code = """import json
import re

# Load data
data = locals()
funding_path = data['var_functions.query_db:8']
civic_path = data['var_functions.query_db:14']

funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

civic_file = open(civic_path, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(item.get('Amount', 0))

# Find projects with 2022 in funding names
projects_2022 = []
for name, amount in funding_lookup.items():
    if '2022' in name and amount > 0:
        projects_2022.append({'name': name, 'funding': amount})

# Calculate totals
total_funding = sum(p['funding'] for p in projects_2022)
count = len(projects_2022)

result = {
    'project_count': count,
    'total_funding': total_funding,
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
