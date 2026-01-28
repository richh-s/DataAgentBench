code = """import json
import re

# Load data from correct file paths
funding_file = open('file_storage/functions.query_db:46/result.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

civic_file = open('file_storage/functions.query_db:5/result.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

print('Data loaded:', len(funding_data), 'funding records,', len(civic_docs), 'civic docs')

# Step 1: Create lookup of high-funded projects
funded_lookup = {}
for rec in funding_data:
    amt = int(rec['Amount'])
    if amt > 50000:
        funded_lookup[rec['Project_Name'].lower()] = rec

print('High-funded projects:', len(funded_lookup))

# Step 2: Search for capital design projects
matches = []
all_text = ''
for doc in civic_docs:
    all_text += doc['text']

for project_name in funded_lookup:
    if project_name in all_text.lower():
        idx = all_text.lower().find(project_name)
        context = all_text.lower()[max(0, idx-200):idx+400]
        if 'capital' in context and 'design' in context:
            matches.append(funded_lookup[project_name]['Project_Name'])

# Remove duplicates
unique_matches = list(set(matches))
print('Capital design projects with >$50k funding:', len(unique_matches))

result = {'count': len(unique_matches), 'projects': unique_matches[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
