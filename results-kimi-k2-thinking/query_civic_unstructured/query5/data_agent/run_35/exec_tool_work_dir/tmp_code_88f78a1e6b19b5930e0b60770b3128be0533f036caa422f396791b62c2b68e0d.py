code = """import json
import re

# Load funding data
funding_file = '/tmp/tmpj4_6s1y9.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print("Total funding records loaded:", len(funding_data))

# Identify disaster-related funding records
disaster_funding_records = []
for record in funding_data:
    proj_name = record['Project_Name'].upper()
    if 'FEMA' in proj_name or 'CALOES' in proj_name or 'CALJPIA' in proj_name:
        disaster_funding_records.append(record)

print("Disaster funding records:", len(disaster_funding_records))

# Create a lookup dictionary: project name -> amount
disaster_funding_lookup = {}
for record in disaster_funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    disaster_funding_lookup[name] = amount

print("\nDisaster projects with funding:")
for name, amount in list(disaster_funding_lookup.items())[:10]:
    print("-", name, ": $", amount)

print("... and", len(disaster_funding_lookup) - 10, "more")

result1 = {
    'funding_lookup': disaster_funding_lookup,
    'count': len(disaster_funding_lookup)
}

print('\n__RESULT__:')
print(json.dumps(result1))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
