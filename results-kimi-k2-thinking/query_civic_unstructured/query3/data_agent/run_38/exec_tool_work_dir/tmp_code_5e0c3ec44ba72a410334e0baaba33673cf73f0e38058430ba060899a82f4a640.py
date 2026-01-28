code = """import json
import re

# Read the documents
with open('var_functions.query_db:2', 'r') as f:
    documents = json.load(f)

print('Found', len(documents), 'documents')

projects = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check for emergency or FEMA keywords
    has_emergency = 'emergency' in text.lower()
    has_fema = 'fema' in text.lower()
    
    if has_emergency or has_fema:
        # Find project sections
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and not line.startswith('(') and not line.endswith(':'):
                # Check if next line indicates a project
                if i + 1 < len(lines) and '(cid:190)' in lines[i+1]:
                    project_name = line
                    
                    # Skip headers
                    if any(x in project_name for x in ['Project', 'Agenda', 'Public Works', 'Capital', 'Disaster']):
                        continue
                    
                    # Determine status from context
                    status = 'not started'
                    snippet = ' '.join(lines[i:i+10])
                    if 'under construction' in snippet.lower():
                        status = 'construction'
                    elif 'design' in snippet.lower():
                        status = 'design'
                    elif 'complete' in snippet.lower():
                        status = 'completed'
                    
                    # Build topic list
                    topic_list = []
                    if has_fema:
                        topic_list.append('FEMA')
                    if has_emergency:
                        topic_list.append('emergency')
                    
                    # Determine type
                    project_type = 'disaster' if has_fema else 'capital'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'topic': ','.join(topic_list),
                        'type': project_type,
                        'status': status,
                        'filename': filename
                    })

print('Extracted', len(projects), 'projects')

# Convert to JSON and output
print('__RESULT__:')
print(json.dumps(projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
