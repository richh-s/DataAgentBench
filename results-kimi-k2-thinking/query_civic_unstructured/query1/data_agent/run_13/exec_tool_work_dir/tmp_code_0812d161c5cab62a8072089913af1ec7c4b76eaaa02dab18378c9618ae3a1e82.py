code = """import json
import re

f_path = var_functions.query_db:64
c_path = var_functions.query_db:54

with open(f_path, 'r') as f:
    funding_records = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

funding_names = [r['Project_Name'] for r in funding_records]

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lower_text = text.lower()
    design_start = lower_text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    end_pos = len(lower_text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = lower_text.find(marker, design_start)
        if pos != -1 and pos < end_pos:
            end_pos = pos
    
    design_section = lower_text[design_start:end_pos]
    lines = design_section.split('\n')
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line or len(clean_line) < 10:
            continue
        
        lower_line = clean_line.lower()
        
        # Skip status/schedule/update lines
        if any(word in lower_line for word in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is']):
            continue
        
        # Skip metadata lines  
        if any(lower_line.startswith(prefix) for prefix in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission']):
            continue
        
        # Skip CID markers and similar
        if '(cid' in lower_line or clean_line.startswith('('):
            continue
        
        # Skip short schedule lines with years
        if re.search(r'\d{4}', lower_line) and len(clean_line.split()) <= 4:
            continue
        
        # This appears to be a project name
        project_name = clean_line.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match with funding data
matched = []

for design in design_projects:
    design_lower = design.lower()
    design_core = re.sub(r'\s*\([^)]+\)$', '', design_lower).strip()
    
    for fund in funding_names:
        fund_lower = fund.lower()
        fund_core = re.sub(r'\s*\([^)]+\)$', '', fund_lower).strip()
        
        if design_core == fund_core and design not in matched:
            matched.append(design)
            break

count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
