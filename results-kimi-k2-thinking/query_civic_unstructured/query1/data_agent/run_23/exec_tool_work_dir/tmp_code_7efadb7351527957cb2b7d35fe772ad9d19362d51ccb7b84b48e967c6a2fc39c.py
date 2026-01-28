code = """import json

# Load funding data
with open('var_functions.query_db:30') as f:
    funding = json.load(f)

# Load civic documents
with open('var_functions.query_db:31') as f:
    docs = json.load(f)

# Build funding dictionary (amount > 50000)
funded = {}
for r in funding:
    amt = int(r.get('Amount', 0))
    if amt > 50000:
        name = r.get('Project_Name', '').strip()
        if name:
            funded[name.lower()] = name

print('Funded > $50K count: ' + str(len(funded)))

# Extract design projects
design = []
for doc in docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = text.find(marker, start + 50)
        if start < pos < end:
            end = pos
    
    section = text[start:end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        if line.startswith('cid:') or 'Updates:' in line or 'Project Schedule:' in line or 'Page' in line:
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        if line[0].isupper() and len(line.split()) >= 2:
            valid = False
            for j in range(i+1, min(i+4, len(lines))):
                if 'updates:' in lines[j].lower():
                    valid = True
                    break
            
            if not valid:
                if 'Project' in line or 'Improvements' in line or 'Drainage' in line:
                    valid = True
            
            if valid and line not in design:
                design.append(line)

print('Design projects: ' + str(len(design)))

matches = []
for p in design:
    pk = p.lower()
    if pk in funded:
        matches.append(p)
    else:
        for fk in funded:
            if pk in fk or fk in pk:
                pw = set(pk.split())
                fw = set(fk.split())
                if len(pw.intersection(fw)) >= 2:
                    matches.append(p)
                    break

unique = list(set(matches))
print('Final matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
