code = """import json

# The funding data is stored in var_functions.query_db:8
# Let's extract it properly
funding_result = var_functions.query_db:8

# Check what type it is and load accordingly
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        all_funding = json.load(f)
else:
    all_funding = funding_result

print(f"Number of funding records: {len(all_funding)}")

# Look for disaster-related projects based on naming patterns
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

print(f"\nFound {len(disaster_projects)} potential disaster-related projects")
print("\nFirst 10 disaster projects:")
for proj in disaster_projects[:10]:
    print(f"  {proj['Project_Name']}: ${proj['Amount']:,}")

# Let's also check unique patterns
disaster_patterns = {}
for proj in disaster_projects:
    name = proj['Project_Name']
    if '(FEMA Project)' in name:
        disaster_patterns['FEMA Project'] = disaster_patterns.get('FEMA Project', 0) + 1
    elif '(CalOES Project)' in name:
        disaster_patterns['CalOES Project'] = disaster_patterns.get('CalOES Project', 0) + 1
    elif '(CalJPIA Project)' in name:
        disaster_patterns['CalJPIA Project'] = disaster_patterns.get('CalJPIA Project', 0) + 1
    elif '(FEMA/CalOES Project)' in name:
        disaster_patterns['FEMA/CalOES Project'] = disaster_patterns.get('FEMA/CalOES Project', 0) + 1

print(f"\nDisaster project patterns: {disaster_patterns}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
