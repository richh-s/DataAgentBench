code = """import json
import re

# Load the civic documents data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Convert funding records to a dictionary for easier lookup
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[project_name] = amount

# Find park-related projects completed in 2022 by searching the text
park_projects_found = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document contains park, completed, and 2022
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        # Look for specific project patterns
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            lower_line = line.lower()
            
            # Skip empty lines
            if not line:
                continue
            
            # Look for park project names
            if 'park' in lower_line and len(line) > 10:
                # Check if this appears to be a project name (not a bullet point or parenthetical)
                if not line.startswith('(') and not line.startswith('\u2022') and not lower_line.startswith('status:') and not lower_line.startswith('updates:') and not lower_line.startswith('schedule:'):
                    # Check the context around this line for completion in 2022
                    context_start = max(0, i-2)
                    context_end = min(len(lines), i+5)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    
                    if 'completed' in context and '2022' in context:
                        park_projects_found.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(park_projects_found))

print('__RESULT__:')
result = {
    'projects': unique_projects,
    'count': len(unique_projects)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
