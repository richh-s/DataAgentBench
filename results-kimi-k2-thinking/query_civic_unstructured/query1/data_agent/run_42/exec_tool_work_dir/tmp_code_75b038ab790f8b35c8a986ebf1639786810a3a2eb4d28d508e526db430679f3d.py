code = """import json

# Load funding data
with open(var_functions.query_db_6) as f:
    funding_data = json.load(f)

# Load mongo data  
with open(var_functions.query_db_2) as f:
    mongo_data = json.load(f)

print('Funding records:', len(funding_data))
print('Mongo documents:', len(mongo_data))

# Count funding > 50000
count_50k = 0
project_names_50k = []
for record in funding_data:
    if record['Amount'] > 50000:
        count_50k += 1
        project_names_50k.append(record['Project_Name'])

print('Funding > 50k:', count_50k)
print('Sample projects:', project_names_50k[:5])

# Extract design projects
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    if '(Design)' in text:
        lines = text.split('\n')
        in_design = False
        for line in lines:
            clean = line.strip()
            if '(Design)' in clean:
                in_design = True
            elif '(Construction)' in clean or '(Not Started)' in clean:
                in_design = False
            elif in_design and clean and not clean.startswith('(') and not clean.startswith('•'):
                if 'Updates:' not in clean and len(clean) > 5:
                    design_projects.append(clean)

print('Design projects:', len(design_projects))
print('Sample:', design_projects[:5])

# Simple matching
match_count = 0
for name in project_names_50k:
    for design in design_projects:
        if name.lower() in design.lower() or design.lower() in name.lower():
            match_count += 1
            break

print('Matches:', match_count)

__RESULT__:
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
