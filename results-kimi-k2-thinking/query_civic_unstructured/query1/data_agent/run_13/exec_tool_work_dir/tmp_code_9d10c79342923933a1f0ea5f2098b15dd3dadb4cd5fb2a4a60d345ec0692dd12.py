code = """import json

# Get file paths from storage
funding_file_path = var_functions.query_db:0
civic_file_path = var_functions.query_db:5

# Load funding data
with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Find capital design projects in civic documents
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
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        lower_line = line.lower()
        
        # Skip update/schedule/metadata lines
        skip = False
        for keyword in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'complete design', 'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda']:
            if keyword in lower_line:
                skip = True
                break
        if skip:
            continue
        
        if '(cid' in lower_line or 'commission' in lower_line:
            continue
        
        # Add project name
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match with funding > $50,000
matched = []

for design_proj in design_projects:
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        if clean_design in fund_proj.lower() and len(clean_design) > 10:
            if design_proj not in matched:
                matched.append(design_proj)

# Count matched projects
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
