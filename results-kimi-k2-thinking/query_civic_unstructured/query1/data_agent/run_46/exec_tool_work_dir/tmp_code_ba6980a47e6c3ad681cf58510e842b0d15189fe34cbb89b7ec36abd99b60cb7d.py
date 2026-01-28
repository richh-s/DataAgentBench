code = """import json, re, os

# Get the file paths from variables
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:8']

# Load the data
with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

# First, get all funding records with amount > 50000
funding_names = set()
for r in funding:
    if int(r.get('Amount', 0)) > 50000:
        funding_names.add(r['Project_Name'].lower())

# Extract capital projects with design status from civic documents
design_projects = set()
for d in docs:
    txt = d.get('text', '')
    # Find Capital Improvement Projects (Design) section
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(txt)
    section = txt[start:end]
    # Extract project names from this section
    for line in section.split('\n'):
        line = line.strip()
        # Filter for likely project names
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                continue
            # Look for infrastructure keywords
            keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
            if any(kw in line.lower() for kw in keywords):
                design_projects.add(line.lower())

# Count projects that have matching funding > $50000
count = 0
for proj in design_projects:
    # Check if any funding record matches this project
    for fund in funding_names:
        if proj in fund or fund in proj:
            count += 1
            break

# Print result in required format
result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
