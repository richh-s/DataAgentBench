code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:0
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:8
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary with amount > 50000
funding_dict = {}
for rec in funding_records:
    try:
        amt = int(rec.get('Amount', 0))
        if amt > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funding_dict[name.lower()] = {'orig': name, 'amt': amt}
    except:
        pass

print('Funding > 50K count: ' + str(len(funding_dict)))

# Extract design projects
projects = []

for doc in civic_docs:
    txt = doc.get('text', '')
    
    # Find design section
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Find section end
    end = len(txt)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = txt.find(marker, start + 50)
        if start < pos < end:
            end = pos
    
    section = txt[start:end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip irrelevant
        if not line or len(line) < 10:
            continue
        
        skip = False
        for kw in ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page']:
            if kw in line:
                skip = True
                break
        
        if skip:
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Look for project names
        if line[0].isupper() and len(line.split()) >= 2:
            valid = False
            # Check following lines for context
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt or 'staff' in nxt:
                    valid = True
                    break
            
            # Or check if line contains project keywords
            if 'Project' in line or 'Improvements' in line or 'Drainage' in line:
                valid = True
            
            if valid and line not in projects:
                projects.append(line)

print('Design projects extracted: ' + str(len(projects)))

# Match with funding
matched = []
for proj in projects:
    proj_key = proj.lower()
    
    if proj_key in funding_dict:
        matched.append(proj)
    else:
        for fund_key in funding_dict:
            # Check overlap
            proj_words = set(proj_key.split())
            fund_words = set(fund_key.split())
            shared = proj_words.intersection(fund_words)
            
            if len(shared) >= 2 or proj_key in fund_key or fund_key in proj_key:
                matched.append(proj)
                break

unique = list(set(matched))
print('Final matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
