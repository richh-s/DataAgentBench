code = """import json
import os

# Try different ways to get funding data
funding_data = None

# Method 1: Check for file in common tmp location
for root, dirs, files in os.walk('/tmp'):
    for file in files:
        if file.endswith('.json') and 'funding' in file.lower():
            try:
                with open(os.path.join(root, file), 'r') as f:
                    funding_data = json.load(f)
                    print('Found funding file:', os.path.join(root, file))
                    break
            except:
                pass
    if funding_data:
        break

if not funding_data:
    # Method 2: Try to load from the most recent query result
    try:
        # Check all variables that might contain the data
        for var_name, var_value in list(globals().items()):
            if isinstance(var_value, str) and var_value.endswith('.json'):
                try:
                    with open(var_value, 'r') as f:
                        funding_data = json.load(f)
                        print('Loaded from variable:', var_name)
                        break
                except:
                    pass
    except:
        pass

if not funding_data:
    print('Could not load funding data')
    exit()

print('Total records:', len(funding_data))

# Identify disaster projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'recovery']
disaster_base_totals = {}

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster-related
    is_disaster = any(keyword in project_name for keyword in disaster_keywords)
    
    if is_disaster:
        # Get base name by removing disaster suffixes
        base_name = project_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)', ' (CalOES Project)']:
            base_name = base_name.replace(suffix, '')
        
        disaster_base_totals[base_name] = disaster_base_totals.get(base_name, 0) + amount

print('\nUnique disaster projects:', len(disaster_base_totals))
print('Total disaster funding (all years): $', sum(disaster_base_totals.values()))

# Projects that started in 2022 (identified by name or date patterns)
projects_2022 = {}
for base_name, total_amount in disaster_base_totals.items():
    # Check if 2022 appears in the project name or could be start year
    if '2022' in base_name:
        projects_2022[base_name] = total_amount
    # Also check for specific patterns that indicate 2022 start
    elif any(x in base_name for x in ['Annual 2022', '2022 Annual', 'Morning View 2022']):
        projects_2022[base_name] = total_amount

print('\nProjects with 2022 in name:', len(projects_2022))
for name, amount in projects_2022.items():
    print(' -', name, ': $', amount)

print('\nTotal 2022 disaster funding (from names): $', sum(projects_2022.values()))

# Save for later use
disaster_data = {
    'all_disaster_projects': disaster_base_totals,
    'disaster_projects_2022': projects_2022,
    'total_2022': sum(projects_2022.values())
}

print('\n__RESULT__:')
print(json.dumps(disaster_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
