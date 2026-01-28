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
    if re.search(r'Spring.*2022', text, re.IGNORECASE) or \
       re.search(r'2022.*Spring', text, re.IGNORECASE) or \
       re.search(r'2022-Spring', text, re.IGNORECASE):
        spring_docs.append({
            'doc_idx': doc_idx,
            'filename': filename,
            'text_snippet': text[:500]
        })

print('Documents mentioning Spring 2022:', len(spring_docs))

# Now try to extract more detailed project information
projects_in_spring_2022 = []

for doc in documents:
    text = doc['text']
    
    # Look for project patterns
    # Try to find project names and their schedules/dates
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Look for patterns that might indicate projects starting in Spring 2022
        if ('Spring 2022' in line or '2022-Spring' in line or 
            ('2022' in line and 'Spring' in line)):
            # Look backward for project name
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    if len(prev_line) < 100 and not any(keyword in prev_line.lower() 
                                                       for keyword in ['update', 'schedule', 'status']):
                        project_name = prev_line
                        break
            
            if project_name:
                projects_in_spring_2022.append({
                    'project_name': project_name,
                    'context': line.strip(),
                    'filename': doc['filename']
                })

print('Potential projects with Spring 2022 start:', len(projects_in_spring_2022))
for p in projects_in_spring_2022[:5]:
    print('Project:', p['project_name'])
    print('Context:', p['context'])
    print('---')

print('__RESULT__:')
print(json.dumps(projects_in_spring_2022))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
