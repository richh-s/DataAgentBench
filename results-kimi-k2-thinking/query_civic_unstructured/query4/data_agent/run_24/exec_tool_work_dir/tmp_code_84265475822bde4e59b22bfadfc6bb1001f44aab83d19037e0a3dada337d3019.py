code = """import json

file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print('Loaded', len(documents), 'documents')

projects = []

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Simple pattern: look for project names followed by Spring 2022 dates
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Basic heuristic for project names
        if len(line) > 10 and line[0].isupper():
            # Look for project keywords
            if any(kw in line.lower() for kw in ['project', 'improvements', 'repairs', 'park', 'road']):
                # Check surrounding lines for Spring 2022
                for j in range(i, min(i+5, len(lines))):
                    if '2022' in lines[j] and ('Spring' in lines[j] or 'spring' in lines[j]):
                        projects.append(line)
                        break

unique_projects = list(set(projects))
print('Found', len(unique_projects), 'unique projects')

result = json.dumps({'count': len(unique_projects), 'projects': unique_projects})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
