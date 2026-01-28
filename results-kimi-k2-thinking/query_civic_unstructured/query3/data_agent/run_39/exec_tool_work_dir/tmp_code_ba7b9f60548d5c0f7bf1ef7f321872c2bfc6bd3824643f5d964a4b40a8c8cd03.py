code = """import json, re, os

# Read the stored data
civic_docs = json.load(open(globals()['var_functions.query_db:0']))
funding_data = json.load(open(globals()['var_functions.query_db:2']))

# Extract projects
all_projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    curr_proj = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('Page') or line.startswith('Agenda') or 'cid:' in line:
            continue
            
        # Detect project name: reasonable length, title case or contains keywords, not all caps
        if (len(line) < 100 and (line.istitle() or 'Project' in line or 'Improvements' in line or 'Repairs' in line)
            and not line.isupper()):
            
            # Save previous project
            if curr_proj:
                all_projects.append(curr_proj)
            
            # Create new project record
            curr_proj = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': '',
                'source_file': doc['filename']
            }
            
            # Determine type based on keywords in project name
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                curr_proj['type'] = 'disaster'
            elif 'Capital' in line or 'Improvements' in line:
                curr_proj['type'] = 'capital'
            else:
                curr_proj['type'] = 'capital'  # default
            
            # Extract topics from project name
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
            curr_proj['topic'] = ', '.join(topics)
        
        elif curr_proj:
            # Process project details
            line_lower = line.lower()
            
            # Extract status if not already set
            if 'design' in line_lower and not curr_proj['status']:
                curr_proj['status'] = 'design'
            elif 'construction' in line_lower or 'under construction' in line_lower:
                curr_proj['status'] = 'construction'
            elif 'completed' in line_lower and not curr_proj['status']:
                curr_proj['status'] = 'completed'
            elif 'not started' in line_lower:
                curr_proj['status'] = 'not started'
            
            # Extract dates
            date_match = re.search(r'(Spring|Summer|Fall|Winter)[\s-](\d{4})', line, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(2) + '-' + date_match.group(1).title()
                if not curr_proj['st']:
                    curr_proj['st'] = date_str
                elif not curr_proj['et']:
                    curr_proj['et'] = date_str
    
    # Add the last project
    if curr_proj:
        all_projects.append(curr_proj)

# Filter for emergency/FEMA related projects
emergency_projects = []
for project in all_projects:
    name_lower = project['Project_Name'].lower()
    topic_lower = project['topic'].lower()
    
    if 'emergency' in name_lower or 'fema' in name_lower or 'emergency' in topic_lower or 'fema' in topic_lower:
        emergency_projects.append(project)

# Match projects with funding data
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = f

matched_projects = []
for proj in emergency_projects:
    proj_name = proj['Project_Name']
    
    # Check for exact match first
    if proj_name in funding_lookup:
        funding = funding_lookup[proj_name]
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': proj['status'] if proj['status'] else 'Unknown',
            'Topic': proj['topic'] if proj['topic'] else 'None'
        })

# Build the final output string
output_text = 'Emergency/FEMA Related Projects - %d projects found\n\n' % len(matched_projects)
for mp in matched_projects:
    output_text += 'Project: %s\n' % mp['Project_Name']
    output_text += '  Funding Source: %s\n' % mp['Funding_Source']
    output_text += '  Amount: $%s\n' % mp['Amount']
    output_text += '  Status: %s\n' % mp['Status']
    output_text += '  Topic: %s\n\n' % mp['Topic']

print('__RESULT__:')
print(json.dumps(output_text))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
