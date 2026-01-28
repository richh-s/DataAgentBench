code = """import json

# Load data
funding_data = json.load(open(var_functions.query_db:5))
civic_docs = json.load(open(var_functions.query_db:6))

# Map funding by project name
funding = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Extract design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 8 and 'Project' not in line and 'Schedule' not in line and 'Updates' not in line:
                if 'Design' in line or (line.istitle() and len(line) < 100):
                    design_projects.add(line)

# Count matches with funding > 50000
count = 0
details = []
for proj in design_projects:
    for funded_name in funding.keys():
        if funding[funded_name] > 50000:
            if proj.lower() in funded_name.lower() or funded_name.lower() in proj.lower():
                if abs(len(proj) - len(funded_name)) < 40:
                    count += 1
                    details.append([proj, funding[funded_name]])
                    break

print('__RESULT__:')
print(json.dumps({'count': count, 'projects': details[:20]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
