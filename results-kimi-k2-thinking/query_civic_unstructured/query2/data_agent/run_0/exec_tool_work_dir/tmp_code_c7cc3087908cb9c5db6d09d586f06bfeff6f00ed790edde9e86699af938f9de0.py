code = """import json
import re
from pathlib import Path

# Load all civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Regex patterns to extract projects
# Looking for project name lines followed by status info
project_pattern = r'([^\n]+)\n\s*\\(cid:\d+\\) Updates:'
status_patterns = {
    'name': r'^([^\n]+?)(?:\s*\\\(cid:\d+\\))?$',
    'status': r'(?:^|\n)\s*([^\n]+?)\s*\\\(cid:\d+\\) Updates:',
    'completion': r'(?:Complete Construction|construction was completed|Completed)[^\n]*(\d{4})',
    'topic': r'topic:\s*([^\n]+)',
}

# Extract all projects from documents
all_projects = []

for doc in documents:
    text = doc.get('text', '').lower()
    # Split by project sections (they start with project names and have updates)
    sections = re.split(r'\n\s*\\\(cid:\d+\\) Updates:', doc.get('text', ''))
    
    for section in sections:
        if not section.strip():
            continue
            
        # Get the first line as potential project name
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        project_name = lines[0].strip()
        
        # Check if it's actually a project (not a heading)
        if len(project_name) < 5 or 'capital improvement' in project_name.lower() or \
           'disaster recovery' in project_name.lower() or \
           'public works' in project_name.lower():
            continue
        
        # Look for completion status in section
        section_text = section.lower()
        
        # Check for completion patterns
        completion_match = re.search(r'(?:construction was completed|complete construction|completed)[^\n]*2022', section_text, re.IGNORECASE)
        
        # Extract status
        status = None
        if 'completed' in section_text and '2022' in section_text:
            status = 'completed'
        elif 'design' in section_text or 'in design' in section_text:
            status = 'design'
        elif 'not started' in section_text or 'construction' in section_text:
            status = 'not started'
        
        # Look for park-related keywords
        park_related = bool(re.search(r'park', project_name, re.IGNORECASE)) or \
                      bool(re.search(r'park|playground', section_text))
        
        # Look for end date/et information
        et_match = re.search(r'(?:complete[d]?|construction|completed)[^\n]*(2022)', section_text, re.IGNORECASE)
        et = None
        if et_match:
            et = et_match.group(1)
        
        if status and park_related:
            all_projects.append({
                'project_name': project_name,
                'status': status,
                'et': et if et else '2022',
                'park_related': park_related,
                'extracted_from': doc.get('filename', '')
            })

# Filter for park-related projects completed in 2022
park_projects_2022 = [
    p for p in all_projects 
    if p['park_related'] and p['status'] == 'completed' and p['et'] == '2022'
]

print('__RESULT__:')
print(json.dumps({'park_projects_2022': park_projects_2022, 'count': len(park_projects_2022)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
