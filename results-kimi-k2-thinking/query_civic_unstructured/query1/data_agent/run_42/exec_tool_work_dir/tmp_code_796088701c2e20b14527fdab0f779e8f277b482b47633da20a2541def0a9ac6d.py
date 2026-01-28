code = """import json

# Load data from the file paths stored in previous results
with open(var_functions.query_db_6) as f:
    funding_data = json.load(f)

with open(var_functions.query_db_2) as f:
    mongo_data = json.load(f)

# Get project names with funding > $50,000
names_over_50k = [r['Project_Name'] for r in funding_data if r['Amount'] > 50000]

# Extract projects with design status from mongo
design_projects = []
for doc in mongo_data:
    sections = doc.get('text', '').split('Capital Improvement Projects (Design)')
    if len(sections) > 1:
        # Take first part after Design header until next section
        design_section = sections[1].split('Capital Improvement Projects (Construction)')[0].split('Capital Improvement Projects (Not Started)')[0]
        
        for line in design_section.split('\n'):
            clean = line.strip()
            if not clean: continue
            if clean.startswith('(') or clean.startswith('•'): continue
            if 'Updates:' in clean or 'Schedule:' in clean: continue
            if 'Consultant' in clean or 'Staff' in clean or 'Project' in clean[:15]: continue
            if len(clean) > 5 and not clean.isupper():
                design_projects.append(clean)

# Count matches
count = 0
matched = []
for name in names_over_50k:
    for design in design_projects:
        if name.lower() in design.lower() or design.lower() in name.lower():
            count += 1
            matched.append(name)
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
