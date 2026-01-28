code = """import json
import re

# Read the civic documents
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Helper function to extract projects from text
def extract_projects_from_text(text):
    projects = []
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    current_project = None
    project_status = None
    
    for line in lines:
        line = line.strip()
        
        # Look for status headers
        if 'Capital Improvement Projects (Design)' in line or 'Disaster Recovery Projects (Design)' in line:
            project_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line or 'Disaster Recovery Projects (Construction)' in line:
            project_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line or 'Disaster Recovery Projects (Not Started)' in line:
            project_status = 'not started'
        elif 'Capital Improvement Projects (Completed)' in line or 'Disaster Recovery Projects (Completed)' in line:
            project_status = 'completed'
            
        # Look for project names (they typically appear as title case lines followed by bullet points)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and not line.startswith('■') and len(line) > 10:
            # Check if this is likely a project name (not a header or other text)
            if not any(header in line for header in ['Public Works', 'Commission', 'Agenda', 'Item', 'To:', 'Prepared', 'Approved', 'Date', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'City Council', 'Page']):
                # If we were tracking a project, save it
                if current_project and project_status:
                    projects.append({
                        'Project_Name': current_project,
                        'Status': project_status,
                        'Topics': extract_topics(current_project)
                    })
                current_project = line
                
    # Add the last project
    if current_project and project_status:
        projects.append({
            'Project_Name': current_project,
            'Status': project_status,
            'Topics': extract_topics(current_project)
        })
        
    return projects

def extract_topics(project_name):
    topics = []
    project_lower = project_name.lower()
    
    topic_keywords = [
        'emergency', 'fema', 'fire', 'warning', 'siren', 'disaster', 'storm', 'drain', 
        'road', 'street', 'highway', 'bridge', 'park', 'playground', 'water', 
        'treatment', 'guardrail', 'slope', 'canyon', 'culvert', 'retaining', 'wall'
    ]
    
    for keyword in topic_keywords:
        if keyword in project_lower:
            topics.append(keyword)
            
    return ','.join(topics) if topics else ''

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Filter projects related to 'emergency' or 'FEMA'
filtered_projects = [
    p for p in all_projects 
    if 'emergency' in p['Project_Name'].lower() or 'fema' in p['Project_Name'].lower()
]

# Also look for projects in funding data that have FEMA in their name
fema_funding_projects = [
    f for f in funding_data 
    if 'fema' in f['Project_Name'].lower() and f['Project_Name'] not in [p['Project_Name'] for p in filtered_projects]
]

# For FEMA projects in funding data not found in civic docs, add them with unknown status
for f in fema_funding_projects:
    filtered_projects.append({
        'Project_Name': f['Project_Name'],
        'Status': 'not specified',
        'Topics': 'fema'
    })

results = {
    'num_total_projects': len(all_projects),
    'num_filtered_projects': len(filtered_projects),
    'sample_projects': filtered_projects[:5] if filtered_projects else []
}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
