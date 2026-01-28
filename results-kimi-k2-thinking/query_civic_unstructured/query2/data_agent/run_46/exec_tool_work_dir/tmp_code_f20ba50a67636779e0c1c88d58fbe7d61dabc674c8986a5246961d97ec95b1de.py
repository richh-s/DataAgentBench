code = """import json
import re

# Load data from storage variables
civic_docs = locals()['var_functions.query_db:8']
funding_records = locals()['var_functions.query_db:10']

# Create funding lookup table
funding_lookup = {}
for record in funding_records:
    normalized_name = record['Project_Name'].lower().replace(' ', '')
    funding_lookup[normalized_name] = int(record['Amount'])

# Identify park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text_content = doc.get('text', '')
    # Search for Bluffs Park Shade Structure specifically mentioned as completed November 2022
    if 'Bluffs Park Shade Structure' in text_content and 'completed' in text_content.lower() and '2022' in text_content:
        park_projects.append('Bluffs Park Shade Structure')

# Calculate total funding
total_amount = 0
matched_projects = []

for project_name in park_projects:
    normalized_key = project_name.lower().replace(' ', '')
    if normalized_key in funding_lookup:
        project_funding = funding_lookup[normalized_key]
        total_amount += project_funding
        matched_projects.append({'project': project_name, 'amount': project_funding})

# Output result
output = {'total_funding': total_amount, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs']}

exec(code, env_args)
