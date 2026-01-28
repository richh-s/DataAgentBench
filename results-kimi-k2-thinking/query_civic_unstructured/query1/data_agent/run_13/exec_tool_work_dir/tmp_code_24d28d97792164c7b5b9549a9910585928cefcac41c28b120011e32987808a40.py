code = """import json
import re

# Get file paths from the stored variables
funding_path = str(var_functions.query_db:64)
civic_path = str(var_functions.query_db:54)

# Load funding data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project names from funding data
funding_names = [record['Project_Name'] for record in funding_records]

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if not text:
        continue
    
    # Find where the "Capital Improvement Projects (Design)" section starts
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find where the design section ends (look for next major section)
    section_end = len(text)
    end_markers = [
        'capital improvement projects (construction)',
        'capital improvement projects (not started)',
        'disaster recovery projects'
    ]
    
    for marker in end_markers:
        pos = text.find(marker, design_start)
        if pos != -1 and pos < section_end:
            section_end = pos
    
    # Extract the design section text
    design_section = text[design_start:section_end]
    
    # Process each line to extract project names
    for line in design_section.split('\n'):
        clean_line = line.strip()
        if not clean_line or len(clean_line) < 10:
            continue
        
        lower_line = clean_line.lower()
        
        # Skip lines that contain status/schedule/update information
        if 'updates:' in lower_line:
            continue
        if 'schedule:' in lower_line:
            continue
        if 'advertise:' in lower_line:
            continue
        if 'staff' in lower_line and 'project' not in lower_line:
            continue
        if 'city' in lower_line and len(clean_line.split()) < 8:
            continue
        
        # Skip metadata/document structure lines
        if lower_line.startswith('to:'):
            continue
        if lower_line.startswith('prepared'):
            continue
        if lower_line.startswith('approved'):
            continue
        if '(cid' in lower_line:
            continue
        if clean_line.startswith('('):
            continue
        if 'agenda' in lower_line and len(clean_line.split()) < 5:
            continue
        if 'commission' in lower_line and len(clean_line.split()) < 5:
            continue
        
        # Skip short lines that are likely just dates
        if re.search(r'\d{4}', lower_line) and len(clean_line.split()) <= 4:
            continue
        
        # Skip lines that are just season references
        if lower_line in ['spring 2023', 'summer 2023', 'fall 2023', 'winter 2024']:
            continue
        
        # This appears to be a project name - convert to title case
        project_name = clean_line.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match capital design projects with funding data
matched_projects = []

for design_project in design_projects:
    design_lower = design_project.lower()
    design_core = re.sub(r'\s*\([^)]+\)$', '', design_lower).strip()
    
    for funding_project in funding_names:
        funding_lower = funding_project.lower()
        funding_core = re.sub(r'\s*\([^)]+\)$', '', funding_lower).strip()
        
        # Check for matches
        if design_lower == funding_lower:
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break
        elif design_core == funding_core:
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break
        elif design_core in funding_core and len(design_core) > 15:
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break
        elif funding_core in design_core and len(funding_core) > 15:
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break

# Count matched projects
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
