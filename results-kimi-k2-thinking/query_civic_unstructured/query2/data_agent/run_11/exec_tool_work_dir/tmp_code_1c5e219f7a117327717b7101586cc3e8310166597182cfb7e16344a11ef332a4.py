code = """import json
import re

# Load data from file paths
civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:6

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project names and their completion status
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this line might be a project name (contains Park, not a header, reasonable length)
        if ('Park' in line or 'park' in line) and len(line) > 5:
            # Skip headers and other non-project lines
            if any(skip in line for skip in ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Public Works', 'Commission']):
                continue
            if line.startswith('(') or line.startswith('cid'):
                continue
                
            # Look ahead for completion information
            next_section = '\n'.join(lines[i:i+15])
            
            # Check if completed in 2022
            if 'completed' in next_section.lower() and '2022' in next_section:
                # Look for more specific completion date
                if re.search(r'completed[^\n]*2022|2022[^\n]*completed', next_section, re.I):
                    park_projects_completed_2022.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects_completed_2022))

print('__RESULT__:')
print(json.dumps({
    'park_projects': unique_park_projects,
    'count': len(unique_park_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
