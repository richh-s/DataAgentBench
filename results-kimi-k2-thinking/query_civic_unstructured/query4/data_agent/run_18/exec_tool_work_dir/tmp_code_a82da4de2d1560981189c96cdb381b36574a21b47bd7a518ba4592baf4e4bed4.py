code = """import json

# Load the data files
civic_docs_file = locals()['var_functions.query_db:11']
funding_file = locals()['var_functions.query_db:12']

civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding map
funding_map = {}
for record in funding_data:
    project_name = record.get('Project_Name', '').strip()
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

# Find projects with 2022 in name (potential Spring 2022 projects)
projects_2022 = []
for name in funding_map.keys():
    if '2022' in name:
        projects_2022.append(name)

total_funding = sum(funding_map.get(name, 0) for name in projects_2022)

print('__RESULT__:')
result = {
    'projects_starting_spring_2022': projects_2022,
    'count': len(projects_2022),
    'total_funding': total_funding
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
