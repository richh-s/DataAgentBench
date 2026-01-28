code = """import json
import re

# Get funding data
f_path = var_functions.query_db:60
with open(f_path, 'r') as f:
    funding = json.load(f)

# Get civic documents
c_path = var_functions.query_db:54
with open(c_path, 'r') as f:
    docs = json.load(f)

# Extract project names from funding
funding_names = [r['Project_Name'] for r in funding]

# Get design projects from civic documents
design_projects = []

for doc in docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find where section ends
    end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    
    # Extract potential project names (lines that are not status updates)
    for line in section.split('\n'):
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        lower = line_clean.lower()
        
        # Skip status/update lines
        if any(word in lower for word in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is']):
            continue
        if '(cid' in lower or line_clean.startswith('('):
            continue
        
        # Skip dates/seasons
        if re.search(r'\d{4}', lower) and len(line_clean.split()) <= 4:
            continue
        
        # Add project name
        proj = line_clean.title().strip()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match with funding data
matched = []

for design_proj in design_projects:
    design_core = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        fund_core = fund_proj.split('(')[0].strip().lower()
        
        if design_core == fund_core:
            if design_proj not in matched:
                matched.append(design_proj)

# Result: count of capital design projects with funding > $50,000
count = len(matched)

print('__RESULT__:')
result_str = json.dumps(count)
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
