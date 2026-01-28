code = """import json
import re

# Load the data
civic_docs = json.load(open(globals()['var_functions.query_db:0']))
funding_data = json.load(open(globals()['var_functions.query_db:2']))

# Extract projects from the civic documents
all_projects = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('Page') or line.startswith('Agenda') or 'cid:' in line:
            continue
            
        # Check if this line looks like a project name
        if len(line) < 100 and not line.isupper() and (line.istitle() or 'Project' in line or 'Improvements' in line or 'Repairs' in line):
            # Save previous project
            if current_project:
                all_projects.append(current_project)
            
            # Create new project
            current_project = {
                'Project_Name': line,
                'topic': '',
                'type': 'capital' if not ('FEMA' in line or 'CalOES' in line or 'CalJPIA' in line) else 'disaster',
                'status': '',
                'st': '',
                'et': '',
                'source_file': doc['filename']
            }
            
            # Extract topics
            topics = []
            if 'emergency' in line.lower():
                topics.append('emergency warning')
            if 'FEMA' in line:
                topics.append('FEMA')
            if 'siren' in line.lower() or 'warning' in line.lower():
                topics.append('emergency warning')
            if 'drain' in line.lower() or 'storm' in line.lower():
                topics.append('drainage')
            if 'road' in line.lower():
                topics.append('road')
            if 'park' in line.lower():
                topics.append('park')
            current_project['topic'] = ', '.join(topics)
        
        elif current_project:
            # Process project details
            line_lower = line.lower()
            
            # Extract status
            if 'design' in line_lower and not current_project['status']:
                current_project['status'] = 'design'
            elif 'construction' in line_lower:
                current_project['status'] = 'construction'
            elif 'completed' in line_lower and not current_project['status']:
                current_project['status'] = 'completed'
            elif 'not started' in line_lower:
                current_project['status'] = 'not started'
            
            # Extract dates
            date_match = re.search(r'(Spring|Summer|Fall|Winter)[\s-](\d{4})', line, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(2) + '-' + date_match.group(1).title()
                if not current_project['st']:
                    current_project['st'] = date_str
                elif not current_project['et']:
                    current_project['et'] = date_str
    
    # Add the last project
    if current_project:
        all_projects.append(current_project)

# Filter for emergency/FEMA projects
emergency_fema_projects = []
for p in all_projects:
    name_lower = p['Project_Name'].lower()
    topic_lower = p['topic'].lower()
    if 'emergency' in name_lower or 'fema' in name_lower or 'emergency' in topic_lower or 'fema' in topic_lower:
        emergency_fema_projects.append(p)

# Match with funding data
funding_lookup = {f['Project_Name']: f for f in funding_data}
final_results = []

for project in emergency_fema_projects:
    proj_name = project['Project_Name']
    
    # Check for exact match in funding data
    if proj_name in funding_lookup:
        funding = funding_lookup[proj_name]
        final_results.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': int(funding['Amount']),
            'Status': project['status'] or 'Unknown',
            'Topic': project['topic'] or 'None'
        })
    else:
        # Check for partial matches (project name appears in funding project name or vice versa)
        for f_name, funding in funding_lookup.items():
            if (proj_name in f_name or f_name in proj_name or 
                ''.join(proj_name.split()).lower() == ''.join(f_name.split()).lower()):
                final_results.append({
                    'Project_Name': proj_name,
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': int(funding['Amount']),
                    'Status': project['status'] or 'Unknown',
                    'Topic': project['topic'] or 'None'
                })
                break

# Build the final answer
answer = []
for r in final_results:
    answer.append({
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': r['Amount'],
        'Status': r['Status'],
        'Topic': r['Topic']
    })

# Return the result as JSON
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
