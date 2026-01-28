code = """import json

# Load funding data
funding_result = var_functions.query_db:8
with open(funding_result, 'r') as f:
    all_funding = json.load(f)

print('Total records:', len(all_funding))

# Identify disaster projects
disaster_projects = []
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']

for rec in all_funding:
    name = rec.get('Project_Name', '')
    if any(k in name for k in keywords):
        disaster_projects.append({
            'name': name, 
            'amount': int(rec.get('Amount', 0)),
            'base': name.split(' (')[0]
        })

print('\nDisaster projects found:', len(disaster_projects))

# Group by base name and sum amounts
base_totals = {}
for proj in disaster_projects:
    base = proj['base']
    base_totals[base] = base_totals.get(base, 0) + proj['amount']

print('\nUnique disaster projects:', len(base_totals))
print('\nTotal disaster funding (all years):', sum(base_totals.values()))

# Show sample projects
print('\nFirst 10 projects:')
for i, (name, amount) in enumerate(list(base_totals.items())[:10]):
    print(i+1, name, ':', amount)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
