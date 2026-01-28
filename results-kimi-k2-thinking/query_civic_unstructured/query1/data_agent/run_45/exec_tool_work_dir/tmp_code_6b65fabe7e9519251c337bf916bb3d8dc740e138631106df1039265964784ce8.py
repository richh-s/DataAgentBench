code = """import json, re

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:6

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_data = json.load(f)

funding_projects = {}
for item in funding_data:
    amount = float(item['Amount'])
    if amount > 50000:
        name = item['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_projects[name] = amount
        funding_projects[clean_name] = amount

design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    design_section = False
    
    for line in text.split('\n'):
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            design_section = False
        
        if design_section and line and len(line) > 10:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                if all(x not in line.upper() for x in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                    if all(x not in line for x in ['Updates:', 'Schedule:', 'Capital Improvement Projects']):
                        design_projects.append(line)

matches = 0
for project in design_projects:
    project_clean = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    if project in funding_projects or project_clean in funding_projects:
        matches += 1

print('__RESULT__:')
print(json.dumps({'count': matches}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
