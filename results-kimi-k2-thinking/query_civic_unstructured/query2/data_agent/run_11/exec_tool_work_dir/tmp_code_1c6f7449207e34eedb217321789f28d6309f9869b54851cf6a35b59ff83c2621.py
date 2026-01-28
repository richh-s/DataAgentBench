code = """import json
import re

# Load data from the storage variables
civic_docs = var_functions.query_db:5
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

funding = var_functions.query_db:6
if isinstance(funding, str):
    with open(funding, 'r') as f:
        funding = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for park projects
        if 'Park' in line and len(line) > 5:
            # Skip headers
            skip_words = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date', 'Public Works', 'Commission', 'Agenda']
            if any(word in line for word in skip_words):
                continue
            if line.startswith('('):
                continue
            
            # Check next lines for completion in 2022
            next_text = ' '.join(lines[i:i+15])
            if 'completed' in next_text.lower() and '2022' in next_text:
                # More specific check for 2022 completion
                patterns = [r'completed[^\n]{0,100}2022', r'2022[^\n]{0,100}completed', r'november\s+2022', r'december\s+2022']
                for pattern in patterns:
                    if re.search(pattern, next_text, re.IGNORECASE):
                        park_projects_2022.append(line)
                        break

# Remove duplicates
unique_projects = list(set(park_projects_2022))

print('__RESULT__:')
print(json.dumps({'projects': unique_projects, 'count': len(unique_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
