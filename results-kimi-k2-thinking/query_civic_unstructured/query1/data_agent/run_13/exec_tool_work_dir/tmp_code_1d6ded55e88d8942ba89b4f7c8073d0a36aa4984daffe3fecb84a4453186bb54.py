code = """import json
import re

# Load funding data
f_file = var_functions.query_db:0
with open(f_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
c_file = var_functions.query_db:5
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Get project names from funding
funding_names = [record['Project_Name'] for record in funding_data]

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find end of design section
    section_end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, design_start)
        if pos > 0 and pos < section_end:
            section_end = pos
    
    design_section = text[design_start:section_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line2 = line.strip().lower()
        
        if not line2:
            continue
        
        # Check for status/schedule keywords
        if any(kw in line2 for kw in ['updates:', 'schedule:', 'advertise:', 'begin construction', 'complete design', 'estimated schedule:', 'staff', 'city', 'project is']):
            continue
            
        # Check for metadata markers
        if line2.startswith(('to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid', '(', '•')):
            continue
            
        # Check if line contains a year (likely schedule info)
        if re.search(r'\d{4}', line2):
            continue
            
        # This is likely a project name - convert to title case
        project_name = line.strip().title()
        if project_name and project_name not in design_projects and len(project_name) > 10:
            design_projects.append(project_name)

# Match with funding projects
matched_projects = []

for design_project in design_projects:
    design_clean = design_project.lower()
    
    for funding_project in funding_names:
        funding_clean = funding_project.lower()
        
        # Remove parenthetical suffixes for matching
        design_core = re.sub(r'\s*\([^)]+\)$', '', design_clean).strip()
        funding_core = re.sub(r'\s*\([^)]+\)$', '', funding_clean).strip()
        
        if (design_clean == funding_clean or 
            design_core == funding_core or 
            design_core in funding_core or 
            funding_core in design_core):
            if design_project not in matched_projects:
                matched_projects.append(design_project)

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
