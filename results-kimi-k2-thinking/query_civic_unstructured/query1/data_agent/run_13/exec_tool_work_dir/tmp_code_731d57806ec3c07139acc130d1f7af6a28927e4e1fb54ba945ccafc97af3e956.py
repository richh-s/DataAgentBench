code = """import json

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
    
    end = len(text)
    markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']
    for marker in markers:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip lines containing status/schedule keywords
        lower_line = line.lower()
        status_words = ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'complete design', 'final design']
        meta_words = ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission']
        
        skip = False
        for word in status_words + meta_words:
            if word in lower_line:
                skip = True
                break
        
        if skip:
            continue
        
        if '(cid' in lower_line:
            continue
        
        # Add project name
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match with funding data
matched = []

for design_proj in design_projects:
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = fund_proj.split('(')[0].strip().lower()
        
        if clean_design == clean_fund:
            if design_proj not in matched:
                matched.append(design_proj)
        elif clean_design in clean_fund and len(clean_design) > 10:
            if design_proj not in matched:
                matched.append(design_proj)
        elif clean_fund in clean_design and len(clean_fund) > 10:
            if design_proj not in matched:
                matched.append(design_proj)

# Get count
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
