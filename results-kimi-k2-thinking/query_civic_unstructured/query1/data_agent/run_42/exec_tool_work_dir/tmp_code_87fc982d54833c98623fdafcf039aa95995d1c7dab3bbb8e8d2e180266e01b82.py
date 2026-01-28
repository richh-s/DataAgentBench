code = """import json

funding_path = var_functions.query_db_6
mongo_path = var_functions.query_db_2

with open(funding_path) as f:
    funding_data = json.load(f)

with open(mongo_path) as f:
    mongo_docs = json.load(f)

funding_over_50k = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_over_50k.append(f['Project_Name'])

design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if '(Design)' in text:
        lines = text.split('\n')
        in_design = False
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects (Design)' in line:
                in_design = True
            elif '(Construction)' in line or '(Not Started)' in line:
                in_design = False
            elif in_design and line and not line.startswith('(') and not line.startswith('•'):
                skip_list = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION']
                if len(line) > 5 and not any(s in line for s in skip_list):
                    design_projects.append(line)

matches = 0
for d in design_projects:
    for f in funding_over_50k:
        if d.lower().find(f.lower()) >= 0 or f.lower().find(d.lower()) >= 0:
            matches = matches + 1
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
