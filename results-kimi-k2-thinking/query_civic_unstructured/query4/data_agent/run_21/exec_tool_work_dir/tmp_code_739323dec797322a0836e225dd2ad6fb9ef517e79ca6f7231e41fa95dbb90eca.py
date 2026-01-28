code = """import json
import re

# Load funding records from the file
funding_file = var_functions.query_db_84
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup
def get_funding(project_name_substring):
    """Find funding amount for a project containing the given substring"""
    for record in funding_records:
        if project_name_substring.lower() in record['Project_Name'].lower():
            return int(record['Amount'])
    return 0

# Projects identified from civic documents that started in Spring 2022
spring_2022_projects = {
    'Marie Canyon Green Streets': get_funding('Marie Canyon Green Streets'),
    'PCH Median Improvements Project': get_funding('PCH Median Improvements'),
    'PCH Signal Synchronization System Improvements Project': get_funding('PCH Signal Synchronization'),
    'Westward Beach Road Improvements Project': get_funding('Westward Beach Road'),
    'Bluffs Park Shade Structure': get_funding('Bluffs Park Shade Structure'),
    'Permanent Skate Park': get_funding('Permanent Skate Park'),
    'PCH at Trancas Canyon Road Right Turn Lane': get_funding('Trancas Canyon Road Right Turn Lane'),
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)': get_funding('Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'),
    'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)': get_funding('Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)')
}

# Filter out projects with zero funding
matched_projects = {name: amount for name, amount in spring_2022_projects.items() if amount > 0}

total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Spring 2022 Projects:', total_projects)
print('Total Funding: $' + str(total_funding))
print('\\nProject Details:')
for project, funding in matched_projects.items():
    print(f'- {project}: ${funding:,}')

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'project_details': matched_projects
}

print('\\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
