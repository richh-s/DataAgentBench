code = """import json
import re

# Access the stored data
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

# Load JSON data
with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    docs = json.load(f)

# Build funding lookup map
funding_lookup = {}
for rec in funding:
    name = rec['Project_Name'].strip().lower()
    funding_lookup[name] = int(rec['Amount'])

# Find design projects
design_projects = []
for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    if design_marker in text:
        start = text.index(design_marker)
        end = text.find(construction_marker, start)
        if end == -1:
            end = len(text)
        
        section = text[start:end]
        lines = section.split('\n')
        
        # Extract project names
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and len(line) > 5:
                # Skip control lines
                if '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                    if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                        # Check context
                        if i + 1 < len(lines):
                            next_line = lines[i+1].strip()
                            if 'Updates:' in next_line or 'Project Schedule:' in next_line:
                                design_projects.append(line.lower())

# Count unique projects with funding > $50000
unique_projects = set(design_projects)
count = 0
for proj in unique_projects:
    if proj in funding_lookup and funding_lookup[proj] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
