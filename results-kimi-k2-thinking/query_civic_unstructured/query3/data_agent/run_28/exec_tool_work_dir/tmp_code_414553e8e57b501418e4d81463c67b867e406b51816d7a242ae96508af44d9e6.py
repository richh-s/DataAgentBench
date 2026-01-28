code = """import json
import pandas as pd
import re

# Load funding data from the file path stored in the variable
funding_file_path = '/tmp/tool_query_result_funding_database_query_db.json'

try:
    with open(funding_file_path, 'r') as f:
        funding_records = json.load(f)
except FileNotFoundError:
    print(f"File not found at {funding_file_path}")
    # Try to find the actual file
    import os
    files = os.listdir('/tmp')
    print("Files in /tmp:")
    for f in files:
        print(f)
    # Exit if can't find file
    raise

print(f"Loaded {len(funding_records)} funding records")

# Show a few sample records
print("\nSample funding records:")
for i, record in enumerate(funding_records[:5]):
    print(f"{i+1}. {record}")

# Filter for FEMA or emergency-related projects in funding data
fema_funding_projects = []
emergency_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia']

for record in funding_records:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check if any emergency keyword appears in project name or funding source
    if any(keyword in project_name or keyword in funding_source for keyword in emergency_keywords):
        fema_funding_projects.append(record)

print(f"\nFound {len(fema_funding_projects)} FEMA/emergency-related projects in funding table")
print("\nFirst 10 matching projects:")
for proj in fema_funding_projects[:10]:
    print(f"- {proj['Project_Name']} | {proj['Funding_Source']} | ${proj['Amount']}")"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
