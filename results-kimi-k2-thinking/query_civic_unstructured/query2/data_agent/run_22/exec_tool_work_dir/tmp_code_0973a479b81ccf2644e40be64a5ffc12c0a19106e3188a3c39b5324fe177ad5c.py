code = """import json, re

civic_docs = locals()['var_functions.query_db_74']
funding_data = locals()['var_functions.query_db_8']

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with 2022 completion
    # Pattern: project name with Park, then completion status with 2022
    pattern = r'([A-Za-z\s]*Park[A-Za-z\s]*)[^\n]*(?:Construction was completed|completed)[^\n]*2022'
    matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
    
    for m in matches:
        project_name = m.group(1).strip()
        if project_name and len(project_name) < 150 and project_name not in park_projects:
            park_projects.append(project_name)

# Also check Broad Beach Road Water Quality Repair (park infrastructure completed Nov 2022)
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Broad Beach Road Water Quality' in text and '2022' in text and 'completed' in text.lower():
        if 'Broad Beach Road Water Quality Repair' not in park_projects:
            park_projects.append('Broad Beach Road Water Quality Repair')

# Match with funding records
total_funding = 0
matched = []

for project in park_projects:
    proj_key = project.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        if proj_key == fund_name or fund_name.startswith(proj_key):
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({'project': project, 'amount': amount})

result = {'total_funding': total_funding, 'matched_projects': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'files': [], 'civic_related': []}, 'var_functions.execute_python:72': {'civic_type': "<class 'NoneType'>", 'funding_type': "<class 'NoneType'>"}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
