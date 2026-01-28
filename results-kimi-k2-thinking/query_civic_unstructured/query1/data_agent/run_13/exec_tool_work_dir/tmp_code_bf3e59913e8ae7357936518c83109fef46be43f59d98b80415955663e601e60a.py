code = """import json
import re

# Load funding data
f_file = var_functions.query_db:0
with open(f_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [r['Project_Name'] for r in funding_records]

# Load civic documents
c_file = var_functions.query_db:5
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find end of section
    end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, start)
        if pos != -1 and pos < end:
            end = pos
    
    section = text[start:end]
    
    # Extract project names from lines
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip lines with status/schedule
        if any(x in line for x in ['updates:', 'schedule:', 'advertise:', 'complete design', 'staff', 'city']):
            continue
        
        # Skip metadata
        if any(line.startswith(x) for x in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid']):
            continue
        
        # Add project
        proj = line.title().strip()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match with funding > $50,000
matched = []

for design_proj in design_projects:
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_proj).strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = re.sub(r'\s*\([^)]+\)$', '', fund_proj).strip().lower()
        
        if clean_design == clean_fund or clean_design in clean_fund or clean_fund in clean_design:
            if design_proj not in matched:
                matched.append(design_proj)

# Get count
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
