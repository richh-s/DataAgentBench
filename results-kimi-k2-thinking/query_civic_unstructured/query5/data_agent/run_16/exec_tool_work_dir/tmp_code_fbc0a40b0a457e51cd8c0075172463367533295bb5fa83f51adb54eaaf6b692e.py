code = """import json
import re

# Load the civic documents from the file path stored in variable
civic_docs_file = var_functions.query_db:4

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project indicators
        if (line.endswith('Project') or 
            'Project:' in line or 
            (line.startswith('2022') and 'Project' in line) or
            re.match(r'^[A-Z].*Project$', line)):
            
            # Look ahead to get more context about this project
            project_text = line + '\n'
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if next_line:
                    project_text += next_line + '\n'
                    # Check for dates
                    if '2022' in next_line and any(keyword in next_line.lower() for keyword in ['schedule', 'start', 'begin', 'complete', 'design']):
                        break
            
            projects.append({
                'name': line,
                'text': project_text
            })
    
    return projects

# Extract disaster projects that started in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    
    for proj in projects:
        name = proj.get('name', '').lower()
        proj_text = proj.get('text', '').lower()
        
        # Check if disaster-related
        is_disaster = any(keyword in name or keyword in proj_text for keyword in [
            'disaster', 'fema', 'fire', 'emergency', 'woolsey', 'caljpia', 'caloes', 'recovery'
        ])
        
        if is_disaster and '2022' in proj.get('text', ''):
            disaster_projects_2022.append({
                'project_name': proj.get('name'),
                'type': 'disaster',
                'start_date': '2022'
            })

# Also look for FEMA/CalJPIA/CalOES project suffixes
fema_pattern = r'\([^)]*(FEMA|CalJPIA|CalOES)[^)]*Project[^)]*\)'

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        match = re.search(fema_pattern, line, re.IGNORECASE)
        if match:
            # Extract project name (remove the suffix)
            proj_name = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if proj_name and len(proj_name) > 5:
                # Check for 2022 in surrounding context
                context_start = max(0, text.index(line) - 200)
                context_end = min(len(text), text.index(line) + 200)
                context = text[context_start:context_end]
                
                if '2022' in context:
                    disaster_projects_2022.append({
                        'project_name': proj_name,
                        'type': 'disaster',
                        'start_date': '2022'
                    })

# Remove duplicates
unique_projects = {}
for proj in disaster_projects_2022:
    name = proj['project_name']
    if name and name not in unique_projects:
        unique_projects[name] = proj

disaster_projects_2022_unique = list(unique_projects.values())

result = json.dumps({
    'disaster_projects_2022': disaster_projects_2022_unique,
    'count': len(disaster_projects_2022_unique)
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
