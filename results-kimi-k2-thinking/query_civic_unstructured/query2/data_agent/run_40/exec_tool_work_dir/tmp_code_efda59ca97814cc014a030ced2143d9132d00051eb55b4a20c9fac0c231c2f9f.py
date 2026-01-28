code = """import json
import re

# Load the civic documents
civic_docs_path = locals()['var_functions.query_db:2']
print('Loading from:', civic_docs_path)

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

print('Total documents loaded:', len(civic_docs_data))

# Look for park projects completed in 2022
park_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    # Track project names
    project_name = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('('):
            continue
        
        # Look for potential project names (not bullet points, not agenda text)
        is_potential_name = True
        skip_patterns = ['capital improvement', 'public works', 'commission meeting', 'agenda report', 'page ', 'item', 'to:', 'prepared by:', 'approved by:', 'date prepared:', 'meeting date:', 'subject:', 'recommended action:', 'discussion:']
        for pattern in skip_patterns:
            if pattern in line.lower():
                is_potential_name = False
                break
        
        if is_potential_name and len(line) > 5 and not line.startswith('●'):
            # Look ahead for project indicators
            look_ahead = []
            for j in range(i+1, min(i+4, len(lines))):
                look_ahead.append(lines[j].strip())
            if any(indicator in ' '.join(look_ahead).lower() for indicator in ['updates:', 'schedule:', 'complete', 'project']):
                project_name = line
        
        # Look for completion info with 2022
        if project_name and '2022' in line and 'completed' in line.lower():
            # Check if it's a park project
            if 'park' in project_name.lower():
                year_match = re.search(r'(202\d)', line)
                year = year_match.group(1) if year_match else '2022'
                park_projects.append({
                    'Project_Name': project_name,
                    'topic': 'park',
                    'status': 'completed',
                    'et': year,
                    'source_doc': filename
                })
                project_name = None

print('Found park projects completed in 2022:', len(park_projects))

# Show results
for p in park_projects:
    print(p['Project_Name'], 'from', p['source_doc'])

# Save to file
output_path = '/tmp/park_projects_2022.json'
with open(output_path, 'w') as f:
    json.dump(park_projects, f, indent=2)

print('Saved to', output_path)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
