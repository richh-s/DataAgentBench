code = """import json
import re

# Load funding data
with open('funding_query_result.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('civic_docs_query_result.json', 'r') as f:
    civic_docs = json.load(f)

print('Total funding records:', len(funding_data))
print('Total civic documents:', len(civic_docs))

# Create dictionary for funding lookup
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = item

# Extract projects from civic documents
extracted_projects = []

def check_and_add_project(project_name, status):
    if project_name in funding_dict:
        funding_info = funding_dict[project_name]
        extracted_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': int(funding_info['Amount']),
            'Status': status
        })

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_status = None
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Check for status section headers
        if 'Capital Improvement Projects (Design)' in line or 'Disaster Recovery Projects (Design)' in line:
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line or 'Disaster Recovery Projects (Construction)' in line:
            current_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line or 'Disaster Recovery Projects (Not Started)' in line:
            current_status = 'not started'
        
        # Skip common headers and metadata
        if any(x in line for x in ['RECOMMENDED ACTION:', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'Public Works', 'Agenda Report', 'Page', 'Agenda Item', 'cid:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:']):
            continue
        
        # Check if line looks like a project name
        if (re.match(r'^[A-Z][a-z]', line) or re.match(r'^\d{4} [A-Z]', line)) and not line.isupper():
            if len(line.split()) > 1:
                check_and_add_project(line, current_status)

# Find FEMA/emergency related projects
emergency_keywords = ['FEMA', 'emergency', 'warning', 'siren', 'fire', 'disaster', 'recovery', 'caloes', 'caljpia']
fema_related_projects = []

# Check extracted projects for keywords in name
for project in extracted_projects:
    project_name = project['Project_Name']
    if any(keyword.lower() in project_name.lower() for keyword in emergency_keywords):
        fema_related_projects.append(project)

# Also check all funding records for FEMA/emergency projects
for funding_item in funding_data:
    project_name = funding_item['Project_Name']
    if any(keyword.lower() in project_name.lower() for keyword in emergency_keywords):
        found = False
        for p in extracted_projects:
            if p['Project_Name'] == project_name:
                if p not in fema_related_projects:
                    fema_related_projects.append(p)
                found = True
                break
        
        if not found:
            fema_related_projects.append({
                'Project_Name': project_name,
                'Funding_Source': funding_item['Funding_Source'],
                'Amount': int(funding_item['Amount']),
                'Status': 'unknown'
            })

# Remove duplicates
seen_projects = set()
unique_projects = []
for proj in fema_related_projects:
    name = proj['Project_Name']
    if name not in seen_projects:
        seen_projects.add(name)
        unique_projects.append(proj)

# Sort by project name
unique_projects.sort(key=lambda x: x['Project_Name'])

print('Found', len(unique_projects), 'emergency/FEMA related projects')

result_json = json.dumps(unique_projects, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
