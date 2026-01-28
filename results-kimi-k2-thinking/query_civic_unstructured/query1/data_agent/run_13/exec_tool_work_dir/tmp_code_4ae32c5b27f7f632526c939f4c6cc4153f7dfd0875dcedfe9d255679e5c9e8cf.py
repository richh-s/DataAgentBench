code = """import json
import re

# Load funding data
f_file_path = var_functions.query_db:46
with open(f_file_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
c_file_path = var_functions.query_db:54
with open(c_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract funding project names
funding_names = [record['Project_Name'] for record in funding_records]

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find the design section
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find where design section ends
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
    
    design_section = text[design_start:section_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        lower_line = line_clean.lower()
        
        # Skip lines with status/schedule keywords
        skip_keywords = [
            'updates:', 'schedule:', 'advertise:', 'begin construction',
            'complete design', 'final design', 'estimated schedule:', 
            'staff', 'city', 'project is', 'project schedule', 'project description'
        ]
        
        should_skip = any(keyword in lower_line for keyword in skip_keywords)
        
        # Skip metadata lines
        meta_prefixes = [
            'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:',
            'agenda', 'item', 'page', 'public works', 'commission', '(cid', '('
        ]
        
        should_skip = should_skip or any(lower_line.startswith(prefix) for prefix in meta_prefixes)
        
        if should_skip:
            continue
        
        # Skip lines that look like schedule dates
        if re.search(r'\d{4}', lower_line) or any(season in lower_line for season in ['spring', 'summer', 'fall', 'winter']):
            if len(line_clean.split()) <= 4:  # Likely just a date phrase
                continue
        
        # This looks like a project name - convert to title case
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
        
        # Check for matches at different levels
        is_match = (
            design_clean == funding_clean or
            design_core == funding_core or
            design_core in funding_core or
            funding_core in design_core
        )
        
        if is_match and design_project not in matched_projects:
            matched_projects.append(design_project)

# Count the results
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
