code = """import json
import re

# Load data files
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Get funding projects with amount > 50000
funding_projects = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_projects[name] = amount
        funding_projects[clean_name] = amount

# Extract capital design projects from documents
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
    
    # Get text after design header
    remaining_text = text[design_pos + 40:]  # Skip the header
    
    # Find where next major section starts
    next_section_pos = remaining_text.find('Capital Improvement Projects (')
    if next_section_pos > 0:
        design_section = remaining_text[:next_section_pos]
    else:
        design_section = remaining_text
    
    # Extract project names from this section
    for line in design_section.split('\n'):
        line = line.strip()
        if line and len(line) > 10:
            # Skip meta lines
            skip = False
            meta_words = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'Page', 'Agenda', 'Capital Improvement', 'Projects']
            for word in meta_words:
                if word in line.upper():
                    skip = True
                    break
            
            if not skip and 'Updates:' not in line and 'Schedule:' not in line and not line.startswith('('):
                # Check if disaster project
                if not any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                    capital_design_projects.add(line)

# Count matches
count = 0
matched_list = []

for proj in capital_design_projects:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    
    if proj in funding_projects or proj_clean in funding_projects:
        count += 1
        amount = funding_projects.get(proj) or funding_projects.get(proj_clean, 0)
        matched_list.append({'Project_Name': proj, 'Amount': amount})

result = {'count': count, 'matches': matched_list}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
