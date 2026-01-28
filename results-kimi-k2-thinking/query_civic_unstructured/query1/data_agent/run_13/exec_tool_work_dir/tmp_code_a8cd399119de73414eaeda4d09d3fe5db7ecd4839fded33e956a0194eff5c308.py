code = """import json
import re

# Load funding data
f_path = var_functions.query_db:64
with open(f_path) as f:
    funding_records = json.load(f)

# Load civic documents
cc_path = var_functions.query_db:54
with open(cc_path) as f:
    civic_records = json.load(f)

# Extract funding project names
funding_names = [r['Project_Name'].lower() for r in funding_records]

# Extract design projects from civic documents
design_projects = []

for doc in civic_records:
    txt = doc.get('text', '').lower()
    
    # Find design section
    s = txt.find('capital improvement projects (design)')
    if s == -1:
        continue
    
    # Find end of design section
    e = len(txt)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = txt.find(marker, s)
        if pos != -1 and pos < e:
            e = pos
    
    section = txt[s:e]
    
    # Extract project lines
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        line_lower = line.lower()
        
        # Skip status/schedule lines
        if any(keyword in line_lower for keyword in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is']):
            continue
        
        # Skip metadata
        if any(prefix in line_lower[:20] for prefix in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:']):
            continue
        
        if '(cid' in line_lower or line.startswith('('):
            continue
        
        # Skip date lines
        if re.search(r'\d{4}', line_lower) and len(line.split()) <= 4:
            continue
        
        # Add project
        pname = line.strip().title()
        if pname and pname not in design_projects:
            design_projects.append(pname)

# Match with funding
matched_projects = []
for d in design_projects:
    d_core = d.lower().split('(')[0].strip()
    if d_core in funding_names and d not in matched_projects:
        matched_projects.append(d)

# Count results
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
