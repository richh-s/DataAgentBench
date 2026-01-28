code = """import json, os, re

# Load civic documents data
filepath = locals().get('var_functions.query_db:2')
if isinstance(filepath, str) and os.path.exists(filepath):
    with open(filepath, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

print(f'Loaded {len(civic_docs)} documents')

# Function to extract projects from document text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Split text into sections - look for project patterns
    # Look for lines that look like project names (often bold or title case)
    lines = text.split('\n')
    
    # Patterns to identify project names
    # Common patterns: Title Case lines, lines ending with "Project", 
    # or lines that are project descriptions
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Check if this might be a project name
        is_project_name = False
        
        # Pattern 1: Line is mostly uppercase words (title case)
        if len(line) > 5 and line[0].isupper() and not line.isupper():
            # Check if next lines contain project details
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if 'Updates:' in next_line or 'Project Schedule:' in next_line or 'Project Description:' in next_line:
                    is_project_name = True
        
        # Pattern 2: Line contains "Project" and is relatively short
        if 'Project' in line and len(line) < 150 and not line.startswith('('):
            is_project_name = True
            
        # Pattern 3: Specific known project patterns from the data
        project_indicators = [
            'Resurfacing', 'Storm Drain', 'Road', 'Bridge', 'Park', 'Highway',
            'Improvements', 'Repairs', 'Drainage', 'Wall', 'Facility', 'Study',
            'System', 'Structure', 'Crosswalk', 'Median', 'Signals', 'Warning'
        ]
        
        if any(indicator.lower() in line.lower() for indicator in project_indicators) and 10 < len(line) < 150:
            # Check if it's not just a continuation of previous text
            if not line.startswith('(') and not line.startswith('•') and not line.startswith('-'):
                is_project_name = True
        
        if is_project_name and not line.startswith('RECOMMENDED') and not line.startswith('DISCUSSION'):
            project_name = line
            
            # Try to extract status, dates, and topics from following lines
            status = None
            st = None
            et = None
            topic = []
            
            j = i + 1
            while j < len(lines) and j < i + 20:  # Look ahead up to 20 lines
                next_line = lines[j].strip()
                if not next_line:
                    j += 1
                    continue
                    
                # Look for status indicators
                if 'Updates:' in next_line:
                    # Check following lines for status
                    k = j + 1
                    while k < len(lines) and k < j + 10:
                        status_line = lines[k].strip()
                        if 'design' in status_line.lower():
                            status = 'design'
                            break
                        elif 'construction' in status_line.lower() or 'under construction' in status_line.lower():
                            status = 'construction'
                            break
                        elif 'completed' in status_line.lower():
                            status = 'completed'
                            break
                        elif 'not started' in status_line.lower():
                            status = 'not started'
                            break
                        k += 1
                
                # Look for schedule info
                if 'Project Schedule:' in next_line or 'Schedule:' in next_line:
                    k = j + 1
                    while k < len(lines) and k < j + 10:
                        schedule_line = lines[k].strip()
                        if 'Complete Design:' in schedule_line:
                            date_match = re.search(r'Complete Design:\s*(\S+)', schedule_line)
                            if date_match:
                                st = date_match.group(1)
                        elif 'Begin Construction:' in schedule_line:
                            date_match = re.search(r'Begin Construction:\s*(\S+)', schedule_line)
                            if date_match:
                                st = date_match.group(1)
                        elif 'Complete Construction:' in schedule_line:
                            date_match = re.search(r'Complete Construction:\s*(\S+)', schedule_line)
                            if date_match:
                                et = date_match.group(1)
                        k += 1
                
                # Look for topics based on project name
                name_lower = project_name.lower()
                if any(word in name_lower for word in ['fema', 'disaster', 'recovery', 'fire', 'woolsey']):
                    topic.extend(['disaster', 'fema', 'recovery'])
                if any(word in name_lower for word in ['storm', 'drain', 'drainage']):
                    topic.extend(['storm', 'drainage'])
                if any(word in name_lower for word in ['park', 'playground']):
                    topic.extend(['park'])
                if any(word in name_lower for word in ['road', 'highway', 'bridge']):
                    topic.extend(['road'])
                if any(word in name_lower for word in ['emergency', 'warning', 'signal']):
                    topic.extend(['emergency', 'warning'])
                
                # Stop if we hit another project name or major section
                if (any(indicator.lower() in next_line.lower() for indicator in project_indicators) 
                    and 10 < len(next_line) < 150 and not next_line.startswith('(')):
                    break
                    
                j += 1
            
            # Determine project type
            project_type = 'capital'  # default
            if 'fema' in project_name.lower() or 'disaster' in project_name.lower() or 'recovery' in project_name.lower():
                project_type = 'disaster'
            
            # Clean up topics
            topic = list(set(topic)) if topic else []
            
            projects.append({
                'Project_Name': project_name,
                'topic': ','.join(topic) if topic else '',
                'type': project_type,
                'status': status,
                'st': st,
                'et': et,
                'source_file': filename
            })
        
        i += 1
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

print(f'Extracted {len(all_projects)} projects')

# Filter disaster-related projects that started in 2022
disaster_projects_2022 = []
for p in all_projects:
    if p['type'] == 'disaster' and p['st'] and '2022' in str(p['st']):
        disaster_projects_2022.append(p)

print(f'Found {len(disaster_projects_2022)} disaster projects that started in 2022')

# Print them
for p in disaster_projects_2022:
    print(f"- {p['Project_Name']} (st: {p['st']})")

print('__RESULT__:')
print(json.dumps({
    'total_projects': len(all_projects),
    'disaster_projects_2022': len(disaster_projects_2022),
    'project_names': [p['Project_Name'] for p in disaster_projects_2022]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}}

exec(code, env_args)
