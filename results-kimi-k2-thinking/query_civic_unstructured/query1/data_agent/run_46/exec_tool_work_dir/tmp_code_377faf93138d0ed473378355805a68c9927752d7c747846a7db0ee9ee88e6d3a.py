code = """import json, re, os, sys

# Access variables directly
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:8

# Load funding data
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents  
with open(civic_path) as f:
    civic_docs = json.load(f)

# Create funding map for >$50000
funding_set = set()
for r in funding_records:
    if int(r['Amount']) > 50000:
        funding_set.add(r['Project_Name'].lower())

# Extract design projects
design_set = set()
for doc in civic_docs:
    t = doc.get('text', '')
    # Find design section
    start = t.find('Capital Improvement Projects (Design)')
    if start == -1: continue
    end = t.find('Capital Improvement Projects (Construction)', start)
    if end == -1: end = len(t)
    section = t[start:end]
    # Extract lines that look like project names
    for line in section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                # Check for infrastructure keywords
                if any(kw in line.lower() for kw in ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']):
                    design_set.add(line.lower())

# Count matches
count = sum(1 for proj in design_set if any(proj in f or f in proj for f in funding_set))

print('__RESULT__:') 
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
