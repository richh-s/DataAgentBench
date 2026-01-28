code = """import json

# Read data files
funding_path = locals()['var_functions.query_db:2']
docs_path = locals()['var_functions.query_db:0']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Find emergency/FEMA projects in funding
emergency_funding = []
for rec in funding_records:
    name = rec['Project_Name'].lower()
    if 'emergency' in name or 'fema' in name:
        emergency_funding.append(rec)

# Extract status info from civic docs
project_status = {}
for doc in civic_docs:
    txt = doc['text'].lower()
    lines = doc['text'].split('\n')
    for line in lines:
        clean = line.strip()
        if clean:
            low = clean.lower()
            if 'emergency' in low or 'fema' in low or 'warning' in low or 'siren' in low:
                status = 'not started'
                if 'under construction' in txt and low in txt:
                    status = 'completed'
                elif 'design' in txt and 'complete design' not in txt:
                    status = 'design'
                project_status[clean] = status

# Merge results
results = []
for proj in emergency_funding:
    name = proj['Project_Name']
    status = project_status.get(name, 'not started')
    proj_type = 'disaster' if 'fema' in name.lower() else 'capital'
    
    results.append({
        'Project_Name': name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Type': proj_type
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}}

exec(code, env_args)
