code = """import json

# Load data from files
funding_path = locals()['var_functions.query_db:2']
docs_path = locals()['var_functions.query_db:0']

with open(funding_path) as f:
    funding_records = json.load(f)
with open(docs_path) as f:
    civic_docs = json.load(f)

# Find emergency/FEMA projects
emergency_projects = []
for rec in funding_records:
    pname = rec['Project_Name'].lower()
    if 'emergency' in pname or 'fema' in pname:
        emergency_projects.append(rec)

# Extract status from documents
status_map = {}
for doc in civic_docs:
    text = doc['text'].lower()
    orig_lines = doc['text'].split('\n')
    for line in orig_lines:
        line_stripped = line.strip()
        if line_stripped:
            low_line = line_stripped.lower()
            if 'emergency' in low_line or 'fema' in low_line or 'warning' in low_line or 'siren' in low_line:
                status = 'not started'
                if 'under construction' in text and low_line in text:
                    status = 'completed'
                elif 'design' in text and 'complete design' not in text:
                    status = 'design'
                status_map[line_stripped] = status

# Combine results
final = []
for proj in emergency_projects:
    proj_name = proj['Project_Name']
    status = status_map.get(proj_name, 'not started')
    proj_type = 'disaster' if 'fema' in proj_name.lower() else 'capital'
    final.append({
        'Project_Name': proj_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Type': proj_type
    })

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}}

exec(code, env_args)
