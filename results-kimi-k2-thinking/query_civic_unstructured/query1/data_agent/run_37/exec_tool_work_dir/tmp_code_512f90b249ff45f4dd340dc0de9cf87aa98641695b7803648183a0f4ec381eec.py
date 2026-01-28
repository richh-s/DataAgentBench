code = """import json
import re

# Load funding data
funding_path = var_functions.query_db_2
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = var_functions.query_db_5
with open(civic_path) as f:
    civic_docs = json.load(f)

print('Data loaded: %d funding records, %d civic docs' % (len(funding_data), len(civic_docs)))

# Step 1: Map projects with funding > $50,000
funded_projects = {}
for rec in funding_data:
    amt = int(rec['Amount'])
    if amt > 50000:
        funded_projects[rec['Project_Name']] = {
            'amount': amt,
            'source': rec['Funding_Source']
        }

print('Projects with >$50k funding: %d' % len(funded_projects))

# Step 2: Search for capital projects in design phase
combined_text = ''
for doc in civic_docs:
    combined_text += ' ' + doc['text']

text_lower = combined_text.lower()
matches = []

for project_name in funded_projects:
    # Check if project name appears in text
    if project_name.lower() in text_lower:
        # Find the section
        idx = text_lower.find(project_name.lower())
        snippet = text_lower[max(0, idx-300):idx+400]
        
        # Check for capital and design indicators
        if 'capital' in snippet and 'design' in snippet:
            matches.append({
                'name': project_name,
                'funding': funded_projects[project_name]['amount']
            })

print('Capital projects in design phase with >$50k funding: %d' % len(matches))
print('__RESULT__:')
print(json.dumps({'count': len(matches), 'projects': matches[:5]}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
