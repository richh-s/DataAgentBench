code = """import json, re

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:20

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

# Build funding lookup
funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Extract design projects
design = []
for doc in docs:
    text = doc.get('text','')
    idx = text.find('Capital Improvement Projects (Design)')
    if idx != -1:
        design_section = text[idx:text.find('Capital Improvement Projects (Construction)', idx)]
        lines = [l.strip() for l in design_section.split(chr(10)) if l.strip()]
        for i,line in enumerate(lines):
            if len(line)>5 and '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line and 'Page' not in line:
                if i+1<len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                    design.append(line)

# Count >50K matches
matched = 0
for proj in design:
    projl = proj.lower()
    if projl in funded and funded[projl] > 50000:
        matched += 1

print('__RESULT__:')
print(json.dumps({'design_count': len(set(design)), 'funded_over_50k': matched}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
