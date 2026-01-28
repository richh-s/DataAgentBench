code = """import json, re, os

# Load the data from the stored file paths
funding_records = json.load(open(locals()['var_functions.query_db:6']))
civic_docs = json.load(open(locals()['var_functions.query_db:8']))

# Build funding map (projects with amount > 50000)
funding_names = set()
for record in funding_records:
    if int(record['Amount']) > 50000:
        funding_names.add(record['Project_Name'].lower())

# Extract capital projects with design status
design_names = set()
for doc in civic_docs:
    txt = doc.get('text', '')
    # Find design section
    design_start = txt.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    design_end = txt.find('Capital Improvement Projects (Construction)', design_start)
    if design_end == -1:
        design_end = len(txt)
    section = txt[design_start:design_end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                continue
            # Check for infrastructure keywords
            keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
            if any(kw in line.lower() for kw in keywords):
                design_names.add(line.lower())

# Count matches between design projects and funding
count = 0
for project in design_names:
    for funding in funding_names:
        if project in funding or funding in project:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
