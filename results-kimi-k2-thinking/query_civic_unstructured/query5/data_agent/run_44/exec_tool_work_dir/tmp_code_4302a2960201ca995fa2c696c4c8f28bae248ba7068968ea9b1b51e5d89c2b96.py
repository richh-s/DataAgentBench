code = """import json

# Load funding data from storage
funding_path = locals()['var_functions.query_db:8']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Identify disaster-related projects that started in 2022
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'recovery']
disaster_2022_totals = {}

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if disaster-related AND has 2022 (indicating start year)
    is_disaster = any(keyword in project_name for keyword in disaster_keywords)
    is_2022 = '2022' in project_name
    
    if is_disaster and is_2022:
        # Get clean base name by removing suffixes
        clean_name = project_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']:
            clean_name = clean_name.replace(suffix, '')
        
        disaster_2022_totals[clean_name] = disaster_2022_totals.get(clean_name, 0) + amount

total_funding = sum(disaster_2022_totals.values())
project_count = len(disaster_2022_totals)

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': project_count,
    'projects': disaster_2022_totals
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
