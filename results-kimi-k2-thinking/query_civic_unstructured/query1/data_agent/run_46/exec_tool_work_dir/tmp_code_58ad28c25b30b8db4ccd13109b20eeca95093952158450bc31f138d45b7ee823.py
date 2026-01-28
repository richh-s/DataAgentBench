code = """import json
import re

# Load data
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:8

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    docs = json.load(f)

# Build funding map
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
        funding_map[key] = r['Project_Name']

# Extract capital design projects
design_list = []
for d in docs:
    txt = d.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(txt)
    
    section = txt[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if line and len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                if any(kw in line.lower() for kw in ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']):
                    design_list.append(line)

# Remove duplicates and clean
unique_design = list(set(design_list))

# Match projects
count = 0
matched = []
for proj in unique_design:
    cproj = clean_name(proj)
    for fkey in funding_map:
        if cproj in fkey or fkey in cproj:
            count += 1
            matched.append(proj)
            break

print("__RESULT__:")
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
