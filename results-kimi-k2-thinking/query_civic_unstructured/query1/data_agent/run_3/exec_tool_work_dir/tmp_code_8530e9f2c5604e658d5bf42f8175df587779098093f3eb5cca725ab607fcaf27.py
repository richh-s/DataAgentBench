code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find capital projects with design status from civic documents
design_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif in_design_section:
            if line.startswith('Capital Improvement') or line.startswith('DISASTER'):
                in_design_section = False
            elif line and len(line) > 5 and not line.startswith('\u') and not line.startswith('-'):
                if 'Project' in line or (line[0].isupper() and any(c.isalpha() for c in line)):
                    design_project_names.add(line)

# Filter capital projects (remove potential disaster/FEMA projects)
capital_design_projects = set()
for name in design_project_names:
    lower_name = name.lower()
    if 'fema' not in lower_name and 'disaster' not in lower_name:
        capital_design_projects.add(name)

# Match with funding data > $50,000
matched_projects = []

for funding in funding_data:
    project_name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    if amount <= 50000:
        continue
    
    # Check various matching approaches
    if project_name in capital_design_projects:
        matched_projects.append(project_name)
    else:
        # Remove parenthetical suffixes
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
        if base_name in capital_design_projects:
            matched_projects.append(base_name)

# Get unique projects
capital_design_with_funding = set(matched_projects)
final_count = len(capital_design_with_funding)

result = {
    'count': final_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
