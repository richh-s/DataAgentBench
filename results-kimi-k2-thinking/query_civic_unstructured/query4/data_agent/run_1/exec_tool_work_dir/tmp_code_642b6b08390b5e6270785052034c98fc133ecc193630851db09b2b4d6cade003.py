code = """import json

with open(var_functions.query_db:5, 'r') as f:
    civic_docs = json.load(f)

print('Documents count:', len(civic_docs))

# Look for Spring 2022 patterns
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if any spring pattern exists in text
    for pattern in spring_patterns:
        if pattern in text:
            # Try to extract project names - look for lines before the pattern
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if pattern in line:
                    # Look back up to 5 lines for a project name
                    for j in range(max(0, i-5), i):
                        prev_line = lines[j].strip()
                        # Heuristic: project names often start with caps, not too short, not common headers
                        if (prev_line and len(prev_line) > 5 and prev_line[0].isupper() and 
                            'Updates' not in prev_line and 'Schedule' not in prev_line and 
                            'Agenda' not in prev_line and 'Page' not in prev_line):
                            spring_2022_projects.append({
                                'project_name': prev_line,
                                'pattern': pattern,
                                'filename': filename
                            })
                            break
            break

print('Found', len(spring_2022_projects), 'Spring 2022 project mentions')

# Get unique project names
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

print('Unique Spring 2022 projects:', len(unique_projects))
for p in list(unique_projects.values())[:10]:
    print('-', p['project_name'])

result = {
    'count': len(unique_projects),
    'projects': list(unique_projects.keys())
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
