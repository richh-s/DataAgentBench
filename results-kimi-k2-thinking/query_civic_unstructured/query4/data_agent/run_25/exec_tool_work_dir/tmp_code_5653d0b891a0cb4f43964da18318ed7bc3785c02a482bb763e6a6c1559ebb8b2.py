code = """import json
import re

civic_docs_result = locals().get('var_functions.query_db:6')

# Load civic documents data
if isinstance(civic_docs_result, str):
    try:
        with open(civic_docs_result, 'r') as f:
            civic_docs = json.load(f)
    except Exception:
        civic_docs = civic_docs_result if isinstance(civic_docs_result, list) else []
else:
    civic_docs = civic_docs_result

# Parse projects from documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Detect section headers
        if line.startswith('Capital Improvement Projects'):
            if 'Design' in line:
                current_section = 'design'
            elif 'Construction' in line:
                current_section = 'construction'
            elif 'Not Started' in line:
                current_section = 'not started'
        
        # Look for project names (all caps, no special chars at start)
        if line and len(line) > 10 and line == line.upper() and not line.startswith('('):
            project = {
                'Project_Name': line,
                'topic': '',
                'type': 'capital',
                'status': current_section or '',
                'st': '',
                'et': ''
            }
            projects.append(project)
        
        # Look for disaster project indicators
        if projects and ('fema' in line.lower() or 'caloes' in line.lower() or 'caljpia' in line.lower()):
            projects[-1]['type'] = 'disaster'
        
        # Look for schedule info with dates
        if projects and ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                value = parts[1].strip()
                
                # Check for spring 2022 start dates
                if '2022' in value and 'spring' in value.lower():
                    if not projects[-1]['st']:
                        projects[-1]['st'] = value
                
                # Extract topics from value
                if 'drain' in value.lower() or 'storm' in value.lower():
                    if projects[-1]['topic']: 
                        projects[-1]['topic'] += ', drainage'
                    else:
                        projects[-1]['topic'] = 'drainage'
                if 'fema' in value.lower():
                    if projects[-1]['topic']:
                        projects[-1]['topic'] += ', FEMA'
                    else:
                        projects[-1]['topic'] = 'FEMA'
                if 'road' in value.lower():
                    if projects[-1]['topic']:
                        projects[-1]['topic'] += ', road'
                    else:
                        projects[-1]['topic'] = 'road'

# Count projects starting in Spring 2022
spring_2022_projects = []
for proj in projects:
    st = proj.get('st', '')
    if st and '2022' in st and 'spring' in st.lower():
        spring_2022_projects.append(proj)

# Debug
result = {
    'total_projects': len(projects),
    'spring_2022_count': len(spring_2022_projects),
    'sample_spring_2022': spring_2022_projects[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records'}

exec(code, env_args)
