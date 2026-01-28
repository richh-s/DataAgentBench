code = """import json
import re
from pathlib import Path

# Load all civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Extract all projects from documents
all_projects = []

for doc in documents:
    text = doc.get('text', '')
    # Normalize text for easier parsing
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and common headings
        if line and len(line) > 5 and not any(skip in line.lower() for skip in [
            'capital improvement', 'disaster recovery', 'public works',
            'commission meeting', 'agenda report', 'recommended action',
            'subject:', 'page ', 'item ', 'council meeting'
        ]):
            
            # Look ahead for Updates section
            j = i + 1
            project_section = ''
            while j < len(lines) and '\\(cid:' not in lines[j]:
                project_section += lines[j] + '\n'
                if 'Updates:' in lines[j]:
                    break
                j += 1
            
            # Now analyze the project section
            section_lower = project_section.lower()
            
            # Check for completion in 2022
            completed_2022 = bool(re.search(r'construction was completed[^\n]*2022', section_lower, re.I)) or \
                           bool(re.search(r'complete construction[^\n]*2022', section_lower, re.I)) or \
                           bool(re.search(r'completed[^\n]*2022', section_lower, re.I))
            
            # Check if park-related
            park_related = bool(re.search(r'park', line, re.I)) or bool(re.search(r'playground', section_lower, re.I))
            
            if completed_2022 and park_related:
                all_projects.append({
                    'project_name': line,
                    'status': 'completed',
                    'et': '2022',
                    'park_related': True
                })
        
        i += 1

print('__RESULT__:')
result_data = {'park_projects_2022': all_projects, 'count': len(all_projects)}
# Ensure valid JSON
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
