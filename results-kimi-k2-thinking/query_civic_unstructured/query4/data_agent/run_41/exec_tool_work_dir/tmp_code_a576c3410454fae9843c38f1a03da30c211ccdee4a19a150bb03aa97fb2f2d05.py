code = """import json
import re

# Load the full result from the file
with open('/tmp/tmp_d5q7p7j.json', 'r') as f:
    documents = json.load(f)

print('Number of documents:', len(documents))

# Extract project information from documents
spring_docs = []
for doc_idx, doc in enumerate(documents):
    text = doc['text']
    filename = doc['filename']
    
    # Look for Spring 2022 mentions
    if 'Spring' in text and '2022' in text:
        spring_docs.append({
            'doc_idx': doc_idx,
            'filename': filename
        })

print('Documents mentioning Spring 2022:', len(spring_docs))

# Now extract more detailed project information
projects_data = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    
    # Split into sections and look for project information
    # Look for capital improvement projects and disaster recovery projects
    
    # Simple approach: find all occurrences of Spring 2022 and extract surrounding context
    for match in re.finditer(r'[^.\n]*Spring[^.\n]*2022[^.\n]*|[^.\n]*2022[^.\n]*Spring[^.\n]*', text, re.IGNORECASE):
        context = match.group(0).strip()
        # Try to find project name in nearby lines
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if context in line:
                # Look for project name (previous non-empty line that looks like a title)
                for j in range(i-1, max(-1, i-10), -1):
                    if lines[j].strip() and not lines[j].strip().startswith('('):
                        project_name = lines[j].strip()
                        if len(project_name) < 150 and not any(word in project_name.lower() for word in ['update', 'schedule', 'status', 'project']):
                            projects_data.append({
                                'project_name': project_name,
                                'context': context,
                                'filename': filename
                            })
                        break
                break

print('Found', len(projects_data), 'potential projects')

# Count unique project names
unique_projects = set()
for p in projects_data:
    unique_projects.add(p['project_name'])

print('Unique projects:', len(unique_projects))

result = {
    'total_found': len(projects_data),
    'unique_count': len(unique_projects),
    'projects': list(unique_projects)[:20]  # First 20 for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
