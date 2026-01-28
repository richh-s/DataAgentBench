code = """import json
import re

# First, let's load the funding data
funding_data = globals()['var_functions.query_db:8']

# If it's a string (file path), load it from file
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        all_funding = json.load(f)
else:
    all_funding = funding_data

print('Total funding records:', len(all_funding))

# Create a dictionary for quick lookup by project name
funding_dict = {}
for record in all_funding:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[name] = funding_dict.get(name, 0) + amount

print('Unique projects with funding:', len(funding_dict))
print('\nSample funding entries:')
for name, amount in list(funding_dict.items())[:5]:
    print(f'  {name}: ${amount:,}')

# Now look for disaster-related projects from civic documents
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'recovery']

# From the preview, I can see project names like:
# Latigo Canyon Road Retaining Wall Repair Project
# (mentions: Awaiting final FEMA/CalOES approval)
# Clover Heights Storm Drainage Improvements (submitted to CalOES)
# Outdoor Warning Signs (emergency warning)

potential_disaster_projects = []

# Let's check which funded projects match disaster patterns
for name in funding_dict.keys():
    base_name = name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (FEMA/CalOES Project)', '')
    
    # Check if it's a disaster project by keyword in name
    if any(keyword in name for keyword in disaster_keywords):
        potential_disaster_projects.append({
            'Project_Name': name,
            'Base_Name': base_name,
            'Amount': funding_dict[name]
        })

print('\nPotential disaster projects found:', len(potential_disaster_projects))
print('\nFirst 10 projects:')
for proj in potential_disaster_projects[:10]:
    print(f"  {proj['Project_Name']}: ${proj['Amount']:,}")

# Group by base name to see duplicates
disaster_by_base = {}
for proj in potential_disaster_projects:
    base = proj['Base_Name']
    if base not in disaster_by_base:
        disaster_by_base[base] = []
    disaster_by_base[base].append(proj)

print('\nProjects with multiple funding entries:')
for base, projects in disaster_by_base.items():
    if len(projects) > 1:
        print(f"  {base}: {len(projects)} entries, total ${sum(p['Amount'] for p in projects):,}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
