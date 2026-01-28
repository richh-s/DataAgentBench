code = """import json

# Load funding data
f_file = var_functions.query_db:0
with open(f_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
c_file = var_functions.query_db:5
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Get project names from funding
funding_names = []
for record in funding_records:
    funding_names.append(record['Project_Name'])

# Extract capital design projects from civic documents
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
        
        # Skip status/schedule/metadata lines
        skip_words = ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'complete design', 'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission']
        should_skip = False
        for word in skip_words:
            if word in lower_line:
                should_skip = True
                break
        if should_skip:
            continue
        if '(cid' in lower_line:
            continue
        
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match design projects with funding > $50,000
matched = []

for design_proj in design_projects:
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = fund_proj.lower()
        
        if clean_design in clean_fund and len(clean_design) > 10:
            if design_proj not in matched:
                matched.append(design_proj)

# Count results
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
