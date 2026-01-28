code = """import json, re

# Get the civic documents from storage
civic_docs_path = locals()['var_functions.query_db:100']
funding_path = locals()['var_functions.query_db:101']

# Read the data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded files successfully')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        # Check for completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for project name nearby
            for j in range(max(0, i-5), min(len(lines), i+5)):
                context = lines[j].strip()
                if context and 'park' in context.lower() and len(context) > 5:
                    # Clean the project name
                    clean = context.replace('•', '').replace('◦', '').strip()
                    # Skip lines that are clearly not project names
                    if clean and 'Update' not in clean and 'Schedule' not in clean and not clean.startswith('('):
                        if clean.lower() not in [p.lower() for p in park_projects]:
                            park_projects.append(clean)
                            print('Found:', clean)

print('\nTotal unique park projects found:', len(park_projects))

# Calculate total funding
total_funding = 0
for park in park_projects:
    park_key = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_key in fund_key or fund_key in park_key:
            total_funding += int(fund['Amount'])
            print('Matched:', park, '->', fund['Project_Name'], '= $', fund['Amount'])
            break

print('\nTotal funding:', total_funding)

result = {'total_funding_dollars': total_funding, 'project_count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:85': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.query_db:97': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:101': 'file_storage/functions.query_db:101.json'}

exec(code, env_args)
