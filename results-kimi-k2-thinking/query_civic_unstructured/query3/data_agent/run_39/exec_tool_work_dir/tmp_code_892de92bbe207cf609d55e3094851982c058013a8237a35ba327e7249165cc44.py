code = """import json
import re

# Load data from storage
civic_docs = globals()['var_functions.query_db:0']
funding_data = globals()['var_functions.query_db:2']

if not isinstance(civic_docs, list):
    civic_docs = json.load(open(civic_docs))
if not isinstance(funding_data, list):
    funding_data = json.load(open(funding_data))

# Function to extract projects from civic document text
def extract_projects_from_text(text):
    projects = []
    
    # Split text into sections - look for project names (lines that don't start with bullet points)
    lines = text.split('\n')
    current_project = None
    
    # Patterns to identify project names vs details
    # Project names are typically title case and don't start with special chars
    project_name_patterns = [
        r'^[A-Z][a-zA-Z0-9 &\-\(\)]+$',  # Title case, mostly letters
        r'^[A-Z][A-Za-z0-9 &\-\(\)]+Project$',  # Ends with Project
        r'^[A-Z][A-Za-z0-9 &\-\(\)]+Improvements$',  # Ends with Improvements
        r'^[A-Z][A-Za-z0-9 &\-\(\)]+Repairs$',  # Ends with Repairs
    ]
    
    # Status indicators
    status_keywords = ['design', 'construction', 'completed', 'not started', 'advertise', 'begin']
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this looks like a project name
        is_project_name = False
        
        # Skip lines that are obviously not project names
        if (line.startswith('(') or line.startswith('cid:') or 
            line.startswith('Page') or line.startswith('Agenda') or
            line.lower().startswith('item') or line.startswith('To:') or
            line.startswith('Prepared') or line.startswith('Approved') or
            line.startswith('Date') or line.startswith('Meeting') or
            line.startswith('Subject') or line.startswith('RECOMMENDED') or
            line.startswith('DISCUSSION') or ':' in line[:30] or
            line.isupper() and len(line.split()) > 10):  # Long all-caps lines
            continue
            
        # Check project name patterns
        if (re.match(r'^[A-Z][a-zA-Z0-9 &\-\(\)]+$', line) and 
            len(line) > 5 and not line.isupper()):
            is_project_name = True
        elif 'Project' in line and line.istitle():
            is_project_name = True
        elif re.match(r'^[A-Z].* (Project|Improvements|Repairs|Study|System)$', line):
            is_project_name = True
            
        if is_project_name and len(line) < 100:  # Reasonable length
            # Save previous project if exists
            if current_project:
                projects.append(current_project)
                
            # Start new project
            current_project = {
                'Project_Name': line.strip(),
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': '',
                'text': ''
            }
            
            # Try to determine type from name
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'Disaster' in line:
                current_project['type'] = 'disaster'
            elif 'Capital' in line or 'Improvement' in line:
                current_project['type'] = 'capital'
                
            # Try to determine topic from name
            topics = []
            if 'emergency' in line.lower() or 'warning' in line.lower() or 'siren' in line.lower():
                topics.append('emergency warning')
            if 'FEMA' in line:
                topics.append('FEMA')
            if 'drain' in line.lower() or 'storm' in line.lower():
                topics.append('drainage')
            if 'road' in line.lower():
                topics.append('road')
            if 'park' in line.lower():
                topics.append('park')
            if 'bridge' in line.lower():
                topics.append('bridge')
                
            current_project['topic'] = ', '.join(topics)
            
        elif current_project:
            # This is detail for the current project
            current_project['text'] += line + '\n'
            
            # Look for status information
            line_lower = line.lower()
            if ('updates:' in line_lower or 'schedule:' in line_lower or 
                'estimated schedule:' in line_lower):
                # Look in following lines for status
                if 'design' in line_lower:
                    current_project['status'] = 'design'
                elif 'construction' in line_lower or 'under construction' in line_lower:
                    current_project['status'] = 'construction'
                elif 'completed' in line_lower:
                    current_project['status'] = 'completed'
                elif 'not started' in line_lower:
                    current_project['status'] = 'not started'
                    
            # Look for dates
            date_patterns = [
                r'(Spring|Summer|Fall|Winter)\s+(\d{4})',
                r'(\d{4})-(Spring|Summer|Fall|Winter)',
                r'(\d{4})-(\d{1,2})',
                r'(\d{4})-([A-Za-z]+)',
            ]
            
            for pattern in date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            date_str = '-'.join(match)
                        else:
                            date_str = match
                        if not current_project['st']:
                            current_project['st'] = date_str
                        else:
                            current_project['et'] = date_str
                            
    # Don't forget the last project
    if current_project:
        projects.append(current_project)
        
    return projects

# Extract projects from all civic documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    for proj in projects:
        proj['source_file'] = doc['filename']
        all_projects.append(proj)

print(f"Extracted {len(all_projects)} projects from civic documents")

# Filter for emergency/FEMA related projects
emergency_projects = []
for proj in all_projects:
    # Check name and topic
    name_lower = proj['Project_Name'].lower()
    topic_lower = proj['topic'].lower()
    
    if ('emergency' in name_lower or 'fema' in name_lower or 
        'emergency' in topic_lower or 'fema' in topic_lower):
        emergency_projects.append(proj)

print(f"Found {len(emergency_projects)} emergency/FEMA related projects")

# Show some examples
for proj in emergency_projects[:10]:
    print(f"\nProject: {proj['Project_Name']}")
    print(f"  Type: {proj['type']}")
    print(f"  Topic: {proj['topic']}")
    print(f"  Status: {proj['status']}")
    print(f"  File: {proj['source_file']}")

# Save the projects for next step
result = {
    'all_projects_count': len(all_projects),
    'emergency_projects_count': len(emergency_projects),
    'emergency_projects': emergency_projects[:20]  # First 20 to avoid too much output
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
