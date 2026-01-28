code = """import json

# Load both data sources
with open(var_functions.query_db_6) as f:
    funding = json.load(f)

with open(var_functions.query_db_2) as f:
    mongo_docs = json.load(f)

# Extract funding > 50k
funding_over_50k = {}
for rec in funding:
    if rec['Amount'] > 50000:
        funding_over_50k[rec['Project_Name']] = rec

# Extract design projects from mongo
projects_with_design_status = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    for line in lines:
        clean = line.strip()
        if '(Design)' in clean:
            in_design = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design = False
        elif in_design and clean and not clean.startswith('(') and not clean.startswith('•'):
            if len(clean) > 5 and 'Updates:' not in clean and 'Schedule:' not in clean:
                if not any(word in clean for word in ['Consultant', 'Staff', 'City', 'Project']):
                    projects_with_design_status.append(clean)

# Find projects in both lists
matching_count = 0
matched_names = []

for design_project in projects_with_design_status:
    for funding_name in funding_over_50k:
        # Case-insensitive partial matching
        if funding_name.lower() in design_project.lower() or design_project.lower() in funding_name.lower():
            matching_count += 1
            matched_names.append(funding_name)
            break

result = {'count': matching_count, 'sample_matches': matched_names[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
