code = """# Load and process data
import json
import re

key1 = 'var_functions.query_db:30'
key2 = 'var_functions.query_db:31'

with open(key1, 'r') as f:
    funding = json.load(f)

with open(key2, 'r') as f:
    docs = json.load(f)

fund = {}
for r in funding:
    amt = int(r.get('Amount', 0))
    if amt > 50000:
        name = r.get('Project_Name', '').strip()
        if name:
            fund[name.lower()] = name

print('Funded projects > 50K: ' + str(len(fund)))

proj = []
for doc in docs:
    t = doc.get('text', '')
    
    start = t.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = len(t)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        p = t.find(marker, start + 50)
        if start < p < end:
            end = p
    
    section = t[start:end]
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
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    good = True
                    break
            
            if good or any(k in line for k in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road']):
                if line not in proj:
                    proj.append(line)

print('Design projects: ' + str(len(proj)))

matched = []
for p in proj:
    pk = p.lower()
    if pk in fund:
        matched.append(p)
    else:
        for fk in fund:
            if pk in fk or fk in pk:
                pw = set(pk.split())
                fw = set(fk.split())
                if len(pw.intersection(fw)) >= 2:
                    matched.append(p)
                    break

unique_matched = list(set(matched))
print('Matches: ' + str(len(unique_matched)))

if unique_matched:
    print('\nExamples:')
    for i in range(min(5, len(unique_matched))):
        print(str(i+1) + '. ' + unique_matched[i])

result = len(unique_matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
