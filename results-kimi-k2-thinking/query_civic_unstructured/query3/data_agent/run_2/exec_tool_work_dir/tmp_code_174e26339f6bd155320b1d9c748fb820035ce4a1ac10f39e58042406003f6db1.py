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
    
    # Look for project patterns with FEMA or emergency
    project_patterns = [
        r'([A-Z][A-Za-z\s]+?(?:Project|Improvements|Repairs|Drainage|Road|Park|Structure|Wall))',
        r'([A-Z][A-Za-z\s\d-]+?\(FEMA[^)]*\))',
        r'([A-Z][A-Za-z\s\d-]+?\(CalOES[^)]*\))',
        r'([A-Z][A-Za-z\s\d-]+?\(CalJPIA[^)]*\))'
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            if len(project_name) > 10 and len(project_name) < 200:
                # Check if it's FEMA/emergency related
                is_relevant = 'FEMA' in project_name or 'emergency' in project_name.lower()
                
                # Check nearby text for context
                start_pos = match.start()
                context = text[max(0, start_pos-300):min(len(text), start_pos+300)]
                
                if is_relevant or 'FEMA' in context or 'emergency' in context.lower():
                    # Determine status from context
                    status = 'Unknown'
                    if 'design phase' in context.lower() or 'complete design' in context.lower():
                        status = 'design'
                    elif 'construction' in context.lower():
                        if 'completed' in context.lower() or 'completion' in context.lower():
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
                    if 'storm' in project_name.lower() or 'drainage' in context.lower():
                        topics.append('drainage')
                    
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
    if name not in unique_projects or p['status'] != 'Unknown':
        unique_projects[name] = p

projects_list = list(unique_projects.values())

# Create lookup for funding data
funding_by_project = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    funding_by_project[proj_name] = {
        'Funding_Source': fund.get('Funding_Source', ''),
        'Amount': fund.get('Amount', 0),
        'Funding_ID': fund.get('Funding_ID', '')
    }

# Also include projects that might be related but not captured
fema_emergency_projects = []
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_emergency_projects.append(proj_name)

# Merge project info with funding
result = []

# Add all FEMA/emergency projects from funding data
for proj_name in fema_emergency_projects:
    funding = funding_by_project.get(proj_name, {})
    
    # Try to find matching project info
    project_info = unique_projects.get(proj_name, {})
    
    if not project_info:
        # Try partial matching
        for p_name, p_info in unique_projects.items():
            if proj_name in p_name or p_name in proj_name:
                project_info = p_info
                break
    
    result.append({
        'Project_Name': proj_name,
        'Funding_Source': funding.get('Funding_Source', ''),
        'Amount': funding.get('Amount', 0),
        'Status': project_info.get('status', 'Unknown'),
        'Type': project_info.get('type', 'disaster' if 'FEMA' in proj_name else ''),
        'Topics': project_info.get('topic', 'FEMA' if 'FEMA' in proj_name else 'emergency')
    })

# Add projects from civic docs that have funding
for project in projects_list:
    proj_name = project['Project_Name']
    if proj_name in funding_by_project:
        funding = funding_by_project[proj_name]
        
        # Don't duplicate
        existing = next((r for r in result if r['Project_Name'] == proj_name), None)
        if not existing:
            result.append({
                'Project_Name': proj_name,
                'Funding_Source': funding.get('Funding_Source', ''),
                'Amount': funding.get('Amount', 0),
                'Status': project.get('status', 'Unknown'),
                'Type': project.get('type', ''),
                'Topics': project.get('topic', '')
            })

# Remove duplicates
unique_result = []
seen_names = set()
for item in result:
    name = item['Project_Name']
    if name not in seen_names:
        unique_result.append(item)
        seen_names.add(name)

# Sort by project name
unique_result = sorted(unique_result, key=lambda x: x['Project_Name'])

# Format output as JSON string
output = json.dumps(unique_result, indent=2)

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
