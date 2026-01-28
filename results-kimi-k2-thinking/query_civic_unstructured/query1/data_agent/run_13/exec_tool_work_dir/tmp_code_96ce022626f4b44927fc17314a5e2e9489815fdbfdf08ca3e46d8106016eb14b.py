code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_project_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Find capital improvement projects in design section
    design_start = lower_text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find end of design section
    construction_start = lower_text.find('capital improvement projects (construction)', design_start)
    not_started_start = lower_text.find('capital improvement projects (not started)', design_start)
    
    end_pos = construction_start if construction_start != -1 else len(lower_text)
    if not_started_start != -1 and not_started_start < end_pos:
        end_pos = not_started_start
    
    design_section = lower_text[design_start:end_pos]
    
    # Extract project names from design section
    # Look for lines that are likely project names
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip status/update lines
        if any(x in line for x in ['updates:', 'schedule:', 'advertise:', 'begin', 'complete:', 'staff', 'city', 'project is', 'estimated schedule', 'complete design']):
            continue
        
        # Skip metadata lines
        if any(line.startswith(x) for x in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', '(cid', '(', '•']):
            continue
        
        # This looks like a project name - convert back to title case
        project_name = line.title().strip()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match with funding projects > $50,000
matched = []

for design_project in design_projects:
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_project).strip().lower()
    
    for funding_project in funding_project_names:
        clean_funding = re.sub(r'\s*\([^)]+\)$', '', funding_project).strip().lower()
        
        # Check for match (exact or partial)
        if (design_project.lower() == clean_funding or
            clean_design == clean_funding or
            clean_design in clean_funding or
            clean_funding in clean_design):
            if design_project not in matched:
                matched.append(design_project)

# Print result
result = {
    'count': len(matched),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
