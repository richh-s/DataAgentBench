code = """import json

# Load data
f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:3']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_data = json.load(f)

# Create lookup for funding amounts
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].upper().strip()
    value = int(item['Amount'])
    funding_lookup[key] = value

# Known park projects completed in 2022 based on document preview
projects_to_check = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs',
    'Marie Canyon Green Streets'
]

# Filter park projects and match with funding
valid_projects = [p for p in projects_to_check if 'park' in p.lower()]

total_amount = 0
matched_list = []

for project in valid_projects:
    proj_key = project.upper()
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_amount += amount
        matched_list.append({'project': project, 'funding': amount})

result = {
    'total_funding_2022_park_completed': total_amount,
    'project_count': len(matched_list),
    'details': matched_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
