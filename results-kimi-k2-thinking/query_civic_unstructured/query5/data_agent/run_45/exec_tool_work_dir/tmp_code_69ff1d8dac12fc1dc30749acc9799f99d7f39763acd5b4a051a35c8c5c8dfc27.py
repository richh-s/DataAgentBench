code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:10
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records: {len(funding_data)}")

# Load civic docs data
civic_file = var_functions.query_db:12
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Step 1: Identify disaster-related project names from funding data
# These will be our target projects to match

disaster_keywords = ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster', 'Fire', 'Emergency', 'FEMA', 'CalOES', 'CalJPIA']
disaster_project_names = set()

disaster_projects_with_funding = []

for record in funding_data:
    project_name = record['Project_Name']
    # Check if this is a disaster-related project
    is_disaster = False
    for keyword in disaster_keywords:
        if keyword in project_name:
            is_disaster = True
            break
    
    if is_disaster:
        # Clean the name for matching (remove suffixes)
        clean_name = re.sub(r'\s*\(FEMA.*\)', '', project_name)
        clean_name = re.sub(r'\s*\(CalOES.*\)', '', clean_name)
        clean_name = re.sub(r'\s*\(CalJPIA.*\)', '', clean_name)
        clean_name = clean_name.strip()
        
        disaster_project_names.add(clean_name)
        disaster_project_names.add(project_name)  # Also add the original
        
        disaster_projects_with_funding.append({
            'Project_Name': project_name,
            'Clean_Name': clean_name,
            'Amount': int(record['Amount']),
            'Funding_Source': record.get('Funding_Source', '')
        })

print(f"Found {len(disaster_projects_with_funding)} disaster-related projects in funding data")
print(f"Unique project name variations: {len(disaster_project_names)}")

# Show some examples
for proj in disaster_projects_with_funding[:10]:
    print(f"  {proj['Project_Name']} -> {proj['Clean_Name']}: ${proj['Amount']:,}")

print('\n__RESULT__:')
print(json.dumps({
    'total_funding_records': len(funding_data),
    'disaster_projects_found': len(disaster_projects_with_funding),
    'unique_names': len(disaster_project_names)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
