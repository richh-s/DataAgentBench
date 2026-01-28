code = """import json
import re

# Get the results from storage
civic_docs_result = locals().get('var_functions.query_db:6')

# Load civic documents data
if isinstance(civic_docs_result, str) and '/' in civic_docs_result:
    try:
        with open(civic_docs_result, 'r') as f:
            civic_docs = json.load(f)
    except:
        # Try to find the actual file
        import os
        for root, dirs, files in os.walk('/tmp'):
            for file in files:
                if 'tmp' in file and file.endswith('.json'):
                    civic_docs_result = os.path.join(root, file)
                    break
        with open(civic_docs_result, 'r') as f:
            civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

# Parse the civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    current_project = None
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project names (typically capitalized project names on their own line)
        if len(line) > 10 and not line.startswith('(') and not line.startswith('•') and line.isupper():
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': ''
            }
        
        # Look for status indicators
        elif line.startswith('Capital Improvement Projects (Design)') and current_project:
            current_project['type'] = 'capital'
            current_project['status'] = 'design'
        elif line.startswith('Capital Improvement Projects (Construction)') and current_project:
            current_project['type'] = 'capital'
            current_project['status'] = 'construction'
        elif line.startswith('Capital Improvement Projects (Not Started)') and current_project:
            current_project['type'] = 'capital'
            current_project['status'] = 'not started'
        
        # Look for schedule/schedule information
        elif ': ' in line and current_project:
            parts = line.split(': ')
            if len(parts) == 2:
                field = parts[0].strip().lower()
                value = parts[1].strip()
                
                if 'begin construction' in field or 'advertise' in field or 'complete' in field:
                    if '2022' in value or value.lower().startswith('spring') or 'spring 2022' in value.lower():
                        if current_project['st'] == '':
                            current_project['st'] = value
                    if '2023' in value or value.lower().startswith('spring 2023'):
                        if 'et' not in current_project:
                            current_project['et'] = value
                
                # Extract topics from the value
                topics = []
                if 'drain' in value.lower() or 'storm' in value.lower():
                    topics.append('drainage')
                if 'fema' in value.lower():
                    topics.append('FEMA')
                if 'road' in value.lower():
                    topics.append('road')
                if 'park' in value.lower():
                    topics.append('park')
                if 'bridge' in value.lower():
                    topics.append('bridge')
                if 'playground' in value.lower():
                    topics.append('playground')
                if 'water' in value.lower() or 'treatment' in value.lower():
                    topics.append('water treatment')
                
                if topics:
                    current_project['topic'] = ', '.join(topics)
        
        # Try to detect disaster projects
        if current_project and ('fema' in line.lower() or 'caloes' in line.lower() or 'caljpia' in line.lower()):
            current_project['type'] = 'disaster'
        
        i += 1
    
    # Add the last project
    if current_project and current_project['Project_Name']:
        projects.append(current_project)

# Debug: print some projects
debug_info = {
    'num_projects': len(projects),
    'sample_projects': projects[:10] if projects else []
}

print('__RESULT__:')
print(json.dumps(debug_info))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records'}

exec(code, env_args)
