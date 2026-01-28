code = """import json

# Load the data
funding_path = var_functions.query_db_6
mongo_path = var_functions.query_db_2

with open(funding_path) as f:
    funding = json.load(f)

with open(mongo_path) as f:
    mongo_docs = json.load(f)

# Basic summary
funding_count = len(funding)
mongo_count = len(mongo_docs)

funding_over_50k = [f for f in funding if f['Amount'] > 50000]
funding_names = [f['Project_Name'] for f in funding_over_50k]

# Extract projects from mongo
all_design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        lines = text.split('\n')
        in_design = False
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects (Design)' in line:
                in_design = True
            elif '(Construction)' in line or '(Not Started)' in line:
                in_design = False
            elif in_design and line:
                # Skip non-project lines
                skip_words = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'Consultant', 'Staff', 'City', 'Project is', 'Plans are']
                if not any(w in line for w in skip_words) and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
                    all_design_projects.append(line)

# Find matches
matches = 0
for design_project in all_design_projects:
    for funding_name in funding_names:
        if funding_name.lower() in design_project.lower():
            matches += 1
            break

result = {'total_matches': matches, 'funding_over_50k': len(funding_names), 'design_projects': len(all_design_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
