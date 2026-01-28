code = """import json

# Load the data from file paths
with open('var_functions.query_db_6') as f:
    funding = json.load(f)

with open('var_functions.query_db_2') as f:
    mongo = json.load(f)

# Get projects with funding > 50000
funding_names = [f['Project_Name'] for f in funding if f['Amount'] > 50000]

# Extract design projects
design_projects = []
for doc in mongo:
    if '(Design)' in doc.get('text', ''):
        text = doc['text']
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('(Construction)')[0]
            for line in design_section.split('\n'):
                clean = line.strip()
                if clean and not clean.startswith('(') and not clean.startswith('•'):
                    if len(clean) > 5 and 'Updates:' not in clean and 'Schedule:' not in clean:
                        if 'Consultant' not in clean and 'Staff' not in clean:
                            design_projects.append(clean)

# Count matches
count = 0
for f in funding_names:
    for d in design_projects:
        if f.lower() in d.lower():
            count += 1
            break

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
