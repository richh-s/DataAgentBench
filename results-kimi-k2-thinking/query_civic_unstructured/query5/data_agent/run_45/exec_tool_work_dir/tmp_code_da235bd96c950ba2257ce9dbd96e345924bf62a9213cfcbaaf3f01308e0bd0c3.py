code = """import json
import re

# Load funding data from the file
funding_file = var_functions.query_db:10
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data from the file  
civic_file = var_functions.query_db:12
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Find all disaster-related projects in funding data
disaster_keywords = ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster', 'Fire', 'Emergency']
disaster_projects_funding = []

for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    
    is_disaster = False
    for keyword in disaster_keywords:
        if keyword in project_name:
            is_disaster = True
            break
    
    if is_disaster:
        disaster_projects_funding.append({
            'Project_Name': project_name,
            'Amount': amount
        })

# Step 2: Create a mapping from base names to disaster projects for matching
base_name_map = {}
for proj in disaster_projects_funding:
    name = proj['Project_Name']
    base_name = re.sub(r'\s*\(FEMA.*\)', '', name)
    base_name = re.sub(r'\s*\(CalOES.*\)', '', base_name)
    base_name = re.sub(r'\s*\(CalJPIA.*\)', '', base_name)
    base_name = base_name.strip()
    
    if base_name not in base_name_map:
        base_name_map[base_name] = []
    base_name_map[base_name].append(name)

# Summary statistics
total_disaster_funding = sum(p['Amount'] for p in disaster_projects_funding)

# Simple JSON output for the interface
result = {
    'total_funding_records': len(funding_data),
    'disaster_projects_found': len(disaster_projects_funding),
    'total_disaster_funding': total_disaster_funding,
    'unique_base_names': len(base_name_map)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}

exec(code, env_args)
