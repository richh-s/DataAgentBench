code = """import json
import re

# Get the civic docs data file path
civic_docs_file = locals()['var_functions.query_db:2']

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded documents:', len(civic_docs))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements with park projects in 2022
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Look for park projects completed in 2022
        if '2022' in line and 'completed' in line.lower():
            # Check if this is about a park
            prev_lines = []
            line_idx = lines.index(line)
            for j in range(max(0, line_idx-3), line_idx):
                prev_lines.append(lines[j].strip())
            
            context = ' '.join(prev_lines + [line]).lower()
            
            if 'park' in context:
                # Extract project name (previous non-empty line before updates/schedule)
                project_name = 'Unknown Park Project'
                for prev_line in reversed(prev_lines):
                    if prev_line and not prev_line.startswith('(') and 'updates' not in prev_line.lower():
                        project_name = prev_line
                        break
                
                # Try to extract year from line
                year_match = re.search(r'(202\d)', line)
                year = year_match.group(1) if year_match else '2022'
                
                park_projects_2022.append({
                    'Project_Name': project_name,
                    'topic': 'park',
                    'status': 'completed',
                    'et': year,
                    'source_doc': filename,
                    'completion_line': line
                })

print('Found park projects in 2022:', len(park_projects_2022))

# Display findings
for p in park_projects_2022:
    print('Project:', p['Project_Name'])
    print('Doc:', p['source_doc'])
    print('Completion:', p['completion_line'])
    print('---')

# Save results
output_file = '/tmp/park_projects_2022.json'
with open(output_file, 'w') as f:
    json.dump(park_projects_2022, f, indent=2)

print('Saved results to:', output_file)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
