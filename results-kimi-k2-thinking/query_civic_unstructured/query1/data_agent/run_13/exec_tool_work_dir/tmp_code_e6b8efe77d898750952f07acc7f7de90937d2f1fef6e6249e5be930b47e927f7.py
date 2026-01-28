code = """import json

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find project names in design section
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find where design section ends
    end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip update/schedule lines and metadata
        skip = False
        for pattern in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'complete design', 'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid', '(']:
            if pattern in line.lower():
                skip = True
                break
        if skip:
            continue
        
        # Add project name
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match projects with funding > $50,000
matched = []

for design_proj in design_projects:
    # Remove parenthetical suffixes for matching
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = fund_proj.split('(')[0].strip().lower()
        
        if clean_design == clean_fund or clean_design in clean_fund or clean_fund in clean_design:
            if design_proj not in matched:
                matched.append(design_proj)

# Result count
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
