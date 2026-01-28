code = """import json, re

# Read both datasets
with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

with open('file_storage/functions.query_db:20.json', 'r') as f:
    funding_data = json.load(f)

# Extract projects from civic documents
def extract_projects_from_docs(docs):
    projects = []
    
    for doc in docs:
        text = doc['text']
        lines = text.split('\n')
        
        current_project = None
        collecting_project = False
        
        for line_idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Detect project sections - look for bolded or title-style project names
            # Often projects are mentioned in "Capital Improvement Projects" or "Disaster Recovery Projects" sections
            
            # Look for lines that look like project names (not too long, start with capital letters, contain key terms)
            if len(line) < 100 and not line.endswith(':') and not line.startswith('('):
                # Check if it contains project-related terms or is followed by project details
                project_terms = ['Park', 'Road', 'Project', 'Improvements', 'Repairs', 'Facility', 'Structure', 'Study', 
                                'Drainage', 'Bridge', 'Culvert', 'Walkway', 'Playground']
                
                if any(term in line for term in project_terms):
                    # Check next lines to see if this is actually a project
                    next_lines = ' '.join(lines[line_idx+1:line_idx+4]).lower()
                    if any(indicator in next_lines for indicator in ['updates:', 'project schedule:', 'description:', 'completion:', 'status:']):
                        current_project = line
                        collecting_project = True
                        
                        # Initialize project info
                        project_info = {
                            'Project_Name': current_project,
                            'topic': '',
                            'status': 'unknown',
                            'type': 'unknown',
                            'st': '',
                            'et': ''
                        }
                        
                        # Determine topic
                        topics = []
                        if any(kw in line.lower() for kw in ['park', 'playground', 'walkway']):
                            topics.append('park')
                        if any(kw in line.lower() for kw in ['storm', 'drain', 'drainage', 'culvert']):
                            topics.append('drainage')
                        if any(kw in line.lower() for kw in ['road', 'street', 'bridge', 'highway']):
                            topics.append('road')
                        if any(kw in line.lower() for kw in ['water', 'treatment', 'quality']):
                            topics.append('water treatment')
                        if any(kw in line.lower() for kw in ['warning', 'signal', 'sign', 'siren']):
                            topics.append('emergency warning')
                        if any(kw in line.lower() for kw in ['fire', 'fema']):
                            topics.append('FEMA')
                        
                        project_info['topic'] = ', '.join(topics) if topics else 'unknown'
                        
                        # Determine type
                        if 'Capital Improvement' in text:
                            project_info['type'] = 'capital'
                        elif 'Disaster Recovery' in text or 'FEMA' in line:
                            project_info['type'] = 'disaster'
                            
                        # Look for status and dates in following lines
                        for j in range(line_idx, min(line_idx + 10, len(lines))):
                            search_line = lines[j].lower()
                            
                            # Look for completion status
                            if any(indicator in search_line for indicator in ['completed', 'completion', 'complete construction']):
                                if '2022' in search_line:
                                    project_info['status'] = 'completed'
                                    project_info['et'] = '2022'
                                    # Try to extract month
                                    month_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', search_line, re.IGNORECASE)
                                    if month_match:
                                        project_info['et'] = month_match.group(0)
                                elif '2023' in search_line:
                                    project_info['status'] = 'completed'
                                    project_info['et'] = '2023'
                                        
                            # Look for design status
                            if 'design' in search_line:
                                project_info['status'] = 'design'
                                
                        projects.append(project_info)
                        collecting_project = False
    
    return projects

# Extract projects
extracted_projects = extract_projects_from_docs(civic_docs)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for proj in extracted_projects:
    if 'park' in proj['topic'].lower() and proj['status'] == 'completed' and '2022' in proj['et']:
        park_projects_2022.append(proj)

print('__RESULT__:')
print(json.dumps({
    'total_extracted_projects': len(extracted_projects),
    'park_projects_2022': park_projects_2022,
    'num_park_projects_2022': len(park_projects_2022)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
