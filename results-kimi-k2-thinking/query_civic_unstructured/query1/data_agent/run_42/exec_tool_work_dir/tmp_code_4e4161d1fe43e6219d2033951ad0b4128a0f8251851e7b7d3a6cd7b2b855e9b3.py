code = """import json

# Load the data files
funding_file = var_functions.query_db_6
mongo_file = var_functions.query_db_2

with open(funding_file) as f:
    funding_records = json.load(f)

with open(mongo_file) as f:
    mongo_docs = json.load(f)

# Get funding projects > $50k
funding_list = [f['Project_Name'] for f in funding_records if f['Amount'] > 50000]

# Get design projects from mongo
projects_in_design = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\\n')
    in_design = False
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif '(Construction)' in line or '(Not Started)' in line:
            in_design = False
        elif in_design:
            if line and not line.startswith('(') and not line.startswith('•'):
                if 'Updates:' not in line and 'Schedule:' not in line and 'Consultant' not in line:
                    if len(line) > 5 and not line.isupper():
                        projects_in_design.append(line)

# Count matches
matching = 0
for f in funding_list:
    for d in projects_in_design:
        if f.lower() in d.lower():
            matching += 1
            break

__RESULT__:
print(json.dumps(matching))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
