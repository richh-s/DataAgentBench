code = """import json
import re

# Access the file path
file_info = locals()['var_functions.query_db:10']
print('File path:', file_info)

# Read the data
with open(file_info, 'r') as f:
    docs = json.load(f)

print('Total documents:', len(docs))

# Simple pattern matching for park projects completed in 2022
park_projects = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find all mentions of park projects with 2022 completion
    # Look for 'Park' followed by project type keywords
    text_lower = text.lower()
    
    # Check if this document mentions 2022 completion
    if '2022' in text and 'completed' in text_lower:
        # Extract lines that mention park
        lines = text.split('\n')
        for line in lines:
            if 'Park' in line and len(line) > 10:
                # Check if this line looks like a project name
                clean_line = line.strip()
                if any(word in clean_line for word in ['Repair', 'Improvement', 'Project', 'Structure', 'Walkway', 'Shade', 'Playground']):
                    park_projects.append({
                        'name': clean_line,
                        'file': filename
                    })

# Remove duplicates
seen_names = set()
unique_projects = []
for p in park_projects:
    if p['name'] not in seen_names:
        seen_names.add(p['name'])
        unique_projects.append(p)

print('Found projects:', len(unique_projects))
for p in unique_projects:
    print('-', p['name'])

# Create result
result = {
    'projects': unique_projects,
    'count': len(unique_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
