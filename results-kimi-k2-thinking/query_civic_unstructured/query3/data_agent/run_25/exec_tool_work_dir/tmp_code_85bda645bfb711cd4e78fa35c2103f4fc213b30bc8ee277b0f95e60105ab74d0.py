code = """import json
import re

# Read the civic documents
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Extract projects from all documents
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for emergency or FEMA
    if not re.search(r'emergency|fema', text, re.IGNORECASE):
        continue
    
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for project patterns
        if line.isupper() and len(line) > 10:
            is_project = True
        elif '(FEMA' in line:
            is_project = True
        elif 'Project' in line and len(line) < 150:
            is_project = True
        else:
            is_project = False
            
        if is_project:
            # Look at surrounding context
            start_idx = max(0, i-3)
            end_idx = min(len(lines), i+20)
            context = ' '.join(lines[start_idx:end_idx])
            
            # Determine status
            status_lower = context.lower()
            if 'design' in status_lower:
                status = 'design'
            elif 'construction' in status_lower:
                status = 'construction'
            elif 'complete' in status_lower:
                status = 'completed'
            else:
                status = 'design'
            
            # Extract dates
            dates = re.findall(r'\d{4}-(?:Spring|Summer|Fall|Winter|\d{1,2})', context, re.IGNORECASE)
            st = dates[0] if dates else ''
            et = dates[-1] if len(dates) > 1 else ''
            
            topics = []
            if 'emergency' in text.lower():
                topics.append('emergency')
            if 'fema' in text.lower():
                topics.append('FEMA')
            topic_str = ', '.join(topics) if topics else 'emergency'
            
            project_info = {
                'Project_Name': line,
                'topic': topic_str,
                'type': 'disaster' if '(FEMA' in line else 'disaster',
                'status': status,
                'st': st,
                'et': et
            }
            
            all_projects.append(project_info)

# Remove duplicates
unique_projects = {}
for p in all_projects:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

final_projects = list(unique_projects.values())

result = json.dumps(final_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
