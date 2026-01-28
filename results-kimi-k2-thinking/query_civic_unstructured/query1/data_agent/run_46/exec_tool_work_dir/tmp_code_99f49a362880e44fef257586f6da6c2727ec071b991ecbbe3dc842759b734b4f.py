code = """import json, re

# Load funding data
f_file = var_functions.query_db:6
with open(f_file, 'r') as f:
    funding = json.load(f)

# Load civic documents
c_file = var_functions.query_db:8
with open(c_file, 'r') as f:
    docs = json.load(f)

# Build funding map for amounts > 50000
def clean_name(n):
    n = re.sub(r'\(FEMA[^\)]*\)', '', n, 2)
    n = re.sub(r'\(CalOES[^\)]*\)', '', n, 2)
    n = re.sub(r'\(CalJPIA[^\)]*\)', '', n, 2)
    n = re.sub(r'Project$', '', n, 2)
    return n.strip().lower()

funding_map = {}
for r in funding:
    amt = int(r['Amount'])
    if amt > 50000:
        key = clean_name(r['Project_Name'])
        if key:
            funding_map[key] = {'name': r['Project_Name'], 'amt': amt}

# Extract capital projects with design status
design_projects = []

for doc in docs:
    txt = doc.get('text', '')
    
    # Find design section
    design_pos = txt.find('Capital Improvement Projects (Design)')
    if design_pos == -1:
        continue
    
    # Find where design section ends
    construct_pos = txt.find('Capital Improvement Projects (Construction)', design_pos)
    if construct_pos == -1:
        construct_pos = txt.find('Disaster Recovery Projects', design_pos)
    if construct_pos == -1:
        construct_pos = len(txt)
    
    # Extract design section
    design_section = txt[design_pos:construct_pos]
    
    # Find project names (lines that are likely project names)
    lines = design_section.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headings and markers
        if line.startswith('(') or 'Capital Improvement' in line:
            continue
        
        # Look for lines that are followed by project details
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Schedule:' in next_line:
                # This is likely a project name
                name = line[:-1] if line.endswith(':') else line
                # Skip disaster projects
                if 'FEMA' not in name and 'CalOES' not in name and 'CalJPIA' not in name:
                    # Check if it's a capital project
                    keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street']
                    if any(kw in name.lower() for kw in keywords):
                        design_projects.append(name)

# Remove duplicates
unique_projects = list(set(design_projects))

# Count matches with funding > 50000
matched_count = 0
matches = []

for proj in unique_projects:
    cproj = clean_name(proj)
    if not cproj:
        continue
    
    # Direct match
    if cproj in funding_map:
        matched_count += 1
        matches.append({'project': proj, 'funding': funding_map[cproj]['name'], 'amt': funding_map[cproj]['amt']})
        continue
    
    # Partial match
    for fkey in funding_map:
        if cproj in fkey or fkey in cproj:
            matched_count += 1
            matches.append({'project': proj, 'funding': funding_map[fkey]['name'], 'amt': funding_map[fkey]['amt']})
            break

print('__RESULT__:')
print(json.dumps({'count': matched_count, 'examples': matches[:3]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
