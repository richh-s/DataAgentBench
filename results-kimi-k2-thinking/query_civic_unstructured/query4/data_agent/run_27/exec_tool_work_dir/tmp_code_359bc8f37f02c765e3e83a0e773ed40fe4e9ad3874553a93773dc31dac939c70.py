code = """import json
import re
from collections import defaultdict

# Load the data
with open(str(globals()['var_functions.query_db:5']), 'r') as f:
    civic_docs = json.load(f)

with open(str(globals()['var_functions.query_db:20']), 'r') as f:
    funding_records = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {}
for rec in funding_records:
    proj_name = rec['Project_Name'].strip()
    amount = int(rec['Amount'])
    funding_map[proj_name] = amount

print('Number of funding records mapped:', len(funding_map))

# Analyze civic documents for Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by projects - look for project headers
    # Common patterns: lines ending with \\n or \\r\\n
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (typically title case or uppercase)
        # Common patterns in these documents
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and
            not line.startswith('▪') and
            not line.lower().startswith('project') and
            not line.lower().startswith('page') and
            not line.lower().startswith('agenda') and
            not line.lower().startswith('to:') and
            not line.lower().startswith('prepared') and
            not line.lower().startswith('approved') and
            not line.lower().startswith('date') and
            not line.lower().startswith('meeting') and
            not line.lower().startswith('subject:') and
            not line.lower().startswith('recommended') and
            not line.lower().startswith('discussion:')):
            
            # This might be a project name
            if current_project:
                # Save previous project if it has Spring 2022
                if project_info.get('has_spring_2022'):
                    project_info['name'] = current_project
                    spring_2022_projects.append(project_info)
            
            current_project = line
            project_info = {'name': line, 'has_spring_2022': False, 'schedule_info': []}
        
        # Look for date/schedule information
        if current_project and '2022' in line:
            project_info['schedule_info'].append(line)
            
            # Check for Spring 2022
            if 'Spring 2022' in line or 'spring 2022' in line:
                project_info['has_spring_2022'] = True
            elif '2022' in line and ('Spring' in line or 'spring' in line or 'Mar' in line or 'Apr' in line or 'May' in line):
                if any(month in line for month in ['Spring', 'Mar', 'Apr', 'May', 'March', 'April', 'May']):
                    project_info['has_spring_2022'] = True
    
    # Don't forget the last project
    if current_project and project_info.get('has_spring_2022'):
        spring_2022_projects.append(project_info)

print('Found Spring 2022 projects:', len(spring_2022_projects))

# Display what we found
for i, proj in enumerate(spring_2022_projects[:10]):
    print('  -', proj['name'])
    for info in proj['schedule_info']:
        print('    ', info)

# Now match with funding
matched_projects = []
total_funding = 0

for proj in spring_2022_projects:
    proj_name = proj['name']
    
    # Exact match
    if proj_name in funding_map:
        matched_projects.append({
            'project_name': proj_name,
            'funding': funding_map[proj_name],
            'schedule_info': proj['schedule_info']
        })
        total_funding += funding_map[proj_name]
    else:
        # Try partial matching - remove common suffixes/prefixes
        base_name = proj_name
        
        # Try without common suffixes
        variations = [
            proj_name,
            proj_name.replace(' Project', ''),
            proj_name.replace(' Project', '').strip(),
            re.sub(r'\(.*?\)', '', proj_name).strip(),
        ]
        
        found = False
        for variant in variations:
            if variant in funding_map:
                matched_projects.append({
                    'project_name': proj_name,
                    'matched_name': variant,
                    'funding': funding_map[variant],
                    'schedule_info': proj['schedule_info']
                })
                total_funding += funding_map[variant]
                found = True
                break
        
        if not found:
            # Try reverse - check if any funding name contains this project name
            for fund_name, amount in funding_map.items():
                if proj_name.lower() in fund_name.lower() or fund_name.lower() in proj_name.lower():
                    matched_projects.append({
                        'project_name': proj_name,
                        'matched_name': fund_name,
                        'funding': amount,
                        'schedule_info': proj['schedule_info']
                    })
                    total_funding += amount
                    found = True
                    break

print('Matched with funding:', len(matched_projects))
print('Total funding:', total_funding)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}}

exec(code, env_args)
