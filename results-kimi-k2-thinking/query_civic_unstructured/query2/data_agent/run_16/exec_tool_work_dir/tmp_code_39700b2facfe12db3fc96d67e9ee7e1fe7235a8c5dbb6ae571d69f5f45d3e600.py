code = """import json
import os

# Load funding data
funding_path = var_functions.query_db_8
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path

# Load civic documents  
civic_path = var_functions.query_db_10
if isinstance(civic_path, str):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Get all park-related project names from funding data
park_names = []
for item in funding_data:
    if 'park' in item['Project_Name'].lower():
        park_names.append(item['Project_Name'])

print('Park projects in funding:', len(park_names))

# Search for completed park projects in 2022 within civic documents
completed_parks_2022 = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for line in lines:
        low = line.lower()
        if 'park' in low and 'completed' in low and '2022' in low:
            completed_parks_2022.append(line.strip())

print('Completed park refs in 2022:', len(completed_parks_2022))
for ref in completed_parks_2022:
    print(' -', ref)

# Based on the document preview, we saw these specific projects:
# - Bluffs Park Shade Structure - completed November 2022
# - Broad Beach Road Water Quality Repair - completed November 2022  
# - Point Dume Walkway Repairs - completed November 2022
# Let's check if these are park projects

specific_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

print('\nChecking specific projects:')
for proj in specific_projects:
    for item in funding_data:
        if proj.lower() in item['Project_Name'].lower():
            print('Found:', item['Project_Name'], '- $' + item['Amount'])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
