code = """import json

# Read the MongoDB result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

print('Loaded documents:', len(civic_docs_data))

# Extract design projects
projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design_section = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design_section = False
        elif in_design_section and clean and not clean.startswith('(') and not clean.startswith('•'):
            if all(x not in clean for x in ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'Approved by:', 'Date prepared:', 'RECOMMENDED ACTION', 'DISCUSSION']):
                if not any(word in clean for word in ['Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 'City has', 'Project is', 'Plans are', 'Bids are', 'Construction']):
                    if len(clean) > 5 and not clean.isupper():
                        projects.append({'name': clean.strip('•- '), 'status': 'design', 'type': 'capital'})
print('Found projects:', len(projects))
for p in projects[:10]:
    print(' -', p['name'])

result = json.dumps(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
