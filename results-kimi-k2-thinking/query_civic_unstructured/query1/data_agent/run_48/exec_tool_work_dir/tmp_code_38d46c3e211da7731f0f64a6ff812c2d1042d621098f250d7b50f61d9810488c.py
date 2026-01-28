code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:70
f1 = open(funding_path)
funding_data = json.load(f1)
f1.close()

# Load civic documents
civic_path = var_functions.query_db:2
f2 = open(civic_path)
civic_docs = json.load(f2)
f2.close()

# Get all high-funding projects
high_funding = set()
for item in funding_data:
    high_funding.add(item['Project_Name'])

# Simple approach: extract capital design project names
design_names = []
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in txt:
        continue
    
    # Find section
    start = txt.find('Capital Improvement Projects (Design)') + 37
    section = txt[start:]
    
    # Cut before next section
    next_sec = section.find('Capital Improvement Projects (Construction)')
    if next_sec == -1: 
        next_sec = section.find('Capital Improvement Projects (Not Started)')
    if next_sec == -1: 
        next_sec = section.find('Disaster Recovery Projects')
    
    if next_sec > 0:
        section = section[:next_sec]
    
    # Parse blocks
    parts = section.split('\n\n')
    for part in parts:
        if len(part.strip()) > 15:
            lines = part.split('\n')
            if lines:
                name = lines[0].strip()
                if len(name) > 10 and not name.isupper():
                    design_names.append(name)

# Match
matched = 0
for proj in design_names:
    pl = proj.lower()
    for fund in high_funding:
        fl = fund.lower()
        if pl == fl or proj in fund or fund in proj:
            matched += 1
            break
        pw = set(pl.split())
        fw = set(fl.split())
        if len(pw) >= 2 and len(fw) >= 2 and len(pw & fw) >= 2:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
