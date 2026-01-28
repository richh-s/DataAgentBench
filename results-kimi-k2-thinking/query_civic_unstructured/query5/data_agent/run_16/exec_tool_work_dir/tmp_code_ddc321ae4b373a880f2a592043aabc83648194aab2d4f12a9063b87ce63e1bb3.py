code = """import json
import re

# Access the stored variable directly
civic_docs_result = var_functions.query_db:4

# Since it might be a file path or the actual data, let's handle both cases
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    # It's a file path
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    # It's the actual data
    civic_docs = civic_docs_result

# Function to extract project information
def extract_disaster_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for project lines
        is_project_line = False
        if line.endswith('Project') or 'Project:' in line or re.match(r'^[A-Z].*Project$', line):
            is_project_line = True
        
        if is_project_line:
            proj_text = line + '\n'
            # Look ahead for context
            for j in range(i+1, min(i+8, len(lines))):
                next_line = lines[j].strip()
                if next_line:
                    proj_text += next_line + '\n'
            
            projects.append({
                'name': line,
                'text': proj_text
            })
    
    return projects

# Extract disaster projects starting in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_disaster_projects(text)
    
    for proj in projects:
        name = proj.get('name', '')
        proj_text = proj.get('text', '')
        
        # Check if disaster-related
        name_lower = name.lower()
        text_lower = proj_text.lower()
        
        is_disaster = any(keyword in name_lower or keyword in text_lower for keyword in [
            'disaster', 'fema', 'fire', 'emergency', 'woolsey', 'caljpia', 'caloes', 'recovery'
        ])
        
        if is_disaster and '2022' in proj_text:
            disaster_projects_2022.append({
                'project_name': name,
                'type': 'disaster',
                'start_date': '2022'
            })

# Also look specifically for FEMA/CalJPIA/CalOES project suffixes
for doc in civic_docs:
    text = doc.get('text', '')
    # Find patterns like (FEMA Project), (CalJPIA Project), etc.
    pattern = r'([^(]+)\s*\(([^)]*(?:FEMA|CalJPIA|CalOES)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    for match in matches:
        proj_name = match[0].strip()
        if proj_name and len(proj_name) > 3 and '2022' in text:
            disaster_projects_2022.append({
                'project_name': proj_name,
                'type': 'disaster',
                'start_date': '2022'
            })

# Remove duplicates based on project name
unique_projects = {}
for proj in disaster_projects_2022:
    name = proj['project_name'].strip()
    if name and name not in unique_projects:
        unique_projects[name] = proj

disaster_projects_2022_clean = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': disaster_projects_2022_clean,
    'count': len(disaster_projects_2022_clean)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
