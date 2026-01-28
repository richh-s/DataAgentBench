code = """import json

# Load funding data from path stored in previous query
funding_result = var_functions.query_db_6
mongo_result = var_functions.query_db_2

with open(funding_result) as f:
    funding_data = json.load(f)

with open(mongo_result) as f:
    mongo_docs = json.load(f)

# Get all projects with funding > $50,000
projects_over_50k = {}
for record in funding_data:
    amt = int(record['Amount'])
    if amt > 50000:
        projects_over_50k[record['Project_Name']] = record

# Extract design projects from mongo documents
design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design_section = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design_section = False
        elif in_design_section and clean and not clean.startswith('(') and not clean.startswith('•'):
            if len(clean) > 5 and 'Updates:' not in clean and 'Schedule:' not in clean:
                if 'Consultant' not in clean and 'Staff' not in clean and 'Project' not in clean[:15]:
                    if not clean.isupper():
                        design_projects.append(clean)

# Count matching projects
matches = []
for design_name in design_projects:
    for funding_name in projects_over_50k:
        design_lower = design_name.lower()
        funding_lower = funding_name.lower()
        if funding_lower in design_lower or design_lower in funding_lower:
            if funding_name not in matches:
                matches.append(funding_name)
                break

result = len(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
