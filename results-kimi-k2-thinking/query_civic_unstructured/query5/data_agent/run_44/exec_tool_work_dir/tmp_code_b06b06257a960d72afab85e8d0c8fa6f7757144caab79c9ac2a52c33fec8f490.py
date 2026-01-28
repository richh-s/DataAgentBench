code = """import json

# Load the funding data
funding_path = var_functions.query_db_14 if hasattr(__import__('builtins'), 'var_functions') else var_functions.query_db_14
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Funding records loaded:', len(funding_records))
print('First record:', funding_records[0])

# Identify disaster-related projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']

disaster_projects = []
for rec in funding_records:
    project_name = rec.get('Project_Name', '')
    if any(keyword in project_name for keyword in disaster_keywords):
        disaster_projects.append({
            'name': project_name,
            'amount': int(rec.get('Amount', 0))
        })

print('\nDisaster projects found:', len(disaster_projects))

# Sum by base name (remove disaster suffixes)
base_totals = {}
for proj in disaster_projects:
    base_name = proj['name']
    for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']:
        base_name = base_name.replace(suffix, '')
    
    base_totals[base_name] = base_totals.get(base_name, 0) + proj['amount']

print('Unique disaster projects:', len(base_totals))
print('Total disaster funding (all years): $', sum(base_totals.values()))

# Look for projects with 2022 in their name (potential 2022 starts)
projects_with_2022 = {name: amount for name, amount in base_totals.items() if '2022' in name}
print('\nProjects with 2022 in name:', len(projects_with_2022))
for name, amount in projects_with_2022.items():
    print(' -', name, ': $', amount)

print('\nTotal for projects with 2022 in name: $', sum(projects_with_2022.values()))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
