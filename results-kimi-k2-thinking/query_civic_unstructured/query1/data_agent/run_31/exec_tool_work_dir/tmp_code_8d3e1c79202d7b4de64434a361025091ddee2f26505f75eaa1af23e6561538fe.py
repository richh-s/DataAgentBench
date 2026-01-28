code = """import json
import re

# Read the funding data
funding_file = var_functions.query_db:2
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:2

# Read the civic docs data
civic_file = var_functions.query_db:5
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:5

# Function to extract projects from civic docs text
def extract_projects_from_text(text):
    projects = []
    
    # Look for project sections
    # Patterns like "Project_Name:", or bullet points with project names
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project name patterns (often bolded or with special characters)
        # Try to detect project names based on common patterns
        if any(keyword in line.lower() for keyword in ['project', 'road', 'avenue', 'drive', 'park', 'beach', 'canyon', 'drain', 'bridge']):
            # This might be a project name or section header
            if len(line) < 100 and not line.startswith('(') and not line.startswith('•'):
                # Check if next lines contain status info
                project_name = line
                status = None
                project_type = None
                
                # Look ahead for status and type
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'design' in next_line:
                        status = 'design'
                    elif 'completed' in next_line:
                        status = 'completed'
                    elif 'not started' in next_line:
                        status = 'not started'
                        
                    if 'capital' in next_line:
                        project_type = 'capital'
                    elif 'disaster' in next_line:
                        project_type = 'disaster'
                
                if status and project_type:
                    projects.append({
                        'Project_Name': project_name,
                        'status': status,
                        'type': project_type
                    })
    
    return projects

# Extract all projects from civic docs
all_projects = []
for doc in civic_docs:
    if 'text' in doc:
        projects = extract_projects_from_text(doc['text'])
        all_projects.extend(projects)

# Filter for capital projects with design status
capital_design_projects = [p for p in all_projects if p['type'] == 'capital' and p['status'] == 'design']

# Get project names from funding data > $50,000
funding_project_names = [f['Project_Name'] for f in funding_data]

# Match projects - look for exact or partial matches
def match_project_name(proj_name, funding_names):
    """Match project name with funding names"""
    proj_name_clean = proj_name.lower().strip()
    
    for funding_name in funding_names:
        funding_name_clean = funding_name.lower().strip()
        # Check if project name is contained in funding name or vice versa
        if proj_name_clean in funding_name_clean or funding_name_clean in proj_name_clean:
            return funding_name
    return None

# Find matching projects with funding > $50,000
matched_projects = []
for proj in capital_design_projects:
    matched_name = match_project_name(proj['Project_Name'], funding_project_names)
    if matched_name:
        # Find the funding record
        for funding_rec in funding_data:
            if funding_rec['Project_Name'] == matched_name:
                matched_projects.append({
                    'project_name': proj['Project_Name'],
                    'funding_name': matched_name,
                    'amount': int(funding_rec['Amount']),
                    'funding_source': funding_rec['Funding_Source']
                })
                break

# Count
count = len(matched_projects)

# Print result in required format
result = {
    'count': count,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
