code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:5']
mongo_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(mongo_file, 'r') as f:
    mongo_data = json.load(f)

# Extract projects from MongoDB documents
projects = []

for doc in mongo_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Pattern: Project name on one line, then updates/schedule info
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            i += 1
            continue
            
        # Look for potential project names (lines that are title-like and not standard headers)
        if (len(line) > 5 and 
            not line.startswith('To:') and 
            not line.startswith('Prepared by:') and 
            not line.startswith('Approved by:') and
            not line.startswith('Meeting date:') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED ACTION:') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Public Works') and
            not line.startswith('Commission') and
            not line.startswith('To:') and
            not line.startswith('Date prepared:') and
            '(cid:' not in line):
            
            # Check if next lines contain project info
            project_name = line
            status = None
            et = None
            topic = []
            
            # Look ahead for status and date info
            j = i + 1
            while j < min(i + 10, len(lines)):
                next_line = lines[j].strip()
                
                if 'completed' in next_line.lower():
                    status = 'completed'
                    # Look for date
                    date_match = re.search(r'(\w+\s+\d{4}|\d{4}-\w+|\d{4})', next_line)
                    if date_match:
                        et = date_match.group(1)
                        if '2022' in next_line:
                            et = '2022'
                
                # Determine topics based on keywords
                if 'park' in project_name.lower():
                    topic.append('park')
                if 'drainage' in project_name.lower() or 'storm drain' in project_name.lower():
                    topic.append('drainage')
                if 'road' in project_name.lower():
                    topic.append('road')
                if 'FEMA' in project_name or 'fema' in next_line.lower():
                    topic.append('FEMA')
                    
                j += 1
            
            # If we found a project with info, add it
            if project_name and len(project_name) < 200:  # Reasonable length
                if not topic:
                    # Try to infer topic from name
                    if 'park' in project_name.lower():
                        topic = ['park']
                    elif 'road' in project_name.lower():
                        topic = ['road']
                    elif 'drainage' in project_name.lower() or 'storm' in project_name.lower():
                        topic = ['drainage']
                    else:
                        topic = ['other']
                        
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'et': et,
                    'topic': topic
                })
                
        i += 1

# Identify park-related projects completed in 2022
park_projects_2022 = []
for proj in projects:
    if (proj['status'] == 'completed' and 
        proj['et'] and '2022' in proj['et'] and 
        'park' in proj['topic']):
        park_projects_2022.append(proj['Project_Name'])

print('__RESULT__:')
print(json.dumps(park_projects_2022, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
