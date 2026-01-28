code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:46
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
civic_file = var_functions.query_db:24
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

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
    
    # Split into lines and process
    for line in design_section.split('\n'):
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        lower_line = line_clean.lower()
        
        # Skip lines with status/schedule keywords
        if any(kw in lower_line for kw in ['updates:', 'schedule:', 'advertise:', 'begin construction', 'complete design', 'staff', 'city', 'project is']):
            continue
        
        # Skip metadata lines
        if any(lower_line.startswith(prefix) for prefix in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid', '(']):
            continue
        
        # Skip lines with years (likely schedule info)
        if re.search(r'\d{4}', lower_line):
            continue
        
        # This appears to be a project name
        project_name = line_clean.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match design projects with funding data
matched_projects = []

for design_project in design_projects:
    design_clean = design_project.lower()
    design_core = re.sub(r'\s*\([^)]+\)$', '', design_clean).strip()
    
    for funding_project in funding_names:
        funding_clean = funding_project.lower()
        funding_core = re.sub(r'\s*\([^)]+\)$', '', funding_clean).strip()
        
        # Check for matches
        if (design_clean == funding_clean or 
            design_core == funding_core or 
            design_core in funding_core or 
            funding_core in design_core):
            if design_project not in matched_projects:
                matched_projects.append(design_project)

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
