code = """import json

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:5

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    docs = json.load(f)

funding_names = [r['Project_Name'] for r in funding]

design_projects = []

for doc in docs:
    text = doc.get('text', '').lower()
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        lower_line = line.lower()
        
        skip = False
        for keyword in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'complete design', 'to:', 'prepared', 'approved']:
            if keyword in lower_line:
                skip = True
                break
        if skip:
            continue
        if '(cid' in lower_line:
            continue
        
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

matched = []

for design_proj in design_projects:
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        if clean_design in fund_proj.lower() and len(clean_design) > 10:
            if design_proj not in matched:
                matched.append(design_proj)

print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
