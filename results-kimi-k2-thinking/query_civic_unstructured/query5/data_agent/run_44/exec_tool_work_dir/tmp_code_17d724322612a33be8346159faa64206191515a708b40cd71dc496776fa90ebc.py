code = """import json
import os
import sys

# Get all variables that might contain funding data
funding_data = []
for var_name, var_value in list(globals().items()):
    var_str = str(var_name)
    if 'query_db' in var_str and 'funding' in var_str.lower():
        try:
            if isinstance(var_value, str) and os.path.exists(var_value):
                with open(var_value, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list) and len(data) > 0:
                        funding_data = data
                        print('Loaded funding data from', var_name, 'with', len(data), 'records')
                        break
        except:
            pass

if not funding_data:
    print('ERROR: Could not load funding data')
    sys.exit(1)

# Now analyze the funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'recovery']

# Find projects that are disaster-related AND have 2022 in their name
# The 2022 in the name likely indicates they started in 2022
disaster_projects_2022 = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster project and started in 2022
    is_disaster = any(keyword in project_name for keyword in disaster_keywords)
    is_2022_start = '2022' in project_name
    
    if is_disaster and is_2022_start:
        # Use base name for grouping
        base_name = project_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']:
            base_name = base_name.replace(suffix, '')
        
        disaster_projects_2022[base_name] = disaster_projects_2022.get(base_name, 0) + amount

total_funding = sum(disaster_projects_2022.values())
num_projects = len(disaster_projects_2022)

print('Found', num_projects, 'disaster projects that started in 2022')
print('Total funding: $', total_funding)
print('\nProjects:')
for name in sorted(disaster_projects_2022.keys()):
    print(' -', name, ': $', disaster_projects_2022[name])

# Save result
result = {
    'total_funding': total_funding,
    'project_count': num_projects,
    'projects': disaster_projects_2022
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
