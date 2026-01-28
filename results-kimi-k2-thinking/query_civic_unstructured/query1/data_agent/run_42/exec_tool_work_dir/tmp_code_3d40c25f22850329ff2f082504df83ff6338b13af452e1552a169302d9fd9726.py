code = """import json

# Load funding data
funding_path = var_functions.query_db_6
with open(funding_path) as f:
    funding_data = json.load(f)

# Load mongo data
mongo_path = var_functions.query_db_2
with open(mongo_path) as f:
    mongo_data = json.load(f)

# Get projects with funding > 50000
funding_projects = []
for f in funding_data:
    if f['Amount'] > 50000:
        funding_projects.append(f['Project_Name'])

# Extract design status projects from mongo
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    if '(Design)' in text:
        lines = text.split('\n')
        in_design = False
        for line in lines:
            line = line.strip()
            if '(Design)' in line:
                in_design = True
            elif '(Construction)' in line or '(Not Started)' in line:
                in_design = False
            elif in_design and line and not line.startswith('(') and not line.startswith('•'):
                if len(line) > 5 and 'Updates:' not in line:
                    design_projects.append(line)

# Count matches
matches = 0
match_list = []
for funding_name in funding_projects:
    for design_name in design_projects:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches += 1
            match_list.append(funding_name)
            break

# Output
print('Funding projects > $50k:', len(funding_projects))
print('Design projects found:', len(design_projects))
print('Matching projects:', matches)
__RESULT__:
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
