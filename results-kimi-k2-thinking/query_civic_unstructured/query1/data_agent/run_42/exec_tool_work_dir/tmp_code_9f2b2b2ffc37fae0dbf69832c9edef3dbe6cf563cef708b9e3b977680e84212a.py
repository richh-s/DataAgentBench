code = """import json

funding = json.load(open(var_functions.query_db_6))
mongo = json.load(open(var_functions.query_db_2))

# Get funding > 50k
funding_names = [f['Project_Name'] for f in funding if f['Amount'] > 50000]

# Extract design projects from mongo text
design_projects = []
for doc in mongo:
    text = doc.get('text', '')
    if '(Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            # Look for project names (lines that are project names)
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(') and not line.startswith('•'):
                    if len(line) > 5 and 'Updates:' not in line and 'Schedule:' not in line:
                        if 'Consultant' not in line and 'Staff' not in line:
                            if not line.isupper():
                                design_projects.append(line)

print('Funding projects >50k:', len(funding_names))
print('Design projects in mongo:', len(design_projects))

matches = 0
for f in funding_names:
    for d in design_projects:
        if f.lower() in d.lower() or d.lower() in f.lower():
            matches += 1
            break

__RESULT__:
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
