code = """import json, re

f_path = var_functions.query_db:64
c_path = var_functions.query_db:54

with open(f_path) as f:
    funding = json.load(f)

with open(c_path) as f:
    docs = json.load(f)

funding_names = [r['Project_Name'].lower() for r in funding]
design_projects = []

# Get capital design projects from document
text = docs[0]['text'].lower()
start = text.find('capital improvement projects (design)')
end = text.find('capital improvement projects (construction)')
if end == -1:
    end = text.find('capital improvement projects (not started)')
if end == -1:
    end = len(text)

design_section = text[start:end]
for line in design_section.split('\n'):
    clean = line.strip()
    if not clean or len(clean) < 10:
        continue
    lower = clean.lower()
    
    # Skip non-project lines
    if 'updates:' in lower or 'schedule:' in lower:
        continue
    if any(word in lower for word in ['staff', 'city will', 'project is', 'to:', 'prepared', 'approved']):
        continue
    if re.search(r'\d{4}', lower) and len(clean.split()) <= 4:
        continue
    if lower.startswith('capital improvement') or lower.startswith('(') or '(cid' in lower:
        continue
    if clean.isdigit():
        continue
    
    project = clean.title().strip()
    if project not in design_projects:
        design_projects.append(project)

# Match with funding data
matched = []
len_funding = len(funding_names)
for d in design_projects:
    d_core = d.lower().split('(')[0].strip()
    for i in range(len_funding):
        f = funding_names[i]
        f_core = f.split('(')[0].strip()
        if d_core == f_core:
            matched.append(d)
            break

result = len(matched)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
