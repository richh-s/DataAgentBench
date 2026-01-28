code = """import json
import os

# Get the data from storage
funding_result = var_functions.query_db_8
civic_docs_result = var_functions.query_db_10

# Load funding data
if isinstance(funding_result, str) and os.path.exists(funding_result):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic documents
if isinstance(civic_docs_result, str) and os.path.exists(civic_docs_result):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

print('Funding records count: ' + str(len(funding_data)))
print('Civic documents count: ' + str(len(civic_docs)))

# Debug: show first few funding records
print('\nFirst 3 funding records:')
for i in range(min(3, len(funding_data))):
    print('  ' + str(funding_data[i]))

print('\nFirst civic document excerpt (first 200 chars):')
if civic_docs:
    print('  ' + civic_docs[0]['text'][:200])

# Now let's extract project information from civic documents
# We'll look for park projects completed in 2022

completed_park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lower_text = text.lower()
    
    # Look for park references, completion status, and 2022
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        # Split into lines to analyze per-line
        lines = text.split('\n')
        for line in lines:
            lower_line = line.lower()
            if 'park' in lower_line and 'completed' in lower_line and '2022' in lower_line:
                completed_park_projects_2022.append(line.strip())

print('\nLines mentioning park projects completed in 2022:')
print('Total found: ' + str(len(completed_park_projects_2022)))
for item in completed_park_projects_2022[:10]:
    print('  - ' + item)

# Let's also extract park-related project names from funding data
park_funding = [item for item in funding_data if 'park' in item['Project_Name'].lower()]
print('\nPark-related projects in funding data: ' + str(len(park_funding)))

# Display these projects
for proj in park_funding:
    print('  ' + proj['Project_Name'] + ': $' + str(proj['Amount']))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
