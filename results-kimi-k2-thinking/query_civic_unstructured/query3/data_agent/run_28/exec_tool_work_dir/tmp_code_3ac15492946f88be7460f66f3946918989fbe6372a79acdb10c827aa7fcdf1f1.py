code = """import json

# Load the funding data file
with open('/mnt/data/funding_data.json', 'r') as f:
    funding_data = json.load(f)

# Filter for projects related to 'emergency' or 'FEMA'
# Looking for projects with FEMA in the name or funding source, or emergency-related terms
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check if project is FEMA-related
    if ('fema' in project_name or 
        'emergency' in project_name or
        'fema' in funding_source or
        'emergency' in funding_source or
        'disaster' in project_name):
        fema_projects.append(record)

print(f"Found {len(fema_projects)} FEMA/emergency-related projects in funding data")
print("\nFirst 10 matching projects:")
for proj in fema_projects[:10]:
    print(f"- {proj['Project_Name']} | {proj['Funding_Source']} | ${proj['Amount']}")"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
