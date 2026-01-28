code = """import json
import os

# Get data from storage using correct keys
funding_result = var_functions.query_db_8
civic_result = var_functions.query_db_10

# Load funding data
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic documents  
if isinstance(civic_result, str):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# From document analysis: Bluffs Park Shade Structure completed November 2022
# Let's verify and calculate

completed_park_projects = []

# Check for Bluffs Park Shade Structure
for item in funding_data:
    if item['Project_Name'] == 'Bluffs Park Shade Structure':
        completed_park_projects.append({
            'name': item['Project_Name'],
            'amount': int(item['Amount'])
        })
        break

# Calculate total funding
total_funding = sum(p['amount'] for p in completed_park_projects)

# Return result in required format
print('__RESULT__:')
print(json.dumps({
    'total_funding_2022': total_funding,
    'projects': completed_park_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
