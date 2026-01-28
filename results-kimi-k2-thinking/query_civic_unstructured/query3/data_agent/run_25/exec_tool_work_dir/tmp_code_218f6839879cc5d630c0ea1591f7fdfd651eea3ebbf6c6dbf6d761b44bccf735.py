code = """import json
import re
from collections import defaultdict

# Read the civic documents
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    if not re.search(r'emergency|fema', text, re.IGNORECASE):
        return projects
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name (various patterns)
        is_project = False
        patterns = ['Project', 'Improvements', 'Repairs', 'Facility', 'System', 'Park', 'Road', 'Structure']
        
        if line.isupper() and len(line) > 10:
            is_project = True
        elif any(pattern in line for pattern in patterns) and len(line) < 150:
            is_project = True
        elif '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line:
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
                
            # Determine type based on content
            if '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line or 'Disaster' in line:
                project_info['type'] = 'disaster'
            elif 'Capital' in line or 'Improvement' in line or 'Infrastructure' in line:
                project_info['type'] = 'capital'
            else:
                project_info['type'] = 'disaster'  # Default to disaster for emergency/fema projects
            
            # Look at next few lines for status and dates
            next_lines_start = max(0, i-5)  # Look a bit before and after
            next_lines_end = min(len(lines), i+25)
            context = '\n'.join(lines[next_lines_start:next_lines_end])
            
            # Determine status
            if 'design' in context.lower() and 'complete design' not in context.lower():
                project_info['status'] = 'design'
            elif 'construction' in context.lower() and ('completed' not in context.lower() or 'complete construction' in context.lower()):
                project_info['status'] = 'construction'
            elif 'complete' in context.lower() or 'completed' in context.lower():
                project_info['status'] = 'completed'
            elif 'not started' in context.lower():
                project_info['status'] = 'not started'
            else:
                project_info['status'] = 'design'  # Default
            
            # Look for dates
            date_patterns = [
                r'(\d{4}-(?:Spring|Summer|Fall|Winter))',
                r'(\d{4}-(?:January|February|March|April|May|June|July|August|September|October|November|December))',
                r'(\d{4}-\d{1,2})',
            ]
            
            all_dates = []
            for date_pattern in date_patterns:
                matches = re.findall(date_pattern, context, re.IGNORECASE)
                all_dates.extend(matches)
            
            if all_dates:
                project_info['st'] = all_dates[0]
                if len(all_dates) > 1:
                    project_info['et'] = all_dates[-1]
            
            # Determine topic based on keywords
            topics = []
            text_lower = text.lower()
            if 'emergency' in text_lower:
                topics.append('emergency')
            if 'fema' in text_lower:
                topics.append('FEMA')
            if 'fire' in text_lower:
                topics.append('fire')
            if 'warning' in text_lower or 'siren' in text_lower:
                topics.append('emergency warning')
                    
            project_info['topic'] = ', '.join(topics) if topics else 'emergency'
            
            projects.append(project_info)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    if projects:
        all_projects.extend(projects)

# Remove duplicates based on project name
unique_projects = {}
for project in all_projects:
    name = project['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = project

filtered_projects = list(unique_projects.values())

result = json.dumps(filtered_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
