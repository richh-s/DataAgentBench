code = """import json
import re

# Load the full result from the query
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    documents = json.load(f)

print(f"Found {len(documents)} documents")

# Function to extract project information from text
def extract_projects(text):
    projects = []
    
    # Look for project sections - they often start with a project name in a specific format
    # Common patterns:
    # 1. Project name on its own line, followed by updates
    # 2. Project name followed by parentheses with description
    # 3. Bullet points with project names
    
    lines = text.split('\n')
    current_project = None
    project_text = ""
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - they typically:
        # - Are title case
        # - Are followed by a line with "(cid:" or "Updates:" or "Project Description:"
        # - Mention park, playground, etc.
        
        # Check if this looks like a project name
        if (len(line) > 10 and 
            (line.istitle() or (line.isupper() and len(line.split()) > 1)) and
            not line.startswith('(') and 
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            not line.startswith('To:') and
            not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and
            not line.startswith('Date prepared:') and
            not line.startswith('Meeting date:') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED ACTION:') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Capital Improvement Projects') and
            not line.startswith('Disaster Recovery Projects') and
            not line.startswith('FEMA') and
            'Project' not in line):
            
            # Check if next line suggests this is a project
            next_lines = ' '.join(lines[i+1:i+4]).lower()
            if ('updates:' in next_lines or 
                'project description:' in next_lines or 
                'updates' in next_lines or
                'project schedule' in next_lines or
                'complete construction:' in next_lines):
                
                # Save previous project if exists
                if current_project and project_text:
                    projects.append({
                        'name': current_project,
                        'text': project_text
                    })
                
                # Start new project
                current_project = line
                project_text = line + "\n"
                continue
        
        # If we're in a project, accumulate text
        if current_project:
            project_text += line + "\n"
    
    # Add the last project
    if current_project and project_text:
        projects.append({
            'name': current_project,
            'text': project_text
        })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in documents:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

print(f"Extracted {len(all_projects)} potential projects")

# Analyze projects for park-related and completed in 2022
park_projects_2022 = []

for project in all_projects:
    name = project['name']
    text = project['text'].lower()
    
    # Check if park-related
    is_park = any(keyword in name.lower() or keyword in text for keyword in 
                  ['park', 'playground', 'bluffs', 'canyon', 'recreation'])
    
    # Check if completed in 2022
    completed_2022 = 'completed' in text and '2022' in text
    
    if is_park and completed_2022:
        # Get more specific status
        status_match = re.search(r'(?:construction was )?completed[^\n]*2022[^\n]*', text, re.IGNORECASE)
        if status_match:
            status_info = status_match.group(0).strip()
        else:
            status_info = "completed in 2022"
            
        park_projects_2022.append({
            'name': name,
            'status': status_info
        })

print(f"Found {len(park_projects_2022)} park projects completed in 2022")
for proj in park_projects_2022:
    print(f"- {proj['name']}: {proj['status']}")

# Print the result in the required format
result_json = json.dumps(park_projects_2022, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
