code = """import json

# Load funding data
with open(var_functions.query_db_6) as f:
    funding = json.load(f)

# Load mongo data  
with open(var_functions.query_db_2) as f:
    mongo = json.load(f)

# Get projects with funding over 50000
funding_names = []
for record in funding:
    if record['Amount'] > 50000:
        funding_names.append(record['Project_Name'])

# Extract design projects from mongo
design_names = []
for doc in mongo:
    text = doc['text']
    lines = text.split('\n')
    in_section = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_section = True
        elif '(Construction)' in line or '(Not Started)' in line:
            in_section = False
        elif in_section and line.strip() and not line.strip().startswith('(') and not line.strip().startswith('•'):
            clean = line.strip()
            if len(clean) > 5 and 'Updates:' not in clean and 'Schedule:' not in clean and 'Page' not in clean and not clean.isupper():
                design_names.append(clean)

# Count matches
count = 0
for funding_project in funding_names:
    for design_project in design_names:
        if funding_project.lower() in design_project.lower() or design_project.lower() in funding_project.lower():
            count += 1
            break

__RESULT__ = str(count)
print('__RESULT__:')
print(__RESULT__)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
