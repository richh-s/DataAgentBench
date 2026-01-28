code = """import json
import re
from collections import defaultdict

# Read the full MongoDB results
with open('var_functions.query_db:0', 'r') as f:
    mongo_docs = json.load(f)

# Read the funding data
with open('var_functions.query_db:2', 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding lookup by project name
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    funding_lookup[project_name] = {
        'Funding_Source': record['Funding_Source'],
        'Amount': record['Amount']
    }

# Function to extract projects from text
def extract_projects(text):
    projects = []
    
    # Pattern to find project names and their details
    # Looking for project names followed by status information
    lines = text.split('\n')
    
    current_project = None
    project_status = None
    project_type = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and common headers/footers
        if not line or line.startswith('Public Works') or line.startswith('Commission') or \
           line.startswith('Agenda Item') or line.startswith('Page'):
            continue
            
        # Look for project type headers
        if 'Capital Improvement Projects (Design)' in line:
            project_type = 'capital'
            project_status = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            project_type = 'capital'
            project_status = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            project_type = 'capital'
            project_status = 'not started'
            continue
        elif 'Disaster Recovery Projects' in line or 'Disaster Recovery Projects (Design)' in line:
            project_type = 'disaster'
            project_status = 'design'
            continue
        elif 'Disaster Recovery Projects (Construction)' in line:
            project_type = 'disaster'
            project_status = 'construction'
            continue
        elif 'Disaster Recovery Projects (Not Started)' in line:
            project_type = 'disaster'
            project_status = 'not started'
            continue
            
        # Look for project names - they typically start without bullet points
        # and are followed by updates or status
        if line and not line.startswith('(') and not line.startswith('•') and \
           not line.startswith('-') and not line.startswith('□') and \
           'Updates:' not in line and 'Schedule:' not in line and \
           'Project Description:' not in line and 'Project Schedule:' not in line:
            
            # Check if this looks like a project name (not too long, not a continuation)
            if len(line) < 150 and not line.endswith('.') and 
               ('Project' in line or 'Improvements' in line or 'Repair' in line or 
                'Maintenance' in line or 'Drainage' in line or 'Road' in line or
                'Bridge' in line or 'Culvert' in line or 'Park' in line):
                
                # Save previous project if any
                if current_project and project_status:
                    projects.append({
                        'Project_Name': current_project,
                        'status': project_status,
                        'type': project_type if project_type else 'unknown'
                    })
                
                current_project = line
                continue
    
    # Add the last project
    if current_project and project_status:
        projects.append({
            'Project_Name': current_project,
            'status': project_status,
            'type': project_type if project_type else 'unknown'
        })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in mongo_docs:
    projects = extract_projects(doc['text'])
    for proj in projects:
        proj['source_doc'] = doc['filename']
        # Check if project is related to emergency or FEMA
        text_lower = doc['text'].lower()
        proj_name_lower = proj['Project_Name'].lower()
        if 'emergency' in text_lower or 'fema' in text_lower or \
           'emergency' in proj_name_lower or 'fema' in proj_name_lower:
            all_projects.append(proj)

# Filter for projects specifically mentioning emergency or FEMA in their name or context
emergency_fema_projects = []
for proj in all_projects:
    proj_name_lower = proj['Project_Name'].lower()
    if 'emergency' in proj_name_lower or 'fema' in proj_name_lower:
        emergency_fema_projects.append(proj)

# Join with funding data
results = []
for proj in emergency_fema_projects:
    project_name = proj['Project_Name']
    funding_info = funding_lookup.get(project_name)
    
    if funding_info:
        results.append({
            'Project_Name': project_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': proj['status'],
            'Type': proj['type']
        })

# If no exact match, try partial matching
if not results:
    for proj in emergency_fema_projects:
        # Try to find funding by matching first part of project name
        proj_words = proj['Project_Name'].split()[:3]  # First 3 words
        for funding_proj, funding_info in funding_lookup.items():
            if all(word in funding_proj for word in proj_words):
                results.append({
                    'Project_Name': funding_proj,  # Use the funding table name
                    'Funding_Source': funding_info['Funding_Source'],
                    'Amount': funding_info['Amount'],
                    'Status': proj['status'],
                    'Type': proj['type']
                })
                break

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
