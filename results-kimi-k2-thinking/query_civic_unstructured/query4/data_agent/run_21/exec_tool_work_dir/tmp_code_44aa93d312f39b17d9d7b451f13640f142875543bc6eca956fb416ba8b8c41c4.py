code = """import json

# Load funding records from file
funding_file = var_functions.query_db_84
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create lookup dictionary
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = amount

# List of projects that started in Spring 2022 (extracted from civic documents)
spring_2022_project_names = [
    'Marie Canyon Green Streets',
    'PCH Median Improvements Project',
    'PCH Signal Synchronization System Improvements Project',
    'Westward Beach Road Improvements Project',
    'Bluffs Park Shade Structure',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)',
    'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)'
]

# Match with funding and calculate totals
matched_projects = {}
for project_name in spring_2022_project_names:
    if project_name in funding_lookup:
        matched_projects[project_name] = funding_lookup[project_name]
    else:
        # Try to find similar projects (without suffixes in parentheses)
        base_name = project_name.split('(')[0].strip()
        for fund_name, amount in funding_lookup.items():
            fund_base_name = fund_name.split('(')[0].strip()
            if base_name == fund_base_name:
                matched_projects[fund_name] = amount
                break

total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in matched_projects.items()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
