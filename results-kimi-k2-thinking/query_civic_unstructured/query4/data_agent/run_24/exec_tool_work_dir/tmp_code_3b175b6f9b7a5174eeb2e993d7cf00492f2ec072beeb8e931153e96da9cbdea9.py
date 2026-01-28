code = """import json
import re

file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print('Loaded', len(documents), 'documents')

spring_2022_projects = []

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for project patterns and Spring 2022 dates in the text
    # Projects often have titles in uppercase or title case
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip if line is too short
        if len(line) < 10:
            continue
        
        # Check if line is capitalized (potential project name)
        if line and line[0].isupper():
            # Check if it contains project-related terms
            project_terms = ['Project', 'Improvements', 'Repairs', 'Facility', 'Park', 'Road', 'Drainage', 'Bridge', 'Playground']
            has_term = any(term.lower() in line.lower() for term in project_terms)
            
            if has_term:
                # Look for Spring 2022 in surrounding text
                context_start = max(0, i-2)
                context_end = min(len(lines), i+8)
                context = ' '.join(lines[context_start:context_end])
                
                # Check for Spring 2022 patterns
                if '2022' in context and ('Spring' in context or 'March' in context or 'April' in context or 'May' in context):
                    # Check if it's related to project timing (Advertise, Begin, etc.)
                    if 'Advertise' in context or 'Begin' in context or 'Start' in context or 'Complete' in context:
                        spring_2022_projects.append(line)
                        print('Found:', line)

# Remove duplicates
unique_projects = list(set(spring_2022_projects))

result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
