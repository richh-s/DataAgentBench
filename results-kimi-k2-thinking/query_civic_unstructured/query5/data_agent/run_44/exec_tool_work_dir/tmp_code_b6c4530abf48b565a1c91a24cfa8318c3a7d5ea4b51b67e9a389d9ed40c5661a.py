code = """import json
import os
import sys

def load_json_from_var(var_value):
    if isinstance(var_value, str) and os.path.exists(var_value):
        with open(var_value, 'r') as f:
            return json.load(f)
    elif isinstance(var_value, list):
        return var_value
    return []

# Load funding data - try different variable names
funding_data = []
for var_name in ['var_functions.query_db:8', 'var_functions.query_db:14']:
    if var_name in globals():
        data = load_json_from_var(globals()[var_name])
        if data:
            funding_data = data
            print('Loaded funding data from', var_name)
            break

if not funding_data:
    print('Failed to load funding data')
    sys.exit(0)

print('Total funding records:', len(funding_data))

# Identify disaster-related projects and sum their funding
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'recovery']
disaster_by_base = {}

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster-related
    if any(keyword in project_name for keyword in disaster_keywords):
        # Remove disaster suffixes to get base name
        base_name = project_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']:
            base_name = base_name.replace(suffix, '')
        
        disaster_by_base[base_name] = disaster_by_base.get(base_name, 0) + amount

print('\nTotal disaster projects (unique):', len(disaster_by_base))
print('Total disaster funding (all years): $', sum(disaster_by_base.values()))

# Identify projects that started in 2022
# Strategy: Look for 2022 in project name OR extract from civic docs
projects_2022 = {}

for base_name, amount in disaster_by_base.items():
    if '2022' in base_name:
        projects_2022[base_name] = amount

print('\nProjects with 2022 in name:', len(projects_2022))
for name in sorted(projects_2022.keys()):
    print(' -', name, ': $', projects_2022[name])

total_2022_funding = sum(projects_2022.values())
print('\nTotal 2022 disaster funding: $', total_2022_funding)

output = {
    'total_2022_disaster_funding': total_2022_funding,
    'num_2022_projects': len(projects_2022),
    'projects_2022': projects_2022
}

print('\n__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
