code = """import json
import re
import os

# Get the data
funding_data = locals().get('var_functions.query_db:5')
civic_data = locals().get('var_functions.query_db:8')

# Load funding data
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding = json.load(f)
elif isinstance(funding_data, list):
    funding = funding_data
else:
    funding = []

# Load civic docs data
if isinstance(civic_data, str) and civic_data.endswith('.json'):
    with open(civic_data, 'r') as f:
        civic_docs = json.load(f)
elif isinstance(civic_data, list):
    civic_docs = civic_data
else:
    civic_docs = []

print('Funding records count:', len(funding))
print('Civic documents count:', len(civic_docs))

if funding:
    print('First funding record:', funding[0])
if civic_docs:
    print('First civic doc filename:', civic_docs[0].get('filename'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
