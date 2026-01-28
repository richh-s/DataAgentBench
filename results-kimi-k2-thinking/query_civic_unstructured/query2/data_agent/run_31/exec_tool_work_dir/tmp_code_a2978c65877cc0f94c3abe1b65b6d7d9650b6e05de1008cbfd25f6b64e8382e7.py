code = """import json
import re

# The civic_docs_path is stored in var_functions.query_db:12
civil_path = var_functions.query_db:12

# Load the full data
civic_docs_full = []
with open(civil_path, 'r') as f:
    civic_docs_full = json.load(f)

print(f"Total civic documents loaded: {len(civic_docs_full)}")

# Looking for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs_full:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into sections and look for park projects
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for project names (title case lines that contain park/project keywords)
        if any(keyword in line.lower() for keyword in ['park', 'project']) and len(line) > 10:
            # Check if it's a likely project name
            if line.istitle() or '"' in line:
                current_project = line.strip('"').strip()
        
        # Check if this line mentions completion in 2022
        if current_project and '2022' in line and 'completed' in line.lower():
            park_projects_2022.append({
                'project_name': current_project,
                'completion_note': line,
                'filename': filename
            })
            current_project = None

# Also search for broader patterns
for doc in civic_docs_full:
    text = doc.get('text', '').lower()
    
    # Find all occurrences of "completed" and "2022" near park references
    if 'completed' in text and '2022' in text:
        # Extract snippets around park keywords
        park_keywords = ['park shade structure', 'park walkway', 'park repairs', 'legacy park', 'bluffs park', 'point dume']
        
        for keyword in park_keywords:
            if keyword in text:
                # Find the section with this keyword
                idx = text.find(keyword)
                snippet = text[idx-100:idx+200]
                if 'completed' in snippet and '2022' in snippet:
                    # Check if we already have this project
                    project_name = keyword.title()
                    exists = any(p['project_name'].lower() == project_name.lower() for p in park_projects_2022)
                    if not exists:
                        park_projects_2022.append({
                            'project_name': project_name,
                            'completion_note': 'Construction completed in 2022',
                            'filename': doc.get('filename', '')
                        })

print(f"Park projects completed in 2022: {len(park_projects_2022)}")
for proj in park_projects_2022:
    print(f"- {proj['project_name']}")

# Create output with project names to match with funding
project_names = [proj['project_name'] for proj in park_projects_2022]

result = {
    'projects': park_projects_2022,
    'count': len(park_projects_2022),
    'project_names': project_names
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
