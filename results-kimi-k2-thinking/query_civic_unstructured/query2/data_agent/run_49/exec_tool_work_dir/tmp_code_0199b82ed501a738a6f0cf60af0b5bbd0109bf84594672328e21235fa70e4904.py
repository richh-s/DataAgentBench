code = """import json
import re

# Load the full result from the query
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    documents = json.load(f)

print('Found', len(documents), 'documents')

# Function to extract project information from text
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    project_text = ''
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        skip_starts = ['(', 'Page', 'Agenda', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects']
        should_skip = False
        for pattern in skip_starts:
            if line.startswith(pattern):
                should_skip = True
                break
        
        if should_skip:
            continue
            
        # Check if this looks like a project name
        if 'Project' not in line and (line.istitle() or (line.isupper() and len(line.split()) > 1)) and 10 < len(line) < 150:
            next_text = ' '.join(lines[i+1:i+4]).lower()
            project_indicators = ['updates:', 'project description:', 'project schedule', 'complete construction:']
            
            is_project = False
            for indicator in project_indicators:
                if indicator in next_text:
                    is_project = True
                    break
            
            if is_project:
                if current_project and project_text:
                    projects.append({'name': current_project, 'text': project_text})
                
                current_project = line
                project_text = line + '\n'
                continue
        
        if current_project:
            project_text += line + '\n'
    
    if current_project and project_text:
        projects.append({'name': current_project, 'text': project_text})
    
    return projects

all_projects = []
for doc in documents:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

print('Extracted', len(all_projects), 'potential projects')

park_projects_2022 = []

for project in all_projects:
    name = project['name']
    text_lower = project['text'].lower()
    
    park_keywords = ['park', 'playground', 'bluffs', 'canyon', 'recreation']
    is_park = False
    for keyword in park_keywords:
        if keyword in name.lower() or keyword in text_lower:
            is_park = True
            break
    
    completed_2022 = 'completed' in text_lower and '2022' in text_lower
    
    if is_park and completed_2022:
        match = re.search(r'completed[^\n]*2022[^\n]*', text_lower, re.IGNORECASE)
        status_info = match.group(0).strip() if match else 'completed in 2022'
        
        park_projects_2022.append({
            'name': name,
            'status': status_info
        })

print('Found', len(park_projects_2022), 'park projects completed in 2022')

result_json = json.dumps(park_projects_2022, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
