code = """import json
import re

# Load funding and document data
with open(var_functions.query_db:30, 'r') as f:
    funding_records = json.load(f)

with open(var_functions.query_db:31, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for amount > 50000
funding_lookup = {}
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        name = rec.get('Project_Name', '').strip()
        if name:
            funding_lookup[name.lower()] = name

print('Funded projects > 50K: ' + str(len(funding_lookup)))

# Extract capital design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    section_start = text.find('Capital Improvement Projects (Design)')
    if section_start == -1:
        continue
    
    # Find section end
    section_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = text.find(marker, section_start + 50)
        if section_start < pos < section_end:
            section_end = pos
    
    section = text[section_start:section_end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip markers
        if line.startswith('cid:') or any(x in line for x in ['Updates:', 'Project Schedule:', 'Page']):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check project name
        if line[0].isupper() and len(line.split()) >= 2:
            valid = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    valid = True
                    break
            
            if not valid and any(k in line for k in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road']):
                valid = True
            
            if valid and line not in design_projects:
                design_projects.append(line)

print('Design projects: ' + str(len(design_projects)))

# Match with funding
matches = []
for p in design_projects:
    pk = p.lower()
    if pk in funding_lookup:
        matches.append(p)
    else:
        for fk in funding_lookup:
            if pk in fk or fk in pk:
                proj_words = set(pk.split())
                fund_words = set(fk.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matches.append(p)
                    break

unique = list(set(matches))
print('Final matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
