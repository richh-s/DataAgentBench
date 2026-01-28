code = """import json, re, os

# Load file paths
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:8']

with open(funding_file) as f:
    funding = json.load(f)
with open(civic_file) as f:
    docs = json.load(f)

# Build funding set for amounts > $50000
funding_names = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funding_names.add(r['Project_Name'].lower())

# Extract capital design projects
design_names = set()
for d in docs:
    txt = d.get('text','')
    # Find design section
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(txt)
    
    section = txt[start:end]
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

# Count projects with matching funding > $50000
count = 0
for proj in design_names:
    for fund in funding_names:
        if proj in fund or fund in proj:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
