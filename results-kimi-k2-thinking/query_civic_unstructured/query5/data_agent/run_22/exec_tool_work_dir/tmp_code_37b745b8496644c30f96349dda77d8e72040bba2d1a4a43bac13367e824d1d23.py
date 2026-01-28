code = """import json
import re

# Get the data from storage
funding_data = locals()['var_functions.query_db:6']
civic_docs_data = locals()['var_functions.query_db:7']

# Load data from files if they're stored as file paths
import os
if isinstance(funding_data, str) and os.path.exists(funding_data):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)
if isinstance(civic_docs_data, str) and os.path.exists(civic_docs_data):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic docs: {len(civic_docs_data)}")

# Extract projects from civic documents
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by project sections - look for common patterns
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - they often appear as standalone titles or after bullets
        # Pattern: project name followed by updates or schedule
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('Page') and 
            not line.startswith('Agenda Item') and
            not any(keyword in line.lower() for keyword in ['capital improvement', 'disaster recovery', 'project schedule', 'updates:', 'completed:', 'not started:']) and
            (i < len(lines) - 1 and ('Updates:' in lines[i+1] or 'Schedule:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or lines[i+1].strip().startswith('(cid:')))):
            
            # Save previous project
            if current_project and project_info:
                projects.append({
                    'project_name': current_project,
                    'info': project_info,
                    'source_file': filename
                })
            
            # Start new project
            current_project = line.strip()
            project_info = {'type': 'unknown', 'has_2022_date': False, 'start_date_mention': None}
            
            # Check if disaster-related based on name
            if any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                project_info['type'] = 'disaster'
            elif any(keyword in line.lower() for keyword in ['storm drain', 'drainage', 'slope repair', 'bridge', 'culvert', 'retaining wall']):
                # Could be either, check for FEMA/CalOES in text after
                pass
        
        # Look for dates in current project context
        if current_project:
            # Find any 2022 dates
            date_patterns = [
                r'(?:Complete Design|Begin Construction|Advertise|Complete Construction|Begin|Complete|Design|Construction)[\s:]*([^\n]*2022[^\n]*)',
                r'(2022[\s-]\w+)',
                r'(\w+[\s-]2022)'
            ]
            
            for pattern in date_patterns:
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    if '2022' in match.group(0):
                        project_info['has_2022_date'] = True
                        project_info['start_date_mention'] = match.group(0)
                        break
            
            # Check for disaster indicators in project description
            if any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                project_info['type'] = 'disaster'
    
    # Save last project
    if current_project and project_info:
        projects.append({
            'project_name': current_project,
            'info': project_info,
            'source_file': filename
        })

print(f"Extracted {len(projects)} potential projects")

# Look for disaster projects with 2022 dates
disaster_projects_2022 = []
for p in projects:
    if p['info']['type'] == 'disaster' and p['info']['has_2022_date']:
        disaster_projects_2022.append(p['project_name'])

print(f"Found {len(disaster_projects_2022)} disaster projects with 2022 dates")
for proj in disaster_projects_2022[:10]:
    print(f"  - {proj}")

print("__RESULT__:")
print(json.dumps({
    "total_projects": len(projects),
    "disaster_2022_count": len(disaster_projects_2022),
    "disaster_projects_2022": disaster_projects_2022[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
