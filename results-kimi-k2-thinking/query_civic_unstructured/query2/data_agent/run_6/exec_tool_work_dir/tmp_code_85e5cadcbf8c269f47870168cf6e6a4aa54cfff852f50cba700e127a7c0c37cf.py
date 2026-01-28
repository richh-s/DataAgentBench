code = """import json

# Load funding data
with open('file_storage/functions.query_db:20.json', 'r') as f:
    funding_data = json.load(f)

# Based on the civic documents preview, these park projects were completed in 2022:
park_projects_2022 = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair', 
    'Point Dume Walkway Repairs'
]

# Find matching funding records
total_funding = 0
matching_records = []

for fund in funding_data:
    project_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    # Check for exact matches or close matches
    for park_project in park_projects_2022:
        if park_project.lower() in project_name.lower():
            total_funding += amount
            matching_records.append({
                'project': park_project,
                'funded_as': project_name,
                'amount': amount,
                'source': fund['Funding_Source']
            })

result = {
    'total_funding': total_funding,
    'matching_records': matching_records,
    'num_projects': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
