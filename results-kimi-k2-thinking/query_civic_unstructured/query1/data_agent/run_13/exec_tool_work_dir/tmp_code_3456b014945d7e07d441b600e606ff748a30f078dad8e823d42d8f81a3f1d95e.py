code = """import json

f_file = var_functions.query_db:0
c_file = var_functions.query_db:5

with open(f_file, 'r') as f:
    funding_records = json.load(f)

with open(c_file, 'r') as f:
    civic_docs = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find where the design section starts
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find where design section ends
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
            
        # Only process lines after cid markers (these contain actual content)
        if 'cid:' in line2 or '•' in line2:
            continue
            
        # Skip lines with status/schedule keywords
        keywords = ['updates:', 'schedule:', 'advertise:', 'begin construction', 
                   'complete design', 'final design', 'staff', 'city', 'project is',
                   'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:',
                   'agenda', 'item', 'page', 'public works', 'commission']
        
        is_status_line = any(k in line2 for k in keywords)
        
        # This appears to be a project name
        if not is_status_line and not line2.startswith('(') and len(line2) > 10:
            # Convert back to title case for matching
            project_name = line.strip().title()
            if project_name not in design_projects:
                design_projects.append(project_name)

# Match design projects with funding data
matched_projects = []

for design_project in design_projects:
    # Check for exact or partial match with funding projects
    for funding_project in funding_names:
        design_clean = design_project.lower().replace('project', '').strip()
        funding_clean = funding_project.lower().replace('project', '').strip()
        
        # Remove parenthetical suffixes for matching
        design_core = design_clean.split('(')[0].strip()
        funding_core = funding_clean.split('(')[0].strip()
        
        # Check if design project matches any funding project
        match = False
        if design_project.lower() == funding_project.lower():
            match = True
        elif design_core == funding_core:
            match = True
        elif design_core in funding_core:
            match = True
        elif funding_core in design_core:
            match = True
            
        if match:
            if design_project not in matched_projects:
                matched_projects.append(design_project)

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
