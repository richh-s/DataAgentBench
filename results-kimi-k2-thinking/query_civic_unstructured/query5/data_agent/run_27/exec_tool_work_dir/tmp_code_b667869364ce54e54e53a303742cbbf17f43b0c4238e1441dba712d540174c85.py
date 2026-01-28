code = """import json

# Load funding and civic data
funding_data = json.load(open('file_storage/functions.query_db:5.json'))
civic_docs = json.load(open('file_storage/functions.query_db:6.json'))

# Build funding map
funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find disaster projects started in 2022
disaster_projects = set()
markers = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']

# Method 1: Projects with both 2022 and disaster markers in name
for name in funding_map.keys():
    if '2022' in name:
        for marker in markers:
            if marker in name:
                disaster_projects.add(name)

# Method 2: Explicit FEMA/CalOES/CalJPIA projects with 2022
for name in funding_map.keys():
    if '2022' in name:
        if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
            disaster_projects.add(name)

# Calculate funding
total = 0
project_list = []
for proj in disaster_projects:
    if proj in funding_map:
        amt = funding_map[proj]
        total += amt
        project_list.append([proj, amt])

project_list.sort(key=lambda x: x[1], reverse=True)

result = dict(total_funding=total, project_count=len(project_list), projects=project_list)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}}

exec(code, env_args)
