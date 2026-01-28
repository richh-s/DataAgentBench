code = """import json

# Load funding data
funding = []
with open(var_functions.query_db_6) as f:
    funding = json.load(f)

# Load mongo data
mongo = []
with open(var_functions.query_db_2) as f:
    mongo = json.load(f)

# Get project names with funding > 50000
funding_names = [f['Project_Name'] for f in funding if f['Amount'] > 50000]

# Extract design projects from mongo
design_projects = []
for doc in mongo:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif '(Construction)' in line or '(Not Started)' in line:
            in_design = False
        elif in_design and line and not line.startswith('(') and not line.startswith('•'):
            if len(line) > 5 and 'Updates:' not in line and 'Schedule:' not in line:
                if 'Consultant' not in line and 'Staff' not in line and 'Project' not in line[:20]:
                    if line and not line.isupper():
                        design_projects.append(line)

# Find matching projects
matches = []
for design_name in design_projects:
    for funding_name in funding_names:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches.append(funding_name)
            break

result = len(matches)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
