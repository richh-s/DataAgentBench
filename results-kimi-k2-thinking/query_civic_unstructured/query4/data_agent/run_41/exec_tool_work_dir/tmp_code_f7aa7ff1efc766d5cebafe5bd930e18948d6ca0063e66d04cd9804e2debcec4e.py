code = """import json
import re

# Load the filtered documents mentioning Spring 2022
with open('/tmp/tmp_zu5y9j5.json', 'r') as f:
    spring_docs = json.load(f)

print('Number of Spring 2022 documents:', len(spring_docs))

# Extract project names and information
spring_2022_projects = []

for doc in spring_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Split into sections
    sections = re.split(r'\n(?=\S)', text)
    
    current_section = None
    in_project_section = False
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Check if this is a project section
        if section.startswith('Capital Improvement Projects') or section.startswith('Disaster Projects'):
            current_section = section
            in_project_section = True
            continue
            
        if in_project_section:
            # Look for project names (typically bold or capitalized)
            lines = section.split('\n')
            project_name = None
            
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                
                # Project name is usually the first non-empty line in a project description
                # that doesn't start with special characters
                if (line[0].isupper() and 
                    not line.startswith('(') and 
                    not line.startswith('•') and 
                    not line.startswith('●') and
                    not line.startswith('cid:') and
                    not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'description', 'status', 'begin construction', 'complete design']) and
                    len(line) < 150):
                    
                    project_name = line
                    # Look for dates in the next few lines
                    date_context = []
                    for j in range(i, min(i+10, len(lines))):
                        date_line = lines[j].strip()
                        if ('Spring 2022' in date_line or '2022-Spring' in date_line or 
                            ('2022' in date_line and 'Spring' in date_line)):
                            date_context.append(date_line)
                    
                    if date_context and project_name:
                        spring_2022_projects.append({
                            'project_name': project_name,
                            'section': current_section,
                            'filename': filename
                        })
                        break

# Get unique project names
unique_projects = {}
for p in spring_2022_projects:
    name = p['project_name']
    if name not in unique_projects:
        unique_projects[name] = p

print('Unique Spring 2022 projects found:', len(unique_projects))
print('\nProject names:')
for name in sorted(unique_projects.keys()):
    print('-', name)

result = {
    'count': len(unique_projects),
    'projects': list(unique_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
