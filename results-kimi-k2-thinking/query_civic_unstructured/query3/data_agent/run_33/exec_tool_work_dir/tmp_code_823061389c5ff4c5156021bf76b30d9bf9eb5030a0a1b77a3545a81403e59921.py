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
    lines = text.split('\n')
    current_project = None
    project_status = None
    
    status_patterns = [
        (r'Capital Improvement Projects \(Design\)', 'design'),
        (r'Disaster Recovery Projects \(Design\)', 'design'),
        (r'Capital Improvement Projects \(Construction\)', 'construction'),
        (r'Disaster Recovery Projects \(Construction\)', 'construction'),
        (r'Capital Improvement Projects \(Not Started\)', 'not started'),
        (r'Disaster Recovery Projects \(Not Started\)', 'not started'),
        (r'Capital Improvement Projects \(Completed\)', 'completed'),
        (r'Disaster Recovery Projects \(Completed\)', 'completed')
    ]
    
    header_patterns = [
        'Public Works', 'Commission', 'Agenda', 'Item', 'To:', 'Prepared', 'Approved', 'Date', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'City Council', 'Page'
    ]
    
    for line in lines:
        line = line.strip()
        
        # Check for status headers
        for pattern, status in status_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                project_status = status
                break
                
        # Look for project names
        if line and len(line) > 10 and not line.startswith(tuple(['(', '•', '-', '■', 'cid'])):
            is_header = any(h in line for h in header_patterns)
            if not is_header and not re.match(r'^[A-Z\s]+$', line):
                has_updates = False
                if current_project:
                    for next_line in lines[lines.index(line):lines.index(line)+3]:
                        if 'Updates:' in next_line or 'Complete' in next_line or 'Schedule:' in next_line:
                            has_updates = True
                            break
                
                if has_updates or 'Project' in line or any(word in line.lower() for word in ['road', 'street', 'park', 'drain', 'bridge', 'culvert', 'wall']):
                    if current_project:
                        projects.append({
                            'Project_Name': current_project.strip(),
                            'Status': project_status or 'not specified'
                        })
                    current_project = line
                    
    # Add last project
    if current_project and project_status:
        projects.append({
            'Project_Name': current_project.strip(),
            'Status': project_status
        })
        
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Filter projects related to emergency/FEMA
filtered_projects = []
project_names_seen = set()

for project in all_projects:
    name_lower = project['Project_Name'].lower()
    if 'emergency' in name_lower or 'fema' in name_lower:
        filtered_projects.append(project)
        project_names_seen.add(project['Project_Name'])

# Process funding data to get amounts and sources
funding_dict = {f['Project_Name'].lower(): f for f in funding_data}

# For each filtered project, add funding info
final_results = []
for project in filtered_projects:
    project_name = project['Project_Name']
    project_lower = project_name.lower()
    
    # Find matching funding
    funding_match = None
    for f in funding_data:
        if project_name in f['Project_Name'] or f['Project_Name'] in project_name:
            funding_match = f
            break
    
    if not funding_match:
        for f in funding_data:
            f_lower = f['Project_Name'].lower()
            if project_lower in f_lower or f_lower in project_lower:
                funding_match = f
                break
    
    if funding_match:
        final_results.append({
            'Project_Name': project_name,
            'Funding_Source': funding_match['Funding_Source'],
            'Amount': int(funding_match['Amount']),
            'Status': project['Status']
        })
    else:
        final_results.append({
            'Project_Name': project_name,
            'Funding_Source': 'Not found',
            'Amount': 0,
            'Status': project['Status']
        })

# Also include projects from funding data that have FEMA but weren't in civic docs
for f in funding_data:
    if 'fema' in f['Project_Name'].lower() and f['Project_Name'] not in [r['Project_Name'] for r in final_results]:
        final_results.append({
            'Project_Name': f['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Not specified in civic docs'
        })

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

result = {
    'total_projects': len(final_results),
    'projects': final_results
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
