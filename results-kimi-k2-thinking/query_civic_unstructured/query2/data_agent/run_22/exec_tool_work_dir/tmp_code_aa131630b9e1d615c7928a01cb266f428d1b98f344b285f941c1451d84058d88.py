code = """import json

civic_docs = locals()['var_functions.query_db_74']
funding_data = locals()['var_functions.query_db_8']

# Find park projects completed in 2022
park_projects = []

# Check for Bluffs Park Shade Structure
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Bluffs Park Shade' in text and 'completed' in text.lower() and '2022' in text:
        park_projects.append('Bluffs Park Shade Structure')

# Check for Broad Beach Road Water Quality Repair
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Broad Beach Road Water Quality Repair' in text and '2022' in text:
        park_projects.append('Broad Beach Road Water Quality Repair')

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding records
total_funding = 0

for project in park_projects:
    proj_name = project
    
    for fund in funding_data:
        if fund['Project_Name'] == proj_name:
            total_funding += int(fund['Amount'])

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'files': [], 'civic_related': []}, 'var_functions.execute_python:72': {'civic_type': "<class 'NoneType'>", 'funding_type': "<class 'NoneType'>"}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
