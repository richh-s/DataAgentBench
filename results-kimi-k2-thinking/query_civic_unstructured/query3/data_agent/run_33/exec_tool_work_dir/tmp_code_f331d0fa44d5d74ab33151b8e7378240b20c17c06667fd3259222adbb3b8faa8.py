code = """import json
import re

# Read the civic documents
civic_docs_file = locals()['var_functions.query_db:0']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_file = locals()['var_functions.query_db:5']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract projects from civic documents
all_projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_status = None
    
    for line in lines:
        line = line.strip()
        if 'Design' in line and 'Project' in line:
            current_status = 'design'
        elif 'Construction' in line and 'Project' in line:
            current_status = 'construction'
        elif 'Not Started' in line:
            current_status = 'not started'
        elif 'Completed' in line:
            current_status = 'completed'
        elif line and len(line) > 10 and not line.startswith('('):
            if any(keyword in line.lower() for keyword in ['emergency', 'fema']):
                if current_status:
                    all_projects.append({
                        'Project_Name': line,
                        'Status': current_status
                    })
                else:
                    # Look for FEMA projects in funding data not in civic docs
                    pass

# Add FEMA projects from funding data
fema_projects = []
for f in funding_data:
    if 'fema' in f['Project_Name'].lower():
        fema_projects.append({
            'Project_Name': f['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Not specified'
        })

print('__RESULT__:')
print(json.dumps({
    'civic_projects': all_projects,
    'fema_funding_projects': fema_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
