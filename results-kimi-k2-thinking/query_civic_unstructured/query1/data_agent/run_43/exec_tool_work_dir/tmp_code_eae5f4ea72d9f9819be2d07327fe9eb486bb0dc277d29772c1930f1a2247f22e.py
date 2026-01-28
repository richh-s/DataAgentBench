code = """import json

# Load data files
funding_data = json.load(open(var_functions.query_db:5))
civic_docs = json.load(open(var_functions.query_db:6))

# Map: project name -> funding amount
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Find design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 9 and not line.startswith('Page'):
                if 'design' in text[max(0, text.find(line)):text.find(line)+400].lower():
                    design_projects.add(line.replace('•', '').strip())

# Count matches with funding > 50000
count = 0
for proj in design_projects:
    for funded_name in funding_map:
        if funding_map[funded_name] > 50000:
            proj_lower = proj.lower()
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                if abs(len(proj) - len(funded_name)) < 35:
                    count += 1
                    break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
