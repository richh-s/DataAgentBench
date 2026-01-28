code = """import json, re

civic_file = locals()['var_functions.query_db:12']
funding_file = locals()['var_functions.query_db:2']

# Load data
with open(civic_file) as f:
    civic_docs = json.load(f)
with open(funding_file) as f:
    funding_data = json.load(f)

# Build funding map with projects > $50k
funding = {}
for r in funding_data:
    amount = int(r['Amount'])
    if amount > 50000:
        funding[r['Project_Name']] = amount

# Extract design projects
projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    in_design = False
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif any(x in line for x in ['Construction)', 'Not Started)']):
            in_design = False
        elif in_design and len(line) > 10 and not line.startswith('('):
            if 'Page' not in line and 'cid:' not in line:
                name = re.sub(r'\(cid:\d+\)', '', line).strip()
                if len(name) > 5 and 'updates' not in name.lower():
                    projects.append(name)

# Match projects
matches = set()
for p in projects:
    for f in funding:
        if p == f or p in f or f in p:
            matches.add(f)
            break

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
