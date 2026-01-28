code = """import json, re

# Load funding data using the exact key provided
funding_data_path = locals()['var_functions.query_db:12']

# Check if it's a file path or already loaded data
if isinstance(funding_data_path, str) and '.json' in funding_data_path:
    with open(funding_data_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data_path

print(f"Funding records loaded: {len(funding_records)}")

# Load civic docs data using the exact key provided
civic_data_path = locals()['var_functions.query_db:2']

# Check if it's a file path or already loaded data
if isinstance(civic_data_path, str) and '.json' in civic_data_path:
    with open(civic_data_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data_path

print(f"Civic docs loaded: {len(civic_docs)}")

# Show first document structure to understand format
print(f"First doc keys: {list(civic_docs[0].keys())}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records'}

exec(code, env_args)
