code = """import json

# Load funding data
funding_result = globals()['var_functions.query_db:8']

# Check if it's a file path or direct data
if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        all_funding = json.load(f)
else:
    all_funding = funding_result

print('Number of funding records:', len(all_funding))

# Look for disaster-related projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']
disaster_projects = []

for record in all_funding:
    project_name = record.get('Project_Name', '')
    if any(keyword in project_name for keyword in disaster_keywords):
        disaster_projects.append({
            'Project_Name': project_name,
            'Amount': int(record.get('Amount', 0)),
            'Funding_Source': record.get('Funding_Source', '')
        })

print('\nFound', len(disaster_projects), 'potential disaster-related projects')

# Count patterns
disaster_patterns = {}
total_disaster_funding = 0

for proj in disaster_projects:
    name = proj['Project_Name']
    amount = proj['Amount']
    total_disaster_funding += amount
    
    if '(FEMA Project)' in name:
        disaster_patterns['FEMA Project'] = disaster_patterns.get('FEMA Project', 0) + 1
    elif '(CalOES Project)' in name:
        disaster_patterns['CalOES Project'] = disaster_patterns.get('CalOES Project', 0) + 1
    elif '(CalJPIA Project)' in name:
        disaster_patterns['CalJPIA Project'] = disaster_patterns.get('CalJPIA Project', 0) + 1
    elif '(FEMA/CalOES Project)' in name:
        disaster_patterns['FEMA/CalOES Project'] = disaster_patterns.get('FEMA/CalOES Project', 0) + 1

print('Disaster project patterns:', disaster_patterns)
print('Total disaster funding (all years):', total_disaster_funding)

# Extract base project names to look for in civic documents
disaster_base_names = []
for proj in disaster_projects:
    name = proj['Project_Name']
    # Remove disaster suffixes to get base name
    base_name = name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (FEMA/CalOES Project)', '')
    disaster_base_names.append(base_name)

print('\nFirst 10 base names:', disaster_base_names[:10])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
