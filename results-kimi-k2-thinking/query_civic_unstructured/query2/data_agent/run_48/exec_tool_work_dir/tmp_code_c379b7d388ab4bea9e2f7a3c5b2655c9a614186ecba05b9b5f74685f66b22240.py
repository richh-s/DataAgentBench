code = """import json

# Get funding data directly from storage - it's already a list
funding_records = var_functions.query_db:0

print('Type of funding data:', type(funding_records))
print('Number of funding records:', len(funding_records))

# Show the first few funding records to understand structure
for i, record in enumerate(funding_records[:10]):
    print(f"Record {i}: {record}")

# Filter for park-related projects
park_project_funding = []
for fund in funding_records:
    proj_name = fund['Project_Name'].lower()
    if 'park' in proj_name or 'playground' in proj_name or 'walkway' in proj_name:
        park_project_funding.append({
            'Project_Name': fund['Project_Name'],
            'Amount': int(fund['Amount']),
            'Funding_Source': fund['Funding_Source']
        })

print('\nPark projects found in funding data:', len(park_project_funding))
for proj in park_project_funding:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']}")

# Calculate total funding for park projects
total_park_funding = sum(proj['Amount'] for proj in park_project_funding)

result = {
    'total_park_funding': total_park_funding,
    'park_projects': park_project_funding,
    'count': len(park_project_funding)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
