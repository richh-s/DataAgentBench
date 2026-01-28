code = """import json
import re

funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create mapping of funding projects with amount > 50000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
    
    # Extract design section (up to next major section)
    remaining = text[design_pos:]
    next_section = remaining.find('Capital Improvement Projects (Construction)')
    if next_section > 0:
        design_section = remaining[:next_section]
    else:
        design_section = remaining
    
    # Parse project names from design section
    for line in design_section.split('\n'):
        line = line.strip()
        if line and len(line) > 10:
            # Skip meta lines
            meta = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'Page', 'Agenda', 'Capital Improvement Projects', 'Updates:', 'Schedule:']
            if any(word in line.upper() for word in meta):
                continue
            
            # Skip lines starting with bullets/parentheses
            if line.startswith('(') or line.startswith('\u2022'):
                continue
            
            # Check if disaster project (skip these)
            if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Add as capital design project
            capital_design_projects.add(line)

# Count matches with funding > $50k
count = 0
matched_projects = []

for proj in capital_design_projects:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    
    if proj in funding_map or proj_clean in funding_map:
        count += 1
        amount = funding_map.get(proj) or funding_map.get(proj_clean, 0)
        matched_projects.append({
            'Project_Name': proj,
            'Amount': int(amount)
        })

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
