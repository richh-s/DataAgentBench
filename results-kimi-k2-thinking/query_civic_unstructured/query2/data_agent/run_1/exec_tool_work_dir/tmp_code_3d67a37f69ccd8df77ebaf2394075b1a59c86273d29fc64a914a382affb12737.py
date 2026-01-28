code = """import json
import re

# Load funding data (this is small enough to be in memory)
funding_data = locals().get('var_functions.query_db:5')
if funding_data and isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Load civic documents data (stored in file)
civic_docs_file = locals().get('var_functions.query_db:8')
if civic_docs_file and isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = []

print(f"Number of civic documents: {len(civic_docs_data)}")
print(f"Number of funding records: {len(funding_data) if funding_data else 0}")

# Let's inspect the structure
if civic_docs_data:
    print(f"\nFirst document keys: {list(civic_docs_data[0].keys())}")
    print(f"First document filename: {civic_docs_data[0]['filename']}")
    # Print a snippet of the text
    print(f"\nText snippet: {civic_docs_data[0]['text'][:500]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
