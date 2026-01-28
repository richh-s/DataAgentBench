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

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find end of section
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']
    end = len(text)
    for marker in end_markers:
        pos = text.find(marker, start)
        if pos > 0 and pos < end:
            end = pos
    
    section = text[start:end]
    
    # Split into lines and extract project names
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip status/schedule lines and metadata
        lower_line = line.lower()
        if 'updates:' in lower_line or 'schedule:' in lower_line or 'advertise:' in lower_line:
            continue
        if 'staff' in lower_line or 'city' in lower_line or 'project is' in lower_line:
            continue
        if lower_line.startswith('to:') or lower_line.startswith('prepared') or lower_line.startswith('approved'):
            continue
        if lower_line.startswith('date') or lower_line.startswith('meeting') or lower_line.startswith('subject:'):
            continue
        if lower_line.startswith('agenda') or lower_line.startswith('item') or lower_line.startswith('page'):
            continue
        if lower_line.startswith('public works') or lower_line.startswith('commission'):
            continue
        if '(cid' in lower_line or line.startswith('('):
            continue
        
        # Add project name
        proj = line.strip().title()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match with funding projects > $50,000
matched = []

for design_proj in design_projects:
    # Clean project name for matching (remove parenthetical suffixes)
    clean_design = design_proj.split('(')[0].strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = fund_proj.split('(')[0].strip().lower()
        
        # Check for match
        if clean_design == clean_fund or clean_design in clean_fund or clean_fund in clean_design:
            if design_proj not in matched:
                matched.append(design_proj)

# Count matched projects
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
