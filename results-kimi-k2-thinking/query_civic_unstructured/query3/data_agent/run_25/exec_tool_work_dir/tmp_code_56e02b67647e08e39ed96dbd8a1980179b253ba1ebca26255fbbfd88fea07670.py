code = """import json
import re

# Read the civic documents
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Extract projects from all documents
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Only process documents with emergency or FEMA
    if not re.search(r'emergency|fema', text, re.IGNORECASE):
        continue
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for project patterns
        is_project = False
        
        if line.isupper() and len(line) > 10:
            is_project = True
        elif 'Project' in line and len(line) < 150:
            is_project = True
        elif '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line:
            is_project = True
        elif 'Improvements' in line and len(line) < 150:
            is_project = True
        elif 'Emergency' in line and len(line) < 150:
            is_project = True
            
        if is_project:
            project_info = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': ''
            }
            
            # Set type
            if '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line or 'Disaster' in line:
                project_info['type'] = 'disaster'
            elif 'Capital' in line:
                project_info['type'] = 'capital'
            else:
                project_info['type'] = 'disaster'
            
            # Look at context for status and dates
            start_idx = max(0, i-3)
            end_idx = min(len(lines), i+20)
            context = ' '.join(lines[start_idx:end_idx])
            
            # Determine status
            status_lower = context.lower()
            if 'design' in status_lower and 'complete design' not in status_lower:
                project_info['status'] = 'design'
            elif 'construction' in status_lower and 'completed' not in status_lower:
                project_info['status'] = 'construction'
            elif 'complete' in status_lower:
                project_info['status'] = 'completed'
            else:
                project_info['status'] = 'design'
            
            # Extract dates
            date_patterns = [
                r'(\d{4}-(?:Spring|Summer|Fall|Winter))',
                r'(\d{4}-\d{1,2})'
            ]
            
            all_dates = []
            for pattern in date_patterns:
                matches = re.findall(pattern, context, re.IGNORECASE)
                all_dates.extend(matches)
            
            if all_dates:
                project_info['st'] = all_dates[0]
                if len(all_dates) > 1:
                    project_info['et'] = all_dates[-1]
            
            # Set topic
            topics = []
            if 'emergency' in text.lower():
                topics.append('emergency')
            if 'fema' in text.lower():
                topics.append('FEMA')
            project_info['topic'] = ', '.join(topics) if topics else 'emergency'
            
            all_projects.append(project_info)

# Remove duplicates
unique_projects = {p['Project_Name']: p for p in all_projects}
final_projects = list(unique_projects.values())

result = json.dumps(final_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
