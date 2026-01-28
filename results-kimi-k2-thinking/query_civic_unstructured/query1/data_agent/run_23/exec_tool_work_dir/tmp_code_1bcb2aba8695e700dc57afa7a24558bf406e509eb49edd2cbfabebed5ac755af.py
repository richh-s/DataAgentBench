code = """import json
import re

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:8

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    docs = json.load(f)

fund_dict = {}
for rec in funding:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        name = rec.get('Project_Name', '').strip()
        if name:
            fund_dict[name.lower()] = name

print('Funded projects >50K: ' + str(len(fund_dict)))

design_projs = []

for doc in docs:
    txt = doc.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = len(txt)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = txt.find(marker, start + 50)
        if start < pos < end:
            end = pos
    
    section = txt[start:end]
    lines = section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        bad = False
        for kw in ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page']:
            if kw in line:
                bad = True
                break
        
        if bad or (line.isupper() and len(line.split()) <= 3):
            continue
        
        if line[0].isupper() and len(line.split()) >= 2:
            good = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt or 'staff' in nxt:
                    good = True
                    break
            
            if good or 'Project' in line or 'Improvements' in line or 'Drainage' in line:
                if line not in design_projs:
                    design_projs.append(line)

print('Design projects: ' + str(len(design_projs)))

matched = []
for proj in design_projs:
    if proj.lower() in fund_dict:
        matched.append(proj)
    else:
        for fund_key in fund_dict:
            if proj.lower() in fund_key or fund_key in proj.lower():
                if len(proj.split()) >= 2:
                    matched.append(proj)
                    break

unique = list(set(matched))
print('Matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
