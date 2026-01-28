code = """import json
import re

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    # Look for patterns that indicate project sections
    # Common patterns in the documents
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Look for project names - they often appear as bolded or titled items
        # Pattern 1: Lines ending with "Project" or containing "Project:" or similar
        if (line.endswith('Project') or 
            'Project:' in line or 
            line.startswith('2022') and 'Project' in line or
            re.match(r'^[A-Z].*Project$', line)):
            
            # Save previous project if exists
            if current_project and current_project.get('name'):
                projects.append(current_project)
            
            current_project = {'name': line, 'text': line + '\n'}
            continue
        
        # Pattern 2: Look for disaster/FEMA indicators in project names
        if current_project and current_project.get('name'):
            # Add to project text
            current_project['text'] += line + '\n'
            
            # Check for date patterns
            if '2022' in line and ('Schedule' in line or 'Start' in line or 'Complete' in line):
                if 'st' not in current_project:
                    # Extract date mentions
                    date_match = re.search(r'(2022[-\s]\w+)', line)
                    if date_match:
                        current_project['st'] = date_match.group(1)
            
            # Check for status
            status_patterns = ['design', 'completed', 'not started', 'construction', 'advertise', 'begin']
            for status in status_patterns:
                if status.lower() in line.lower():
                    if 'status' not in current_project:
                        current_project['status'] = status
                    break
    
    # Add the last project
    if current_project and current_project.get('name'):
        projects.append(current_project)
    
    # Filter and enrich projects
    disaster_projects = []
    for proj in projects:
        name = proj.get('name', '').lower()
        text = proj.get('text', '').lower()
        
        # Check if it's a disaster-related project
        is_disaster = (
            'disaster' in name or 'disaster' in text or
            'fema' in name or 'fema' in text or
            'fire' in name or 'fire' in text or
            'emergency' in name or 'emergency' in text or
            'woolsey' in name or 'woolsey' in text or
            'caljpia' in name or 'caljpia' in text or
            'caloes' in name or 'caloes' in text
        )
        
        if is_disaster:
            proj['type'] = 'disaster'
            # Look for year 2022 in the text
            if 'st' not in proj and '2022' in proj.get('text', ''):
                # Try to find any 2022 reference that might be a start date
                proj['st'] = '2022'
            disaster_projects.append(proj)
        else:
            # Check for capital improvement projects that might be disaster-related
            if 'recovery' in name or 'recovery' in text:
                proj['type'] = 'disaster'
                if 'st' not in proj and '2022' in proj.get('text', ''):
                    proj['st'] = '2022'
                disaster_projects.append(proj)
    
    return disaster_projects

# Process the civic documents
civic_docs_file = var_functions.query_db:4
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    
    for proj in projects:
        # Check if it started in 2022
        start_date = proj.get('st', '')
        if '2022' in str(start_date):
            disaster_projects_2022.append({
                'project_name': proj.get('name', ''),
                'type': proj.get('type', 'disaster'),
                'status': proj.get('status', ''),
                'start_date': start_date
            })

# Also look for projects with FEMA/CalJPIA/CalOES suffixes in the document text
# These are definitely disaster projects
fema_pattern = r'\([^)FEMA[^)]*?Project\)|\([^)CalJPIA[^)]*?Project\)|\([^)CalOES[^)]*?Project\)'

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find lines containing disaster project names with suffixes
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if re.search(fema_pattern, line, re.IGNORECASE):
            # Extract project name (usually before the parenthetical)
            proj_name = re.sub(r'\s*\([^)]*\)\s*$', '', line)
            if proj_name and len(proj_name) > 5:  # Avoid too short matches
                # Check if 2022 is mentioned nearby
                if '2022' in text[max(0, text.index(line)-200):min(len(text), text.index(line)+200)]:
                    disaster_projects_2022.append({
                        'project_name': proj_name,
                        'type': 'disaster',
                        'status': 'design',  # Default status
                        'start_date': '2022'
                    })

# Remove duplicates based on project name
unique_projects = {}
for proj in disaster_projects_2022:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

disaster_projects_2022 = list(unique_projects.values())

result = json.dumps({
    'disaster_projects_2022': disaster_projects_2022,
    'count': len(disaster_projects_2022)
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
