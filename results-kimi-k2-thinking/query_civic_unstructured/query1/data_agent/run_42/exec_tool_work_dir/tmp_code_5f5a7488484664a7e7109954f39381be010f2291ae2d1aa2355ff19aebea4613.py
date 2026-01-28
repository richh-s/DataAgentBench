code = """import json

# Load funding data
funding_file = var_functions.query_db_6
with open(funding_file) as f:
    funding = json.load(f)

# Load mongo data
mongo_file = var_functions.query_db_2
with open(mongo_file) as f:
    mongo = json.load(f)

# Get projects with funding > 50000
funding_names = [f['Project_Name'] for f in funding if f['Amount'] > 50000]

# Extract design projects from mongo
design_projects = []
for doc in mongo:
    text = doc.get('text', '')
    sections = text.split('\n\n')
    in_design_section = False
    for section in sections:
        lines = section.split('\n')
        for line in lines:
            clean = line.strip()
            if 'Capital Improvement Projects (Design)' in clean:
                in_design_section = True
            elif 'Capital Improvement Projects (Construction)' in clean or 'Capital Improvement Projects (Not Started)' in clean:
                in_design_section = False
            elif in_design_section and clean and not any(skip in clean for skip in ['Updates:', 'Schedule:', 'Consultant', 'Staff', 'Project', 'To:', 'Subject:', 'Page', 'RECOMMENDED']):
                if clean and not clean.startswith('(') and not clean.startswith('•') and len(clean) > 10 and not clean.isupper():
                    design_projects.append(clean)

# Find matches
matches = []
for design_proj in design_projects:
    for fund_name in funding_names:
        if fund_name.lower() in design_proj.lower() or design_proj.lower() in fund_name.lower():
            matches.append(design_proj)
            break

result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
