code = """import json
import re

# Load the funding data from the file
funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents data from the file
civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract the text from the first document
text = civic_docs[0]['text']

# Initialize list to store extracted projects
projects = []

# Find the design section
design_start = text.find('Capital Improvement Projects (Design)')
construction_start = text.find('Capital Improvement Projects (Construction)')

if design_start > 0 and construction_start > design_start:
    design_section = text[design_start:construction_start]
    lines = design_section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for lines that are likely project names
        if line and not line.startswith('(cid:') and not line.startswith('Page') and len(line) > 5:
            # Check if next line has project markers
            next_line = lines[i+1] if i+1 < len(lines) else ''
            if '(cid:' in next_line or 'Updates:' in next_line:
                projects.append(line)

# Remove duplicates
unique_projects = list(set(projects))

print('__RESULT__:')
result = {
    'extracted_projects': unique_projects,
    'total_extracted': len(unique_projects),
    'funding_records': len(funding_data)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
