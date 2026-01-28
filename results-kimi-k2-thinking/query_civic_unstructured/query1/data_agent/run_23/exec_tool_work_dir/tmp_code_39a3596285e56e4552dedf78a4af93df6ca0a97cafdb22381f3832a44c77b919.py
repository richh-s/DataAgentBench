code = """import json, re

# Load data
funding_file = var_functions.query_db:30
civic_file = var_functions.query_db:31

with open(funding_file) as f:
    funding_records = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Build funding dictionary (amount > 50000)
funded_lookup = {}
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        name = rec.get('Project_Name', '').strip()
        if name:
            funded_lookup[name.lower()] = name

print('Funded projects > $50K: ' + str(len(funded_lookup)))

# Extract capital design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        p = text.find(marker, start + 50)
        if start < p < end:
            end = p
    
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
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    valid = True
                    break
            
            if not valid:
                keywords = ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road', 'Park']
                for k in keywords:
                    if k in line:
                        valid = True
                        break
            
            if valid and line not in design_projects:
                design_projects.append(line)

print('Design projects: ' + str(len(design_projects)))

# Match projects
matches = []
for p in design_projects:
    pk = p.lower()
    if pk in funded_lookup:
        matches.append(p)
    else:
        for fk in funded_lookup:
            if pk in fk or fk in pk:
                proj_words = set(pk.split())
                funded_words = set(fk.split())
                if len(proj_words.intersection(funded_words)) >= 2:
                    matches.append(p)
                    break

unique_matches = list(set(matches))
print('Final matches: ' + str(len(unique_matches)))

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
