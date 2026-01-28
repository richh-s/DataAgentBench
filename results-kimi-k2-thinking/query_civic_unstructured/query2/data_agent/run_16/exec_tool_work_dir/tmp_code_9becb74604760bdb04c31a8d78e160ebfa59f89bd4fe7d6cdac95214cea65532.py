code = """import json
import os

# Load funding data
funding_path = var_functions.query_db_8
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path

# Based on the document analysis, projects completed in 2022 include:
# - Bluffs Park Shade Structure (completed November 2022)
# Let's find the funding for park projects completed in 2022

# First, get all park-related projects from funding data
park_projects = []
for item in funding_data:
    if 'park' in item['Project_Name'].lower():
        park_projects.append(item)

print('Found park projects:', len(park_projects))

# Based on the document excerpt, these specific projects were completed in November 2022:
# - Bluffs Park Shade Structure
# - Broad Beach Road Water Quality Repair  
# - Point Dume Walkway Repairs

# Of these, only Bluffs Park Shade Structure is clearly park-related

# Check for Bluffs Park Shade Structure in funding data
total_funding = 0
bluffs_park = None

for item in funding_data:
    if item['Project_Name'] == 'Bluffs Park Shade Structure':
        bluffs_park = item
        total_funding += int(item['Amount'])
        break

result = {
    'total_funding': total_funding,
    'projects_found': []
}

if bluffs_park:
    result['projects_found'].append({
        'name': bluffs_park['Project_Name'],
        'amount': bluffs_park['Amount']
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
