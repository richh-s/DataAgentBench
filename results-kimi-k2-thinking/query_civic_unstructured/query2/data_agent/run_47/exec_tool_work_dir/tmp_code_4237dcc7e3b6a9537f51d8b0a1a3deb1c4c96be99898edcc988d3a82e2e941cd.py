code = """import json
import re

# Load the civic documents data
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Processing {len(civic_docs)} documents...")

# Function to extract projects from text
def extract_completed_projects(text):
    projects = []
    
    # Look for completion statements
    # Pattern 1: "Construction was completed, November 2022" 
    # Pattern 2: "Complete Construction: Summer 2023"
    # Pattern 3: "Complete: Summer 2023"
    
    # Find project blocks
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name patterns (typically title case, not too short)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and
            not line.startswith('-') and
            not 'Project Description' in line and
            not 'Project Updates' in line and
            not 'Project Schedule' in line and
            not ':' in line and
            (line.istitle() or (sum(1 for c in line if c.isupper()) > 5))):
            
            # This might be a project name
            current_project = line
            continue
        
        # If we have a current project, look for completion dates
        if current_project:
            lower_line = line.lower()
            
            # Check if it's park-related
            is_park_related = 'park' in current_project.lower()
            
            # Look for completion in 2022
            if '2022' in line and ('complet' in lower_line or 'construction was' in lower_line):
                if 'completed' in lower_line or 'complet' in lower_line:
                    # Extract the date
                    date_match = re.search(r'(\w+\s+2022)', line)
                    if date_match:
                        completion_date = date_match.group(1)
                        
                        project_info = {
                            'Project_Name': current_project,
                            'status': 'completed',
                            'et': completion_date,
                            'topic': 'park' if is_park_related else None,
                            'is_park_related': is_park_related
                        }
                        projects.append(project_info)
                        current_project = None  # Reset after finding completion
    
    return projects

# Extract all completed projects from all documents
all_completed_projects = []
for doc in civic_docs:
    projects = extract_completed_projects(doc['text'])
    all_completed_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = [p for p in all_completed_projects if p['is_park_related'] and '2022' in p['et']]

print(f"Found {len(park_projects_2022)} park-related projects completed in 2022:")
for proj in park_projects_2022:
    print(f"  - {proj['Project_Name']}: {proj['et']}")

print("__RESULT__:")
print(json.dumps(park_projects_2022, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
