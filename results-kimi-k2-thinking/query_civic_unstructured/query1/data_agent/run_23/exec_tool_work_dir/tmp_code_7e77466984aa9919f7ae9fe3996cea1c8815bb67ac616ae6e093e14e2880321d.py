code = """import json
import re

# Load data
f_path = var_functions.query_db:18
c_path = var_functions.query_db:19

with open(f_path) as f:
    funding = json.load(f)

with open(c_path) as f:
    docs = json.load(f)

# Funding dict
fund = {}
for r in funding:
    amt = int(r.get('Amount', 0))
    if amt > 50000:
        name = r.get('Project_Name', '').strip()
        if name:
            fund[name.lower()] = name

print('Funded >50K: ' + str(len(fund)))

# Find design projects
projs = []

for doc in docs:
    t = doc.get('text', '')
    
    # Get design section
    d_start = t.find('Capital Improvement Projects (Design)')
    if d_start == -1:
        continue
    
    c_start = t.find('Capital Improvement Projects (Construction)', d_start)
    n_start = t.find('Capital Improvement Projects (Not Started)', d_start)
    
    end = len(t)
    if c_start > d_start:
        end = min(end, c_start)
    if n_start > d_start:
        end = min(end, n_start)
    
    section = t[d_start:end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        if any(x in line for x in ['cid:', 'Updates:', 'Project Schedule:', 'Page']):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        if line[0].isupper() and len(line.split()) >= 2:
            good = False
            for j in range(i+1, min(i+4, len(lines))):
                if 'updates:' in lines[j].lower() or 'project schedule:' in lines[j].lower():
                    good = True
                    break
            
            if good or 'Project' in line or 'Improvements' in line:
                if line not in projs:
                    projs.append(line)

print('Design projects: ' + str(len(projs)))

# Match
matches = []
for p in projs:
    key = p.lower()
    if key in fund:
        matches.append(p)
    else:
        for fk in fund:
            if key in fk or fk in key:
                if len(key.split()) >= 2:
                    matches.append(p)
                    break

unique = list(set(matches))
print('Final matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)
