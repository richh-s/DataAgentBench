code = """import json

# Load results
marie_canyon = locals()['var_functions.query_db:80']
broad_beach = locals()['var_functions.query_db:82']
bluffs_park = locals()['var_functions.query_db:84']

print('Marie Canyon funding:', marie_canyon)
print('Broad Beach funding:', broad_beach)
print('Bluffs Park funding:', bluffs_park)

# Calculate totals
spring_2022_projects = [
    "Marie Canyon Green Streets",
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)",
    "Bluffs Park Shade Structure"
]

# Sum all funding for Broad Beach related projects
total_funding = 0
funding_breakdown = {}

for record in marie_canyon:
    amount = int(record['Amount'])
    total_funding += amount
    funding_breakdown['Marie Canyon Green Streets'] = amount

for record in broad_beach:
    amount = int(record['Amount'])
    total_funding += amount
    funding_breakdown['Broad Beach Road Water Quality Infrastructure Repairs'] = funding_breakdown.get('Broad Beach Road Water Quality Infrastructure Repairs', 0) + amount

for record in bluffs_park:
    amount = int(record['Amount'])
    total_funding += amount
    funding_breakdown['Bluffs Park Shade Structure'] = amount

print('\nProjects starting Spring 2022:')
for proj in spring_2022_projects:
    print('- ' + proj)

print('\nTotal funding: $' + str(total_funding))
print('Project count: ' + str(len(spring_2022_projects)))

result = {
    'count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': spring_2022_projects,
    'funding_breakdown': funding_breakdown
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.list_db:72': ['civic_docs'], 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:80': [{'Funding_ID': '61', 'Project_Name': 'Marie Canyon Green Streets', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '50000'}], 'var_functions.query_db:82': [{'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}], 'var_functions.query_db:84': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}]}

exec(code, env_args)
