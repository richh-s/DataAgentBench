code = """import json

f_file = var_functions.query_db:0
c_file = var_functions.query_db:5

with open(f_file, 'r') as f:
    funding_data = json.load(f)

with open(c_file, 'r') as f:
    civic_docs = json.load(f)

funding_names = [r['Project_Name'] for r in funding_data]

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    end = len(text)
    markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']
    for marker in markers:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    for line in section.split('\n'):
        line2 = line.strip()
        if not line2 or len(line2) < 10:
            continue
        lower_line = line2.lower()
        
        # Skip status lines
        if 'updates:' in lower_line or 'schedule:' in lower_line:
            continue
        if 'staff' in lower_line or 'city' in lower_line:
            continue
        if '(cid' in lower_line:
            continue
        if 'to:' in lower_line or 'prepared' in lower_line:
            continue
        
        # Add project name
        proj = line2.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

matched = []

for design_proj in design_projects:
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = fund_proj.split('(')[0].strip().lower()
        
        if clean_design == clean_fund:
            if design_proj not in matched:
                matched.append(design_proj)

print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
