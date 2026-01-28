code = """import json
import os

# The results are stored as variables. Let's see what we have
print("Available variables:", [k for k in dir() if k.startswith('var_functions')])

# Access the funding data
funding_path = 'var_functions.query_db:2'
civic_path = 'var_functions.query_db:0'

# Load the data from the file paths if they exist, otherwise use the variables directly
if os.path.exists(funding_path):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:2']

if os.path.exists(civic_path):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:0']

print(f"Funding data: {len(funding_data)} records")
print(f"Civic docs: {len(civic_docs)} documents")

# Step 1: Find all emergency/FEMA related projects in funding data
emergency_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_funding.append(record)

print(f"\nFound {len(emergency_funding)} emergency/FEMA projects in funding database:")
for proj in emergency_funding:
    print(f"- {proj['Project_Name']}: ${proj['Amount']} from {proj['Funding_Source']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
