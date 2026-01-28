code = """import json

# Get the data from storage
civic_docs = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

# Build funding lookup
funding_dict = {}
for item in funding:
    project_name = item['Project_Name'].lower().replace(' ', '')
    funding_dict[project_name] = int(item['Amount'])

# Based on the document text:
# - Bluffs Park Shade Structure was completed in November 2022
# - Broad Beach Road Water Quality Repair was completed in November 2022  
# - Point Dume Walkway Repairs was completed in November 2022

park_projects_2022 = ['Bluffs Park Shade Structure']

# Combine all document text
total_text = ''
for doc in civic_docs:
    total_text += doc.get('text', '') + '\n'

# Check which park projects were completed in 2022
if 'Bluffs Park Shade Structure' in total_text and '2022' in total_text:
    proj_key = 'bluffsparkshadestructure'
    amount = funding_dict.get(proj_key, 0)
else:
    amount = 0

print('__RESULT__:')
print(json.dumps({
    'total_funding': amount,
    'project_count': 1 if amount > 0 else 0,
    'projects': [{'project': 'Bluffs Park Shade Structure', 'amount': amount}] if amount > 0 else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
