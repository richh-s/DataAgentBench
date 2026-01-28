code = """import json

# Load funding data
funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects in design status from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    start_marker = 'Capital Improvement Projects (Design)'
    if start_marker not in text:
        continue
    
    design_start = text.find(start_marker)
    design_text = text[design_start + len(start_marker):]
    
    # Find where design section ends
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    design_end = len(design_text)
    for marker in end_markers:
        pos = design_text.find(marker)
        if pos > 0 and pos < design_end:
            design_end = pos
    
    design_section = design_text[:design_end]
    
    # Split into sections (double newline indicates new project/section)
    sections = design_section.split('\n\n')
    
    for section in sections:
        section = section.strip()
        if len(section) < 10:
            continue
        
        # Get first line - this is likely the project name
        first_line = section.split('\n')[0].strip()
        
        # Skip obvious non-project lines
        if len(first_line) > 150 or len(first_line) < 10:
            continue
        
        check_upper = first_line.upper()
        if 'UPDATES' in check_upper or 'SCHEDULE' in check_upper or 'RECOMMENDED' in check_upper:
            continue
        
        # Clean the name
        cleaned_name = first_line
        # Remove leading bullets like "A." or "1."
        if cleaned_name and cleaned_name[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(cleaned_name) > 2 and cleaned_name[1] == '.':
            cleaned_name = cleaned_name[2:].strip()
        
        if len(cleaned_name) > 10 and not cleaned_name.startswith('('):
            projects.append({
                'Project_Name': cleaned_name,
                'status': 'design',
                'type': 'capital'
            })

# Normalize for matching
import re

def normalize_name(name):
    if not name:
        return ''
    n = name.lower().strip()
    n = re.sub(r' +', ' ', n)  # Normalize spaces
    n = re.sub(r'\([^)]*\)', '', n)  # Remove parenthetical content
    n = re.sub(r'[^a-z0-9]', '', n)  # Keep only alnum
    return n

# Filter funding > 50000
high_funding = []
for fund in funding_data:
    amount = int(fund['Amount'])
    if amount > 50000:
        high_funding.append({
            'Project_Name': fund['Project_Name'],
            'Amount': amount,
            'Normalized_Name': normalize_name(fund['Project_Name'])
        })

# Match projects
matched = 0

for project in projects:
    proj_name = project['Project_Name']
    proj_normalized = normalize_name(proj_name)
    
    if len(proj_normalized) < 10:
        continue
    
    for fund in high_funding:
        fund_normalized = fund['Normalized_Name']
        
        # Exact normalized match
        if proj_normalized == fund_normalized:
            matched += 1
            break
        
        # Substring match
        if len(proj_normalized) > 15 and proj_normalized in fund_normalized:
            matched += 1
            break
        
        if len(fund_normalized) > 15 and fund_normalized in proj_normalized:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
