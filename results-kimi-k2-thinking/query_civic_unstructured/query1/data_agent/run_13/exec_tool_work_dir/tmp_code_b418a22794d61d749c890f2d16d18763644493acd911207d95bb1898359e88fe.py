code = """import json, re

# Load the funding data - projects > $50,000
with open(var_functions.query_db:103[2]) as f:
    funding_data = json.load(f)

# Load civic documents data
with open(var_functions.query_db:54[2]) as f:
    civic_docs = json.load(f)

# Extract funding project names (lowercase for matching)
funding_names = [r['Project_Name'].lower() for r in funding_data]

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    # Get the text content of the document
    text = doc.get('text', '').lower()
    if not text:
        continue
    
    # Find the "Capital Improvement Projects (Design)" section
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find where this section ends (look for next major section)
    section_end = len(text)
    next_markers = [
        'capital improvement projects (construction)',
        'capital improvement projects (not started)',
        'disaster recovery projects'
    ]
    
    for marker in next_markers:
        marker_pos = text.find(marker, design_start + 1)
        if marker_pos != -1 and marker_pos < section_end:
            section_end = marker_pos
    
    # Extract the design section text
    design_section = text[design_start:section_end]
    
    # Split into lines and extract project names
    lines = design_section.split('\n')
    for line in lines:
        clean_line = line.strip()
        if not clean_line or len(clean_line) < 10:
            continue
        
        lower_line = clean_line.lower()
        
        # Skip status/schedule/update lines
        if any(keyword in lower_line for keyword in ['updates:', 'schedule:', 'advertise:', 'project schedule', 'project description']):
            continue
        
        # Skip metadata lines
        if any(lower_line.startswith(prefix) for prefix in ['to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission']):
            continue
        
        # Skip CID markers and similar
        if '(cid' in lower_line or clean_line.startswith('('):
            continue
        
        # Skip short lines with years/dates
        if re.search(r'\d{4}', lower_line) and len(clean_line.split()) <= 4:
            continue
        
        # Skip lines that are just update indicators
        if clean_line == '•':
            continue
            
        # This looks like a project name - convert to title case
        project_name = clean_line.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match design projects with funding data
matched_projects = []

for design_project in design_projects:
    # Clean the name for matching (remove parenthetical suffixes)
    design_clean = re.sub(r'\s*\([^)]+\)$', '', design_project.lower()).strip()
    
    for funding_project in funding_names:
        # Clean the funding project name too
        funding_clean = re.sub(r'\s*\([^)]+\)$', '', funding_project).strip()
        
        # Check for exact match or core name match
        if (design_project.lower() == funding_project or 
            design_clean == funding_clean or
            design_clean in funding_clean):
            if design_project not in matched_projects:
                matched_projects.append(design_project)
                break

# Count the results
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:98': 'file_storage/functions.query_db:98.json', 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:103': 'file_storage/functions.query_db:103.json'}

exec(code, env_args)
