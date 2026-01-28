code = """import json

# Load all funding data
funding_file = '/tmp/tmpv2h8j5z2.json'
with open(funding_file, 'r') as f:
    all_funding = json.load(f)

print('Total funding records:', len(all_funding))

# Identify disaster-related projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']
disaster_funding = {}

disaster_projects = []
for record in all_funding:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if this is a disaster project
    is_disaster = any(keyword in project_name for keyword in disaster_keywords)
    
    if is_disaster:
        disaster_projects.append({
            'name': project_name,
            'amount': amount
        })
        
        # Group by base name (remove disaster suffixes)
        base_name = project_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (FEMA/CalOES Project)', '')
        disaster_funding[base_name] = disaster_funding.get(base_name, 0) + amount

print('\nDisaster projects found:', len(disaster_projects))
print('Unique disaster projects (base names):', len(disaster_funding))
print('Total disaster funding (all years): $', sum(disaster_funding.values()))

# Look for projects with 2022 in the name (indicating 2022 start)
projects_2022 = []
for name, amount in disaster_funding.items():
    if '2022' in name:
        projects_2022.append({'name': name, 'amount': amount})

print('\nProjects with 2022 in name:', len(projects_2022))
for proj in projects_2022:
    print(' -', proj['name'], ': $', proj['amount'])

total_2022 = sum(p['amount'] for p in projects_2022)
print('\nTotal funding for 2022 disaster projects (by name): $', total_2022)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
