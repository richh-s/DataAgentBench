code = """import json, re

# Load funding data from file
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Load civic documents from file
civic_file = var_functions.query_db:8
with open(civic_file, 'r') as f:
    docs = json.load(f)

# Create funding map for amounts > 50000
def clean_name(n):
    n = re.sub(r'\(FEMA[^\)]*\)', '', n, flags=2)
    n = re.sub(r'\(CalOES[^\)]*\)', '', n, flags=2)
    n = re.sub(r'\(CalJPIA[^\)]*\)', '', n, flags=2)
    n = re.sub(r'Project$', '', n, flags=2)
    return n.strip().lower()

funding_map = {}
for r in funding:
    amt = int(r['Amount'])
    if amt > 50000:
        key = clean_name(r['Project_Name'])
        if key:
            funding_map[key] = r['Project_Name']

# Extract capital design projects
design_projects = set()

for d in docs:
    text = d.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = text.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = text.find('Disaster Recovery Projects', start)
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    lines = section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                # Look for infrastructure keywords
                keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic','building','parkway']
                if any(kw in line.lower() for kw in keywords):
                    design_projects.add(line)

# Count matches
count = 0
for proj in design_projects:
    cproj = clean_name(proj)
    for fkey in funding_map:
        if cproj in fkey or fkey in cproj:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
