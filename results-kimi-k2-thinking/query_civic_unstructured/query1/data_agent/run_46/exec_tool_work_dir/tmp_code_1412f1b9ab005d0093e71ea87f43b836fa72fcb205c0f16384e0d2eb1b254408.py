code = """import json, re, os

# Get file paths from variables
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:8']

# Load funding data
with open(funding_file) as f:
    funding = json.load(f)

# Load civic documents
with open(civic_file) as f:
    docs = json.load(f)

# Build set of funded project names (> $50000)
funded = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funded.add(r['Project_Name'].lower())

# Extract capital projects with design status
design = set()
for d in docs:
    txt = d.get('text','')
    start = txt.find('Capital Improvement Projects (Design)')
    if start > -1:
        end = txt.find('Capital Improvement Projects (Construction)', start)
        if end == -1: end = len(txt)
        section = txt[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                    keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
                    if any(kw in line.lower() for kw in keywords):
                        design.add(line.lower())

# Count matches
count = sum(1 for proj in design if any(f in proj or proj in f for f in funded))

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
