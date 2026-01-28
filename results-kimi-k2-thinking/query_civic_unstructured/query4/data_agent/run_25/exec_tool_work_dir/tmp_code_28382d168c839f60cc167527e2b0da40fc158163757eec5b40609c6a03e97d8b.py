code = """import json
import re

civic_docs_result = locals().get('var_functions.query_db:6')

# Load civic documents data
if isinstance(civic_docs_result, str) and '.json' in civic_docs_result:
    try:
        with open(civic_docs_result, 'r') as f:
            civic_docs = json.load(f)
    except Exception as e:
        civic_docs = []
else:
    civic_docs = civic_docs_result

# Parse projects from documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    current_project = None
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect project sections
        if line.startswith('Capital Improvement Projects'):
            section_type = 'unknown'
            if 'Design' in line:
                section_type = 'design'
            elif 'Construction' in line:
                section_type = 'construction'
            elif 'Not Started' in line:
                section_type = 'not started'
        
        # Look for project names (typically lines in ALL CAPS, not starting with special chars)
        if len(line) > 10 and line == line.upper() and not line.startswith('(') and not line.startswith('•'):
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'topic': '',
                'type': 'capital',  # Default for CIP projects
                'status': section_type if 'section_type' in locals() else '',
                'st': '',
                'et': ''
            }
        
        # Look for dates and schedule info
        if current_project and ':' in line:
            field_value = line.split(':', 1)
            if len(field_value) == 2:
                field = field_value[0].strip().lower()
                value = field_value[1].strip()
                
                # Check for spring 2022 dates
                if '2022' in value and 'spring' in value.lower():
                    if not current_project['st']:
                        current_project['st'] = value
                
                # Extract topics
                detect_topics = []
                if 'drain' in value.lower() or 'storm' in value.lower():
                    detect_topics.append('drainage')
                if 'fema' in value.lower():
                    detect_topics.append('FEMA')
                if 'road' in value.lower():
                    detect_topics.append('road')
                if 'park' in value.lower():
                    detect_topics.append('park')
                if 'bridge' in value.lower():
                    detect_topics.append('bridge')
                
                if detect_topics:
                    current_project['topic'] = ', '.join(detect_topics)
        
        # Detect disaster projects
        if current_project and ('fema' in line.lower() or 'caloes' in line.lower() or 'caljpia' in line.lower()):
            current_project['type'] = 'disaster'
        
        i += 1
    
    # Add last project
    if current_project and current_project.get('Project_Name'):
        projects.append(current_project)

# Count projects that started in Spring 2022
spring_2022_projects = []
for proj in projects:
    if proj.get('st') and '2022' in proj['st'] and 'spring' in proj['st'].lower():
        spring_2022_projects.append(proj)

# Debug info
debug_info = {
    'total_projects_found': len(projects),
    'spring_2022_projects': len(spring_2022_projects),
    'sample_projects': spring_2022_projects[:5]
}

print('__RESULT__:')
print(json.dumps(debug_info))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records'}

exec(code, env_args)
