code = """import json
import re

# Read the data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects
all_projects = []
for doc in civic_docs:
    text_lines = doc.get('text', '').splitlines()
    current_status = None
    current_type = None
    
    for line in text_lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
            current_type = 'capital'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'completed'
            current_type = 'capital'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            current_type = 'capital'
        elif current_status and current_type and line and len(line) < 150:
            if not line.startswith('(') and 'Updates:' not in line and 'Project Schedule' not in line:
                if 'Capital Improvement' not in line and 'Disaster Recovery' not in line:
                    all_projects.append({'name': line, 'status': current_status, 'type': current_type})

# Filter for design capital projects and check funding > 50000
matching_projects = set()

for proj in all_projects:
    if proj['status'] == 'design' and proj['type'] == 'capital':
        for fund in funding:
            amount = int(fund['Amount'])
            if amount > 50000:
                proj_name_lower = proj['name'].lower()
                fund_name_lower = fund['Project_Name'].lower()
                
                if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
                    matching_projects.add(proj['name'])

answer = {'count': len(matching_projects)}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
