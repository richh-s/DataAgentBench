code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Based on document review, park projects completed in 2022 include:
# - Bluffs Park Shade Structure (completed November 2022)
# Let's search funding table for park-related projects

park_projects_funding = []
for record in funding_records:
    project_name = record['Project_Name'].lower()
    if 'park' in project_name:
        amount = int(record['Amount'])
        park_projects_funding.append({
            'project_name': record['Project_Name'],
            'amount': amount
        })

# Filter for projects completed in 2022 based on civic documents
# From the documents we identified:
# Bluffs Park Shade Structure - completed November 2022
projects_completed_2022 = [
    'Bluffs Park Shade Structure',
]

# Match with funding amounts
total_funding = 0
matched_projects = []

for project in projects_completed_2022:
    for fund in park_projects_funding:
        if project.lower() in fund['project_name'].lower():
            total_funding += fund['amount']
            matched_projects.append({
                'project': project,
                'funding_name': fund['project_name'],
                'amount': fund['amount']
            })

print('__RESULT__:')
print(json.dumps({
    'matched_projects': matched_projects,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
