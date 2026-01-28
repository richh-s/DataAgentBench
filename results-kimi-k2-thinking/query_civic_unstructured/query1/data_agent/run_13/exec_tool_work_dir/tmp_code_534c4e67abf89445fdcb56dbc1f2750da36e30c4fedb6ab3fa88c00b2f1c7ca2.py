code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section start
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find where design section ends
    end1 = text.find('capital improvement projects (construction)', start)
    end2 = text.find('capital improvement projects (not started)', start)
    end3 = text.find('disaster recovery projects', start)
    
    end = len(text)
    if end1 != -1:
        end = end1
    if end2 != -1 and end2 < end:
        end = end2
    if end3 != -1 and end3 < end:
        end = end3
    
    section = text[start:end]
    
    # Extract lines that look like project names
    lines = section.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip update and schedule lines
        skip_patterns = ['updates:', 'schedule:', 'advertise:', 'complete design:', 'final design:', 'estimated schedule:']
        if any(p in line for p in skip_patterns):
            continue
        
        # Skip metadata
        if line.startswith(('to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page')):
            continue
        
        if line.startswith(('public works', 'commission', '(cid', '(', '•')):
            continue
        
        # Add project name (convert to title case)
        proj = line.title().strip()
        if proj and proj not in design_projects:
            design_projects.append(proj)

# Match design projects with funding > $50,000
matched = []

for design_proj in design_projects:
    # Clean project names by removing parenthetical suffixes
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_proj).strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = re.sub(r'\s*\([^)]+\)$', '', fund_proj).strip().lower()
        
        # Check for match
        is_match = False
        
        if design_proj.lower() == clean_fund:
            is_match = True
        elif clean_design == clean_fund:
            is_match = True
        elif clean_design in clean_fund:
            is_match = True
        elif clean_fund in clean_design:
            is_match = True
        
        if is_match and design_proj not in matched:
            matched.append(design_proj)

# Result is the count
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
