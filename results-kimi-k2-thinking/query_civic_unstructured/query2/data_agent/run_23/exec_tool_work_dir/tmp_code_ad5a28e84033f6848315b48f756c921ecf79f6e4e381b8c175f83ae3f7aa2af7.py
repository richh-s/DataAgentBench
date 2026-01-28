code = """import json
import re

# Read the civic documents data
civic_docs_data = locals()['var_functions.query_db:14']

# Load the data if it's a file path
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print(f'Loaded {len(civic_docs_data)} civic documents')

# Look for completed projects in 2022
completed_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Check if line mentions completion in 2022
        if 'completed' in line_lower and '2022' in line:
            # Look back for project name
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) < 100:
                    # Skip lines with bullet points
                    if '●' not in prev_line and '■' not in prev_line and '·' not in prev_line:
                        if 'Updates:' not in prev_line and 'Project Schedule:' not in prev_line:
                            project_name = prev_line
                            break
            
            if project_name:
                completed_2022.append({
                    'project_name': project_name,
                    'completion_note': line.strip()
                })

print(f'Found {len(completed_2022)} completed projects in 2022')

# Filter for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume', 'point dume']
park_projects = []

for proj in completed_2022:
    proj_name_lower = proj['project_name'].lower()
    if any(keyword in proj_name_lower for keyword in park_keywords):
        park_projects.append(proj)

print(f'Found {len(park_projects)} park-related projects:')
for proj in park_projects:
    print(f'  Project: {proj["project_name"]}. Note: {proj["completion_note"]}')

result = {
    'completed_2022_count': len(completed_2022),
    'park_projects': park_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
