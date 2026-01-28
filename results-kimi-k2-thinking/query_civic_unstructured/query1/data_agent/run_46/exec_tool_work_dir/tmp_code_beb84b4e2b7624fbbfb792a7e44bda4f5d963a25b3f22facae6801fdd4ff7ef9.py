code = """import json
import re

# Load funding data
with open(var_functions.query_db:6, 'r') as f:
    funding = json.load(f)

# Load civic documents
with open(var_functions.query_db:8, 'r') as f:
    docs = json.load(f)

# Build funding map for amounts > 50000
def clean(name):
    name = re.sub(r'\(FEMA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\(CalOES[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\(CalJPIA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'Project$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

funding_map = {}
for r in funding:
    amt = int(r['Amount'])
    if amt > 50000:
        key = clean(r['Project_Name'])
        funding_map[key] = {'orig': r['Project_Name'], 'amt': amt}

# Extract design projects
design_projects = []
for doc in docs:
    text = doc.get('text', '')
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos == -1:
        continue
    
    constr_pos = text.find('Capital Improvement Projects (Construction)', design_pos)
    if constr_pos == -1:
        constr_pos = len(text)
    
    section = text[design_pos:constr_pos]
    lines = section.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            # Look ahead for project context
            ahead = ' '.join(lines[i+1:min(i+4, len(lines))])
            if 'Updates:' in ahead or 'Schedule:' in ahead:
                name = line[:-1] if line.endswith(':') else line
                if 'FEMA' not in name and 'CalOES' not in name and 'CalJPIA' not in name:
                    design_projects.append(name)
                    i += 3
        i += 1

# Remove duplicates
unique_design = list(set(design_projects))

# Match with funding
matches = []
for pname in unique_design:
    cname = clean(pname)
    if cname in funding_map:
        matches.append(pname)
    else:
        for funded in funding_map.keys():
            if cname in funded or funded in cname:
                matches.append(pname)
                break

print("__RESULT__:")
print(json.dumps({'count': len(matches), 'projects': matches[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
