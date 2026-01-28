code = """import json
import re

# Read funding data (projects > $50,000)
funding_file = var_functions.query_db:64
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'].lower() for record in funding_records]

# Read civic documents
civic_file = var_functions.query_db:54
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects from first document
text = civic_docs[0]['text'].lower()

# Find design section
start = text.find('capital improvement projects (design)')
if start != -1:
    end = text.find('capital improvement projects (construction)', start)
    if end == -1:
        end = text.find('capital improvement projects (not started)', start)
    if end == -1:
        end = len(text)
    
    design_section = text[start:end]
    lines = design_section.split('\n')
    
    design_projects = []
    for line in lines:
        clean = line.strip()
        if not clean:
            continue
        
        lower = clean.lower()
        
        # Skip metadata and status lines
        if lower.startswith('capital improvement') or lower.startswith('(') or '(cid' in lower:
            continue
        if 'updates:' in lower or 'schedule:' in lower:
            continue
        if any(word in lower for word in ['staff', 'city will', 'project is', 'to:', 'prepared', 'approved']):
            continue
        if re.search(r'\d{4}', lower) and len(clean.split()) <= 4:
            continue
        if clean.isdigit() or len(clean) < 10:
            continue
        
        project_name = clean.title().strip()
        if project_name not in design_projects:
            design_projects.append(project_name)

# Match design projects with funding
matched = []
for d in design_projects:
    d_core = d.lower().split('(')[0].strip()
    for f in funding_names:
        f_core = f.split('(')[0].strip()
        if d_core == f_core:
            matched.append(d)
            break

result = len(matched)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
