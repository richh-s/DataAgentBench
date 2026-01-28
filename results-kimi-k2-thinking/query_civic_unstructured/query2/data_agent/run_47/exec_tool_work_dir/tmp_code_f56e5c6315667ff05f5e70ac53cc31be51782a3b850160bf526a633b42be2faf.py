code = """import json
import re
from collections import defaultdict

# Load the civic documents data
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract projects from document text
def extract_projects_from_text(text):
    projects = []
    
    # Patterns to identify project sections
    # Capital Improvement Projects - Construction, Design, Not Started
    sections = re.split(r'\n\s*Capital Improvement Projects\s*\((Design|Construction|Not Started)\)', text, flags=re.IGNORECASE)
    
    for i in range(1, len(sections), 2):
        section_type = sections[i]
        section_text = sections[i+1]
        
        # Split into individual projects
        project_blocks = re.split(r'\n\s*(?=[A-Z][a-zA-Z\s\-\&\(\)]+\n)', section_text)
        
        for block in project_blocks:
            if not block.strip() or len(block.strip()) < 10:
                continue
                
           lines = block.split('\n')
            if not lines:
                continue
                
            # Extract project name from first line
            project_name = lines[0].strip()
            if not project_name or len(project_name) < 3 or 'Project Description' in project_name:
                continue
            
            # Extract status
            status = 'design' if 'Design' in section_type else 'not started' if 'Not Started' in section_type else 'completed'
            
            # Extract dates
            st = None
            et = None
            
            # Look for date patterns
            if 'Project Schedule' in block:
                schedule_part = block.split('Project Schedule')[-1]
                date_patterns = [
                    r'Complete:\s*(\w+\s+\d{4})',
                    r'Complete\s*:\s*(\w+\s+\d{4})',
                    r'Completed\s*:\s*(\w+\s+\d{4})',
                    r'Construction was completed\s*,\s*(\w+\s+\d{4})',
                    r'Complete Construction:\s*(\w+\s+\d{4})',
                    r'Begin Construction:\s*(\w+\s+\d{4})',
                    r'Advertise:\s*(\w+\s+\d{4})'
                ]
                
                for pattern in date_patterns:
                    match = re.search(pattern, schedule_part, re.IGNORECASE)
                    if match:
                        et = match.group(1)
                        break
            
            # Extract topics based on keywords
            topics = []
            lower_text = block.lower()
            
            keyword_topics = {
                'park': ['park', 'playground', 'skate park'],
                'road': ['road', 'street', 'highway', 'avenue', 'drive', 'way'],
                'drainage': ['drainage', 'storm drain', 'drain'],
                'bridge': ['bridge', 'overcrossing'],
                'emergency warning': ['warning', 'siren', 'sign'],
                'fire': ['fire'],
                'fema': ['fema']
            }
            
            for topic, keywords in keyword_topics.items():
                if any(keyword in lower_text for keyword in keywords):
                    topics.append(topic)
            
            # Add to projects list
            project_info = {
                'Project_Name': project_name,
                'status': status,
                'st': st,
                'et': et,
                'topic': ', '.join(topics) if topics else None,
                'type': 'capital'  # Most projects in this context are capital projects
            }
            
            projects.append(project_info)
    
    # Look for Disaster Recovery projects specifically
    disaster_matches = re.findall(
        r'([A-Z][a-zA-Z\s\-\&\(\)]+?)\s*\(FEMA.*Project.*\).*?Construction was completed[,\s]*([A-Za-z]+\s+\d{4})',
        text,
        re.IGNORECASE | re.DOTALL
    )
    
    for match in disaster_matches:
        project_name = match[0].strip()
        completion_date = match[1]
        
        projects.append({
            'Project_Name': project_name,
            'status': 'completed',
            'st': None,
            'et': completion_date,
            'topic': 'FEMA, fire, disaster',
            'type': 'disaster'
        })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Remove duplicates based on project name
unique_projects = {}
for proj in all_projects:
    name = proj['Project_Name']
    if name not in unique_projects or proj.get('et') is not None:
        unique_projects[name] = proj

projects_list = list(unique_projects.values())

print("__RESULT__:")
print(json.dumps(projects_list, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
