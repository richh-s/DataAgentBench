code = """import json

# Load funding data
funding_file = open(var_functions.query_db_6, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load mongo data
mongo_file = open(var_functions.query_db_2, 'r')
mongo_data = json.load(mongo_file)
mongo_file.close()

# Get project names with funding > $50,000
funding_names = []
for rec in funding_data:
    if rec['Amount'] > 50000:
        funding_names.append(rec['Project_Name'])

# Extract design projects from mongo
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    if '(Design)' in text:
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        design_section = design_section.split('Capital Improvement Projects (Construction)')[0]
        for line in design_section.split('\n'):
            clean = line.strip()
            if clean and not clean.startswith('(') and 'Updates:' not in clean:
                if len(clean) > 5 and 'Consultant' not in clean and not clean.isupper():
                    design_projects.append(clean)

# Count matches
matches = 0
for funding_name in funding_names:
    for design_name in design_projects:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches += 1
            break

final_answer = json.dumps(matches)
print('__RESULT__:')
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
