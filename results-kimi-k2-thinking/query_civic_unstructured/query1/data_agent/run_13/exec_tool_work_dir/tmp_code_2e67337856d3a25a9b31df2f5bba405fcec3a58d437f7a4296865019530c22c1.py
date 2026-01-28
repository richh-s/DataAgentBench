code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:46
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [r['Project_Name'] for r in funding_records]

# Load civic documents
civic_file = var_functions.query_db:50
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = []

for doc in civic_docs:
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
    lines = section.split('\n')
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        lower_line = line_clean.lower()
        
        # Skip status/schedule/metadata lines
        skip_patterns = ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'prepared', 'approved', 'date', 'meeting', 'subject:']
        
        skip = False
        for pattern in skip_patterns:
            if pattern in lower_line:
                skip = True
                break
        
        if skip or '(cid' in lower_line:
            continue
        
        # This looks like a project name
        project_name = line_clean.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match with funding data
matched = []

for design_proj in design_projects:
    design_core = re.sub('\s*\([^)]+\)$', '', design_proj.lower()).strip()
    
    for fund_proj in funding_names:
        fund_core = re.sub('\s*\([^)]+\)$', '', fund_proj.lower()).strip()
        
        if (design_core == fund_core or 
            design_core in fund_core or 
            fund_core in design_core):
            if design_proj not in matched:
                matched.append(design_proj)

count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
