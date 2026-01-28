code = """import json
import re

# Load data
f_path = var_functions.query_db:64
c_path = var_functions.query_db:54

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_data = json.load(f)

funding_names = [item['Project_Name'] for item in funding_data]

# Find capital design projects
capital_design = []

for doc in civic_data:
    txt = doc.get('text', '').lower()
    
    # Find design section
    design_idx = txt.find('capital improvement projects (design)')
    if design_idx == -1:
        continue
    
    # Find section end
    next_section = txt.find('capital improvement projects (construction)', design_idx)
    if next_section == -1:
        next_section = txt.find('capital improvement projects (not started)', design_idx)
    if next_section == -1:
        next_section = txt.find('disaster recovery projects', design_idx)
    if next_section == -1:
        next_section = len(txt)
    
    section = txt[design_idx:next_section]
    
    # Split lines
    for ln in section.split('\n'):
        ln = ln.strip()
        if not ln or len(ln) < 10:
            continue
        
        lower_ln = ln.lower()
        
        # Skip update/schedule lines
        if lower_ln.find('updates:') > -1 or lower_ln.find('schedule:') > -1 or lower_ln.find('advertise:') > -1:
            continue
        
        if lower_ln.find('staff') > -1 or lower_ln.find('city') > -1 or lower_ln.find('project is') > -1:
            continue
        
        if lower_ln.startswith('to:') or lower_ln.startswith('prepared'):
            continue
        
        if '(cid' in lower_ln or ln.startswith('('):
            continue
        
        # Skip short lines with years/seasoons
        if re.search('202[0-9]', lower_ln) and len(ln.split()) <= 4:
            continue
        
        # Add project name
        pname = ln.strip().title()
        if pname not in capital_design:
            capital_design.append(pname)

# Match with funding
matched = []

for design_proj in capital_design:
    design_clean = design_proj.lower().split('(')[0].strip()
    
    for fund_proj in funding_names:
        fund_clean = fund_proj.lower().split('(')[0].strip()
        
        if design_clean == fund_clean:
            if design_proj not in matched:
                matched.append(design_proj)
                break

count = len(matched)

print('__RESULT__:')
result_json = json.dumps(count)
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
