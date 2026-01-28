code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project info from text
projects = []

for doc in civic_docs_data:
    text = doc['text']
    filename = doc['filename']
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    # Look for project names (typically title case or all caps, followed by schedule updates)
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip common header/footer lines
        if any(skip in line for skip in ['Page ', 'Item #', 'Agenda Item', 'Public Works', 'Commission', '-----']):
            continue
        
        # Look for project names (heuristic: longer than 15 chars, starts with capital letter, not a common phrase)
        if (len(line) > 15 and 
            line[0].isupper() and 
            not line.startswith('To:') and 
            not line.startswith('Prepared by:') and 
            not line.startswith('Approved by:') and
            not line.startswith('Subject:') and
            'RECOMMENDED ACTION' not in line and
            'DISCUSSION' not in line and
            'Capital Improvement Projects' not in line and
            'Disaster Recovery Projects' not in line):
            
            # Check if next few lines contain project indicators
            next_lines = '\n'.join(lines[i+1:i+4])
            if ('Updates:' in next_lines or 'Schedule' in next_lines or 'Project Schedule' in next_lines):
                if current_project:
                    projects.append(current_project)
                current_project = {
                    'Project_Name': line,
                    'filename': filename,
                    'st': '',
                    'status': '',
                    'type': 'capital'  # default
                }
                continue
        
        # Extract dates if we're in a project
        if current_project:
            # Look for date patterns like "Spring 2022", "2022-Spring", "2022-03"
            if re.search(r'(Spring|Summer|Fall|Winter)\s+2022', line, re.IGNORECASE):
                if not current_project['st']:
                    current_project['st'] = line
            elif re.search(r'2022-(Spring|Summer|Fall|Winter)', line, re.IGNORECASE):
                if not current_project['st']:
                    current_project['st'] = line
            elif re.search(r'2022-(0[3-5]|Mar|Apr|May)', line, re.IGNORECASE):
                if not current_project['st']:
                    current_project['st'] = line
            
            # Detect status
            if 'under construction' in line.lower():
                current_project['status'] = 'construction'
            elif 'design' in line.lower() and ('complete' in line.lower() or 'phase' in line.lower()):
                current_project['status'] = 'design'
            elif 'not started' in line.lower():
                current_project['status'] = 'not started'
            
            # Detect type
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'disaster' in line.lower():
                current_project['type'] = 'disaster'
    
    if current_project:
        projects.append(current_project)

# Filter projects that started in Spring 2022
spring_2022_projects = []
for p in projects:
    st = p.get('st', '').lower()
    # Check for Spring 2022 patterns
    if ('2022' in st and 'spring' in st) or \
       ('2022' in st and any(month in st for month in ['mar', 'apr', 'may', '03', '04', '05'])):
        spring_2022_projects.append(p)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects': spring_2022_projects,
    'count': len(spring_2022_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
