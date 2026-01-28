code = """import json

# Load funding data
with open(var_functions.query_db_6, 'r') as f:
    funding_data = json.load(f)

# Load mongo data  
with open(var_functions.query_db_2, 'r') as f:
    mongo_docs = json.load(f)

# Get project names with funding > $50,000
funding_names = []
for rec in funding_data:
    if rec['Amount'] > 50000:
        funding_names.append(rec['Project_Name'])

# Extract design projects from mongo documents
design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design_section = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design_section = False
        elif in_design_section and clean and len(clean) > 5:
            if 'Updates:' not in clean and 'Schedule:' not in clean and not clean.startswith('(') and not clean.startswith('•'):
                if not any(word in clean for word in ['Consultant', 'Staff', 'City', 'Project']):
                    if not clean.isupper():
                        design_projects.append(clean)

# Find matching projects
matches = 0
for fname in funding_names:
    found = False
    for dname in design_projects:
        if fname.lower() in dname.lower() or dname.lower() in fname.lower():
            found = True
            break
    if found:
        matches = matches + 1

# Print result
answer = json.dumps(matches)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
