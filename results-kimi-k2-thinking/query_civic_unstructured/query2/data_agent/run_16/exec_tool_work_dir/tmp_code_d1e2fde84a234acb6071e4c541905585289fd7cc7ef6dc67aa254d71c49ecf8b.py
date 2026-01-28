code = """import json

# Read the funding data from the file
with open('results/query_db_8.json', 'r') as f:
    funding_data = json.load(f)

# Read the civic documents from the file
with open('results/query_db_10.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Let's examine the structure of the documents
if civic_docs:
    print(f"\nFirst document keys: {list(civic_docs[0].keys())}")
    print(f"First document excerpt: {civic_docs[0]['text'][:500]}")

# Let's also look at some park-related project names from funding data
park_projects = [item for item in funding_data if 'park' in item['Project_Name'].lower()]
print(f"\nFound {len(park_projects)} park-related projects in funding data:")
for proj in park_projects[:10]:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
