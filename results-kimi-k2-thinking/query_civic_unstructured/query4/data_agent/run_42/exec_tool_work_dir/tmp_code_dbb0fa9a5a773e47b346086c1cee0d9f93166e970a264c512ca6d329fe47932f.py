code = """# Check what variables are available
available_vars = list(locals().keys())
print('Available variables:', available_vars)

# Try to read the data
mongo_file_path = locals()['var_functions.query_db:14']
funding_file_path = locals()['var_functions.query_db:4']

import json

# Read MongoDB data
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

# Read funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

print(f'Mongo docs: {len(mongo_docs)}')
print(f'Funding records: {len(funding_data)}')

# Look for Spring 2022 projects
projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text and 'Begin Construction' in text:
        # Extract project sections
        parts = text.split('\n\n')
        for part in parts:
            if 'Spring 2022' in part and 'Begin Construction' in part:
                lines = part.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('(') and len(line) > 10:
                        if 'Project' in line or 'Improvements' in line:
                            projects.append(line)

print('Projects:', projects[:10])

# Find funding for these projects
funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding_data}

matched = []
for proj in set(projects):
    if proj in funding_lookup:
        matched.append({'name': proj, 'funding': funding_lookup[proj]})

print('Matched with funding:', len(matched))
print(matched)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
