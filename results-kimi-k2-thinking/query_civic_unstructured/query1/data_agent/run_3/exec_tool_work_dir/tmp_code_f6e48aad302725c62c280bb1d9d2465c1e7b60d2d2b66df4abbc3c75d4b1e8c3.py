code = """import json
import re

# Load data from files
with open(locals()['var_functions.query_db:2'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects by scanning for project titles in design section
project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif in_design and ('Capital Improvement Projects (Construction)' in line or 'Disaster Recovery' in line):
            break
        elif in_design:
            clean_line = line.strip()
            if (clean_line and len(clean_line) > 8 and 'Project' in clean_line and 
                'Updates' not in clean_line and 'Schedule' not in clean_line):
                project_names.add(clean_line)

# Filter out FEMA/disaster projects
capital_design = set()
for name in project_names:
    lower = name.lower()
    if 'fema' not in lower and 'disaster' not in lower:
        capital_design.add(name)

# Match with funding > 50000
found = set()

for record in funding_data:
    amount = int(record['Amount'])
    if amount <= 50000:
        continue
    
    full_name = record['Project_Name']
    # Remove suffix
    base = re.sub(r'\s*\([^)]*\)$', '', full_name)
    
    if base in capital_design:
        found.add(base)

result = {'count': len(found)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
