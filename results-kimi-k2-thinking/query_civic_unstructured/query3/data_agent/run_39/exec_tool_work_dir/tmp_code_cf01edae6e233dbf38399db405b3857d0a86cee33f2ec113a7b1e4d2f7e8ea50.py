code = """import json
import re

# Load the civic documents and funding data
civic_docs_file = globals()['var_functions.query_db:0']
funding_file = globals()['var_functions.query_db:2']

civic_docs = json.load(open(civic_docs_file)) if isinstance(civic_docs_file, str) else civic_docs_file
funding_data = json.load(open(funding_file)) if isinstance(funding_file, str) else funding_file

print('Documents loaded:', len(civic_docs), 'civic docs,', len(funding_data), 'funding records')

# Extract projects from civic documents
def extract_projects(text, filename):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip header/footer lines
        skip_patterns = ['Page', 'Agenda', 'Item', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION']
        if any(line.startswith(p) for p in skip_patterns) or 'cid:' in line:
            continue
            
        # Check if this is a project name (title case, reasonable length, no colon at start)
        if (len(line) < 100 and not line.isupper() and 
            line[0].isalpha() and ':' not in line[:30] and
            (line.istitle() or 'Project' in line or 'Improvements' in line or 'Repairs' in line)):
            
            # Save previous project
            if current_project:
                projects.append(current_project)
            
            # Start new project
            current_project = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': '',
                'source_file': filename
            }
            
            # Set type based on keywords
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                current_project['type'] = 'disaster'
            elif any(kw in line for kw in ['Improvements', 'Capital', 'Project']):
                current_project['type'] = 'capital'
            else:
                current_project['type'] = 'capital'  # default
            
            # Set topics
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'drain' in line.lower() or 'storm' in line.lower(): topics.append('drainage')
            if 'road' in line.lower(): topics.append('road')
            if 'park' in line.lower(): topics.append('park')
            if 'siren' in line.lower() or 'warning' in line.lower(): topics.append('emergency warning')
            current_project['topic'] = ', '.join(topics)
        
        elif current_project:
            # Add to current project details
            line_lower = line.lower()
            
            # Extract status
            if 'design' in line_lower and not current_project['status']:
                current_project['status'] = 'design'
            elif 'construction' in line_lower or 'under construction' in line_lower:
                current_project['status'] = 'construction'
            elif 'completed' in line_lower and not current_project['status']:
                current_project['status'] = 'completed'
            elif 'not started' in line_lower:
                current_project['status'] = 'not started'
                
            # Extract dates (look for patterns like "Spring 2023", "2023-Fall", etc.)
            date_matches = re.findall(r'(Spring|Summer|Fall|Winter)\s+([0-9]{4})', line, re.IGNORECASE)
            if date_matches:
                for match in date_matches:
                    date_str = f"{match[1]}-{match[0]}"
                    if not current_project['st']:
                        current_project['st'] = date_str
                    elif not current_project['et']:
                        current_project['et'] = date_str
    
    # Add final project
    if current_project:
        projects.append(current_project)
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'], doc['filename'])
    all_projects.extend(projects)

print('Total projects extracted:', len(all_projects))

# Filter for emergency/FEMA projects
emergency_projects = []
for p in all_projects:
    name = p['Project_Name'].lower()
    topic = p['topic'].lower()
    if 'emergency' in name or 'fema' in name or 'emergency' in topic or 'fema' in topic:
        emergency_projects.append(p)

print('Emergency/FEMA projects:', len(emergency_projects))

# Show sample projects
for p in emergency_projects[:10]:
    print('-', p['Project_Name'], '| Type:', p['type'], '| Topic:', p['topic'], '| Status:', p['status'])

# Join with funding data
funding_lookup = {f['Project_Name']: f for f in funding_data}

final_results = []
for p in emergency_projects:
    proj_name = p['Project_Name']
    # Try exact match first
    if proj_name in funding_lookup:
        funding = funding_lookup[proj_name]
        final_results.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': int(funding['Amount']),
            'Status': p['status'],
            'Type': p['type'],
            'Topic': p['topic']
        })
    else:
        # Try to find funding records that contain this project name or vice versa
        for f_name, funding in funding_lookup.items():
            if (proj_name in f_name or f_name in proj_name or 
                ''.join(proj_name.split()) == ''.join(f_name.split())):
                final_results.append({
                    'Project_Name': proj_name,
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': int(funding['Amount']),
                    'Status': p['status'],
                    'Type': p['type'],
                    'Topic': p['topic']
                })
                break

print('\nProjects with funding matches:', len(final_results))

# Output the final results in JSON format
output = {
    'total_emergency_projects': len(emergency_projects),
    'projects_with_funding': len(final_results),
    'projects': final_results
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
