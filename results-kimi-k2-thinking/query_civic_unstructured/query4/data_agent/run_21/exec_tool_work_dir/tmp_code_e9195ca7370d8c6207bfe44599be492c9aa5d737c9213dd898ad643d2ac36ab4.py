code = """import json
import re

# Load funding data
funding_key = "var_functions.query_db:12"
funding_result = locals()[funding_key]

if isinstance(funding_result, str) and ".json" in funding_result:
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Load civic docs data
civic_key = "var_functions.query_db:2"
civic_result = locals()[civic_key]

if isinstance(civic_result, str) and ".json" in civic_result:
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print("Data loaded successfully")
print(f"Funding records: {len(funding_records)}")
print(f"Civic documents: {len(civic_docs)}")

# Extract project names from funding for quick lookup
funding_project_names = {record['Project_Name'].lower().strip() for record in funding_records}
print(f"Unique funding project names: {len(funding_project_names)}")

# Show a few funding project names
sample_names = list(funding_project_names)[:10]
print("Sample funding project names:")
for name in sample_names:
    print(f"  - {name}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records'}

exec(code, env_args)
