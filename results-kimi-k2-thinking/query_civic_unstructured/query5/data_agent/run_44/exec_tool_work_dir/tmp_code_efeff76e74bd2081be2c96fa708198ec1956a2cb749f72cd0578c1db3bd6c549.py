code = """import json
import os

# Load funding data - try to find the file manually
funding_data = None

# Get all json files in /tmp
tmp_files = [f for f in os.listdir('/tmp') if f.endswith('.json')]
print('JSON files in /tmp:', tmp_files)

for file in tmp_files:
    try:
        file_path = os.path.join('/tmp', file)
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                # Check if this looks like funding data
                if isinstance(data[0], dict) and 'Project_Name' in data[0]:
                    funding_data = data
                    print('Loaded funding data from', file_path)
                    break
    except Exception as e:
        continue

if not funding_data:
    print('Failed to load funding data')
    exit()

print('Total records:', len(funding_data))

# Identify disaster projects that started in 2022
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']
disaster_2022_projects = {}

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster-related AND has 2022 (indicating start year)
    is_disaster = any(keyword in project_name for keyword in disaster_keywords)
    has_2022 = '2022' in project_name
    
    if is_disaster and has_2022:
        # Clean up the name
        clean_name = project_name.split(' (')[0]
        disaster_2022_projects[clean_name] = disaster_2022_projects.get(clean_name, 0) + amount

total_funding = sum(disaster_2022_projects.values())
project_count = len(disaster_2022_projects)

# Print results
for name, amount in sorted(disaster_2022_projects.items()):
    print(name, ':', amount)

print('\nTotal funding for 2022 disaster projects:', total_funding)
print('Number of projects:', project_count)

# Export result
result = {
    'total_funding': total_funding,
    'project_count': project_count,
    'projects': disaster_2022_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
