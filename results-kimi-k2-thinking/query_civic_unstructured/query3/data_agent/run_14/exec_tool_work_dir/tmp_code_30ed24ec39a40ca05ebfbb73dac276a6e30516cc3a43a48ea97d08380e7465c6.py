code = """import json
import re

# Load funding data
with open(var_functions.query_db:1, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open(var_functions.query_db:4, 'r') as f:
    civic_docs = json.load(f)

print(f'Total funding records: {len(funding_data)}')
print(f'Total civic documents: {len(civic_docs)}')

# Create dictionary for funding lookup
funding_dict = {item['Project_Name']: item for item in funding_data}

# Extract projects from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_status = None
    
    status_patterns = [
        (r'Capital Improvement Projects \(Design\)', 'design'),
        (r'Capital Improvement Projects \(Construction\)', 'construction'),
        (r'Capital Improvement Projects \(Not Started\)', 'not started'),
        (r'Disaster Recovery Projects \(Design\)', 'design'),
        (r'Disaster Recovery Projects \(Construction\)', 'construction'),
        (r'Disaster Recovery Projects \(Not Started\)', 'not started'),
    ]
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for status section headers
        for pattern, status in status_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                current_status = status
                break
        
        # Skip empty lines and common headers
        if not line or len(line) < 5:
            continue
            
        skip_patterns = [
            r'^RECOMMENDED ACTION:',
            r'^DISCUSSION:',
            r'^To:',
            r'^Prepared by:',
            r'^Approved by:',
            r'^Date prepared:',
            r'^Meeting date:',
            r'^Subject:',
            r'^Public Works',
            r'^Agenda Report',
            r'^Page \d+ of \d+',
            r'^Agenda Item #',
            r'^cid:\d+',
            r'^--',
            r'Updates:',
            r'Project Schedule:',
            r'Estimated Schedule:',
            r'Complete Design:',
            r'Advertise:',
            r'Begin Construction:',
            r'Complete Construction:',
            r'Project Description:',
            r'Project Updates:'
        ]
        
        should_skip = any(re.search(pattern, line) for pattern in skip_patterns)
        if should_skip:
            continue
        
        # Check if line looks like a project name
        # Project names typically start with capital letters or years
        if (re.match(r'^[A-Z][a-z]', line) or re.match(r'^\d{4} [A-Z]', line)):
            if len(line.split()) > 1 and not line.isupper():
                project_name = line.strip()
                
                # Check if this project has funding
                if project_name in funding_dict:
                    funding_info = funding_dict[project_name]
                    extracted_projects.append({
                        'Project_Name': project_name,
                        'Funding_Source': funding_info['Funding_Source'],
                        'Amount': int(funding_info['Amount']),
                        'Status': current_status
                    })

# Find FEMA/emergency related projects
emergency_keywords = ['FEMA', 'emergency', 'warning', 'siren', 'fire', 'disaster', 'recovery', 'caloes', 'caljpia']
fema_related_projects = []

# Check extracted projects
for project in extracted_projects:
    project_name = project['Project_Name']
    if any(keyword.lower() in project_name.lower() for keyword in emergency_keywords):
        fema_related_projects.append(project)

# Also check all funding records for FEMA/emergency projects
for funding_item in funding_data:
    project_name = funding_item['Project_Name']
    if any(keyword.lower() in project_name.lower() for keyword in emergency_keywords):
        # Check if we already have status info
        existing = None
        for p in extracted_projects:
            if p['Project_Name'] == project_name:
                existing = p
                break
        
        if not existing:
            fema_related_projects.append({
                'Project_Name': project_name,
                'Funding_Source': funding_item['Funding_Source'],
                'Amount': int(funding_item['Amount']),
                'Status': 'unknown'
            })

# Remove duplicates
seen = set()
unique_projects = []
for project in fema_related_projects:
    if project['Project_Name'] not in seen:
        seen.add(project['Project_Name'])
        unique_projects.append(project)

# Sort by project name
unique_projects.sort(key=lambda x: x['Project_Name'])

print(f'Found {len(unique_projects)} emergency/FEMA related projects')

# Convert to JSON and print
result_json = json.dumps(unique_projects, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
