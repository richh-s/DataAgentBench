code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Look for specific patterns indicating completion in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Pattern 1: "Construction was completed, November 2022" with preceding project name
    pattern1 = r'([A-Z][a-zA-Z\s\-\&]+?)\s*\n.*?Construction was completed[^\n]*2022'
    matches = re.finditer(pattern1, text, re.IGNORECASE | re.DOTALL)
    
    for match in matches:
        project_name = match.group(1).strip()
        if 'park' in project_name.lower():
            # Extract completion date
            date_match = re.search(r'(\w+\s+2022)', match.group(0))
            date = date_match.group(1) if date_match else '2022'
            park_projects_2022.append({
                'Project_Name': project_name,
                'completion_date': date
            })
    
    # Pattern 2: "Complete Construction: Summer 2022"
    pattern2 = r'([A-Z][a-zA-Z\s\-\&]+?)\s*\n.*?Complete Construction[^:]*:\s*([^\n]*2022)'
    matches = re.finditer(pattern2, text, re.IGNORECASE | re.DOTALL)
    
    for match in matches:
        project_name = match.group(1).strip()
        if 'park' in project_name.lower():
            park_projects_2022.append({
                'Project_Name': project_name,
                'completion_date': match.group(2).strip()
            })

print(f'Found {len(park_projects_2022)} park projects completed in 2022')
for proj in park_projects_2022:
    print(f'  - {proj["Project_Name"]} ({proj["completion_date"]})')

result = {'park_projects_2022': park_projects_2022}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'file_path': 'file_storage/functions.query_db:6.json', 'doc_count': 5}, 'var_functions.execute_python:22': {'text_length': 63698, 'doc_count': 5}}

exec(code, env_args)
