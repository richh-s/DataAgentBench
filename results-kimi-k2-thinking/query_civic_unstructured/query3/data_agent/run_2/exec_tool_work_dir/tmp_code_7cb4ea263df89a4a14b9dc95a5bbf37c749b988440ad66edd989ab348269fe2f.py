code = """import json
import re
from collections import defaultdict

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections that might contain projects
    # Look for patterns that indicate projects
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically all caps or title case on their own line)
        # Common patterns: project names followed by "Project" or on their own line
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('-'):
            # Check if this looks like a project name
            # Usually followed by "Project" or has capitalized words
            
            # Check for "(FEMA Project)" or similar suffixes
            if '(FEMA' in line or 'FEMA' in line or 'emergency' in line.lower():
                project_name = line
                
                # Look for status indicators
                status = None
                if 'in design' in text.lower() or 'design phase' in text.lower():
                    status = 'design'
                elif 'construction' in text.lower() and 'completed' not in text.lower():
                    status = 'construction'
                elif 'completed' in text.lower() or 'completion' in text.lower():
                    status = 'completed'
                elif 'not started' in text.lower():
                    status = 'not started'
                
                # Look for schedule/project type
                project_type = None
                if 'Capital Improvement' in text:
                    project_type = 'capital'
                if 'Disaster Recovery' in text or 'FEMA' in line or 'emergency' in line.lower():
                    project_type = 'disaster'
                
                # Topics
                topics = []
                if 'FEMA' in line:
                    topics.append('FEMA')
                if 'emergency' in text.lower():
                    topics.append('emergency')
                if 'drainage' in text.lower() or 'storm' in text.lower():
                    topics.append('drainage')
                if 'road' in text.lower():
                    topics.append('road')
                if 'park' in text.lower():
                    topics.append('park')
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type,
                    'topic': ','.join(topics) if topics else '',
                    'filename': filename
                })
    
    # Also look for bullet points or sections that start with project names
    # Pattern: project name followed by updates/schedule
    project_patterns = [
        r'([A-Z][A-Za-z\s]+?(?:Project|Improvements|Repairs|Drainage|Road|Park|Structure))',
        r'([A-Z][A-Za-z\s\d-]+?\(FEMA[^)]*\))',
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            if len(project_name) > 10 and len(project_name) < 150:
                # Check if it's FEMA/emergency related
                is_relevant = 'FEMA' in project_name or 'emergency' in project_name.lower()
                
                # Check nearby text for context
                start_pos = match.start()
                context = text[max(0, start_pos-200):min(len(text), start_pos+200)]
                
                if is_relevant or 'FEMA' in context or 'emergency' in context.lower():
                    # Determine status from context
                    status = None
                    if 'design' in context.lower() and 'construction' not in context.lower():
                        status = 'design'
                    elif 'construction' in context.lower():
                        if 'completed' in context.lower():
                            status = 'completed'
                        else:
                            status = 'construction'
                    elif 'completed' in context.lower():
                        status = 'completed'
                    elif 'not started' in context.lower():
                        status = 'not started'
                    
                    project_type = 'disaster' if ('FEMA' in project_name or 'emergency' in project_name.lower()) else None
                    
                    topics = []
                    if 'FEMA' in project_name:
                        topics.append('FEMA')
                    if 'emergency' in project_name.lower():
                        topics.append('emergency')
                    
                    projects.append({
                        'Project_Name': project_name,
                        'status': status,
                        'type': project_type,
                        'topic': ','.join(topics),
                        'filename': filename
                    })

# Filter for distinct projects
unique_projects = {}
for p in projects:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

projects_list = list(unique_projects.values())

# Now match with funding data
funding_by_project = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    funding_by_project[proj_name] = {
        'Funding_Source': fund.get('Funding_Source', ''),
        'Amount': fund.get('Amount', 0),
        'Funding_ID': fund.get('Funding_ID', '')
    }

# Merge project info with funding
result = []
for project in projects_list:
    proj_name = project['Project_Name']
    funding = funding_by_project.get(proj_name, {})
    
    if funding:  # Only include projects with funding data
        result.append({
            'Project_Name': proj_name,
            'Funding_Source': funding.get('Funding_Source', ''),
            'Amount': funding.get('Amount', 0),
            'Status': project.get('status', 'Unknown'),
            'Type': project.get('type', ''),
            'Topics': project.get('topic', '')
        })

# Also check funding data for FEMA/emergency projects that might not be in civic docs
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        # Check if we already have this project
        existing = next((p for p in result if p['Project_Name'] == proj_name), None)
        if not existing:
            result.append({
                'Project_Name': proj_name,
                'Funding_Source': fund.get('Funding_Source', ''),
                'Amount': fund.get('Amount', 0),
                'Status': 'Unknown',
                'Type': 'disaster' if 'FEMA' in proj_name else '',
                'Topics': 'FEMA' if 'FEMA' in proj_name else 'emergency'
            })

# Sort by project name
result = sorted(result, key=lambda x: x['Project_Name'])

# Print result
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
