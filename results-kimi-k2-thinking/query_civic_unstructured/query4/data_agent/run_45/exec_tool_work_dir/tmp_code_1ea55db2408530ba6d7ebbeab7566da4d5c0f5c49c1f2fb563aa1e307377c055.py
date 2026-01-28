code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:90']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Projects with 2022 in their names (indicating they started/were slated for 2022)
year_2022_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if '2022' in name and amount > 0:
        year_2022_projects.append({'name': name, 'amount': amount})

# Calculate totals
total_projects = len(year_2022_projects)
total_funding = sum(p['amount'] for p in year_2022_projects)

print('2022 projects from funding data:', total_projects)
print('Total funding:', total_funding)

for p in year_2022_projects:
    print(f"- {p['name']}: ${p['amount']:,}")

result = {
    'project_count': total_projects,
    'total_funding': total_funding,
    'projects': year_2022_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}], 'var_functions.list_db:82': ['civic_docs'], 'var_functions.list_db:84': ['civic_docs'], 'var_functions.query_db:86': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:96': [{'total_funding': 'None'}]}

exec(code, env_args)
