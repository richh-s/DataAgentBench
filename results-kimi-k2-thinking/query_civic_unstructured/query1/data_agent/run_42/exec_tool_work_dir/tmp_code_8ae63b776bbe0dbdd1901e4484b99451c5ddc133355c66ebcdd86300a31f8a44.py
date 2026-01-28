code = """import json

# Load funding data
with open(var_functions.query_db_6) as f:
    funding_data = json.load(f)

# Count projects with funding > 50000
count_funding_over_50k = 0
project_names_over_50k = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        count_funding_over_50k += 1
        project_names_over_50k.append(f['Project_Name'])

print('Funding > 50k count:', count_funding_over_50k)

# Load mongo data
with open(var_functions.query_db_2) as f:
    mongo_data = json.load(f)

# Extract design projects
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        clean_line = line.strip()
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
        elif '(Construction)' in clean_line or '(Not Started)' in clean_line:
            in_design_section = False
        elif in_design_section and clean_line:
            if not clean_line.startswith('(') and not clean_line.startswith('•'):
                skip_pattern = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION', 'Consultant', 'Staff is', 'Staff will', 'City is', 'Project is']
                if not any(pattern in clean_line for pattern in skip_pattern):
                    if len(clean_line) > 5 and not clean_line.isupper():
                        design_projects.append(clean_line.strip('•- '))

print('Design projects found:', len(design_projects))

# Find matches
matches = []
for funding_project in project_names_over_50k:
    for design_project in design_projects:
        if funding_project.lower() in design_project.lower() or design_project.lower() in funding_project.lower():
            matches.append(funding_project)
            break

print('Final count of matching projects:', len(matches))

__RESULT__:
print(json.dumps(len(matches)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
