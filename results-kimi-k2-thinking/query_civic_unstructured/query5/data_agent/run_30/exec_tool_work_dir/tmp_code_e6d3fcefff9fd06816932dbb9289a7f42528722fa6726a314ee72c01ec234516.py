code = """import json

# Load full funding data
funding_file = locals()['var_functions.query_db:10']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Look specifically for projects with 2022 in the name that are disaster-related
disaster_keywords = ['fema', 'caloes', 'caljpia', 'emergency', 'fire', 'disaster', 'siren']
disaster_2022_projects = []
total_amount = 0

for funding in funding_records:
    project_name = funding.get('Project_Name', '')
    amount = float(funding.get('Amount', 0))
    
    name_lower = project_name.lower()
    has_2022 = '2022' in project_name
    is_disaster = any(keyword in name_lower for keyword in disaster_keywords)
    
    if has_2022 and is_disaster:
        disaster_2022_projects.append({
            'name': project_name,
            'amount': amount
        })
        total_amount += amount

# Also check for any projects that start with 2022 and might be disaster-related
for funding in funding_records:
    project_name = funding.get('Project_Name', '')
    amount = float(funding.get('Amount', 0))
    
    name_lower = project_name.lower()
    
    if project_name.startswith('2022'):
        # Look for infrastructure/disaster related keywords
        if any(keyword in name_lower for keyword in ['storm', 'drain', 'emergency', 'resurfacing', 'road', 'repair']):
            disaster_2022_projects.append({
                'name': project_name,
                'amount': amount
            })
            total_amount += amount

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_amount,
    'project_list': disaster_2022_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:22': {'total_funding': 0, 'record_count': 0}}

exec(code, env_args)
