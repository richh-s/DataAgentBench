code = """import json
import re
import os

# Read the civic documents data
civic_docs_data = locals()['var_functions.query_db:14']

# Load the data if it's a file path
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents")

# First, let's just scan the text for completed projects in 2022
completed_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for patterns like "completed November 2022", "completed, November 2022", etc.
    # Also look for project names that might be park-related
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this line mentions completion in 2022
        if 'completed' in line.lower() and '2022' in line:
            # Look backwards to find the project name (usually a few lines above)
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('●') and not prev_line.startswith('■'):
                    # This might be a project name
                    if len(prev_line) < 100 and '·' not in prev_line:
                        project_name = prev_line
                        break
            
            if project_name:
                completed_2022_projects.append({
                    'project_name': project_name,
                    'completion_line': line,
                    'context': '\n'.join(lines[max(0, i-3):i+2])
                })

print(f"\nFound {len(completed_2022_projects)} potentially completed projects:")
for proj in completed_2022_projects:
    print(f"- {proj['project_name']}: {proj['completion_line']}")
    
# Check for park-related keywords
park_keywords = ['park', 'playground', 'slope', 'walkway', 'shade', 'green streets']
park_projects = []

for proj in completed_2022_projects:
    proj_name_lower = proj['project_name'].lower()
    if any(keyword in proj_name_lower for keyword in park_keywords):
        park_projects.append(proj)

print(f"\nFound {len(park_projects)} park-related projects completed in 2022:")
for proj in park_projects:
    print(f"- {proj['project_name']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
