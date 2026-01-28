code = """import json

file1 = var_functions.query_db_6
file2 = var_functions.query_db_2

with open(file1) as f:
    funding = json.load(f)

with open(file2) as f:
    mongo = json.load(f)

funding_over_50k = []
for rec in funding:
    if rec['Amount'] > 50000:
        funding_over_50k.append(rec['Project_Name'])

design_projects = []
for doc in mongo:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_section = False
    for line in lines:
        line = line.strip()
        if '(Design)' in line:
            in_section = True
        elif '(Construction)' in line or '(Not Started)' in line:
            in_section = False
        elif in_section and line and not line.startswith('(') and not line.startswith('•'):
            if len(line) > 5 and 'Updates:' not in line and 'Schedule:' not in line:
                design_projects.append(line)

matches = 0
for f in funding_over_50k:
    for d in design_projects:
        if f.lower() in d.lower() or d.lower() in f.lower():
            matches += 1
            break

answer = json.dumps(matches)
print('__RESULT__:', answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
