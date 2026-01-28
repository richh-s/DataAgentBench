code = """import json
import re

# Load funding data from the file path stored in the variable
funding_file = var_functions.query_db:36
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from the file path stored in the variable  
civic_file = var_functions.query_db:24
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract funding project names
funding_names = [r['Project_Name'] for r in funding_records]

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    section_end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = text.find(marker, design_start)
        if pos > 0 and pos < section_end:
            section_end = pos
    
    design_section = text[design_start:section_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line2 = line.strip().lower()
        
        # Skip empty lines
        if not line2:
            continue
        
        # Skip lines with status/schedule keywords (common patterns)
        skip_patterns = ['updates:', 'schedule:', 'advertise:', 'begin construction', 'complete design', 'final design', 'estimated schedule:', 'staff', 'city', 'project is'
        ]
        
        skip = False
        for pattern in skip_patterns:
            if pattern in line2:
                skip = True
                break
        
        if skip:
            continue
            
        # Skip metadata lines
        meta_patterns = ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid', '•']
        
        for pattern in meta_patterns:
            if line2.startswith(pattern):
                skip = True
                break
                
        if skip:
            continue
        
        # Skip if line looks like a date range or schedule item
        if re.match(r'\d{4}(-\w+)?', line2) or 'spring' in line2 or 'summer' in line2 or 'fall' in line2 or 'winter' in line2:
            continue
        
        # This looks like a project name - convert back to title case
        project_name = line.strip().title()
        if project_name and project_name not in design_projects and len(project_name) > 10:
            design_projects.append(project_name)

# Match design projects with funding data
matched_projects = []

for design_project in design_projects:
    design_clean = design_project.lower()
    
    for funding_project in funding_names:
        funding_clean = funding_project.lower()
        
        # Check for matches (exact, or core name without suffixes/prefixes)
        # Remove parenthetical suffixes like (FEMA Project)
        design_core = re.sub(r'\s*\([^)]+\)$', '', design_clean).strip()
        funding_core = re.sub(r'\s*\([^)]+\)$', '', funding_clean).strip()
        
        if (design_clean == funding_clean or design_core == funding_core or 
            design_core in funding_core or funding_core in design_core):
            if design_project not in matched_projects:
                matched_projects.append(design_project)

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
