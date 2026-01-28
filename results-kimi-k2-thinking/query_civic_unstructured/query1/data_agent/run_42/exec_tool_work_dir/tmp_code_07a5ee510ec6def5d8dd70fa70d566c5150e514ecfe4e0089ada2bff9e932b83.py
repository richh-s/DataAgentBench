code = """import json

# Load funding data
with open('var_functions.query_db_6') as f:
    funding = json.load(f)

# Load mongo data  
with open('var_functions.query_db_2') as f:
    mongo = json.load(f)

# Projects with funding > $50,000
funding_names = []
for rec in funding:
    if rec['Amount'] > 50000:
        funding_names.append(rec['Project_Name'])

# Extract design projects from mongo
design_names = []
for doc in mongo:
    text = doc.get('text', '')
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1].split('Capital Improvement Projects (Construction)')[0]
        for line in design_section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('•'):
                if len(line) > 5 and 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                    if not any(word in line for word in ['Consultant', 'Staff', 'City', 'Project']):
                        if not line.isupper():
                            design_names.append(line)

# Count matching projects
matches = 0
for f_name in funding_names:
    for d_name in design_names:
        if f_name.lower() in d_name.lower() or d_name.lower() in f_name.lower():
            matches += 1
            break

result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
