code = """import json

funding_file = var_functions.query_db_6
mongo_file = var_functions.query_db_2

with open(funding_file) as f:
    funding_data = json.load(f)

with open(mongo_file) as f:
    mongo_data = json.load(f)

funding_names = []
for f in funding_data:
    if f['Amount'] > 50000:
        funding_names.append(f['Project_Name'])

projects_in_design = []
for doc in mongo_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    lines = text.split('\n')
    in_design = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
            continue
        if '(Construction)' in line or '(Not Started)' in line:
            in_design = False
            continue
        if in_design:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith('(') and not clean_line.startswith('•'):
                skip_terms = ['Updates:', 'Schedule:', 'Consultant', 'Staff', 'Project', 'To:', 'Subject:', 'Page']
                should_skip = False
                for term in skip_terms:
                    if term in clean_line:
                        should_skip = True
                        break
                if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                    projects_in_design.append(clean_line)

matches = 0
for funding_name in funding_names:
    for design_name in projects_in_design:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches = matches + 1
            break

__RESULT__:
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
