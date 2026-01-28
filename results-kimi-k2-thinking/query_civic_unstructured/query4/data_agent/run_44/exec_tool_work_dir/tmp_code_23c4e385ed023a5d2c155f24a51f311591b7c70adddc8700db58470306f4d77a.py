code = """import json

# Load funding data
funding_data = locals()['var_functions.query_db:10']

# Projects that started in Spring 2022 based on document analysis
spring_2022_projects = [
    "Marie Canyon Green Streets",
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)",
    "Bluffs Park Shade Structure"
]

print('Projects starting construction in Spring 2022:')
for proj in spring_2022_projects:
    print('- ' + proj)

# Lookup funding for these projects
total_funding = 0
project_funding = {}

for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Match project names
    if 'Marie Canyon' in project_name and 'Green Streets' in project_name:
        project_funding['Marie Canyon Green Streets'] = project_funding.get('Marie Canyon Green Streets', 0) + amount
        total_funding += amount
    elif 'Broad Beach Road' in project_name and 'Water Quality' in project_name:
        project_funding['Broad Beach Road Water Quality Infrastructure Repairs'] = amount
        total_funding += amount
    elif 'Bluffs Park Shade Structure' in project_name:
        project_funding['Bluffs Park Shade Structure'] = amount
        total_funding += amount

print('\nFunding amounts:')
for proj, funding in project_funding.items():
    print('- ' + proj + ': $' + str(funding))

print('\nTotal funding for Spring 2022 projects: $' + str(total_funding))

result_json = json.dumps({
    'project_count': len(spring_2022_projects),
    'projects': spring_2022_projects,
    'total_funding': total_funding,
    'funding_details': project_funding
})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.list_db:72': ['civic_docs'], 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
