code = """import json

# Load funding data from file
funding_path = '/tmp/tmpj4_6s1y9.json'
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Funding records loaded:', len(funding_records))

# Identify disaster-related projects in funding database
disaster_funding = {}
for record in funding_records:
    project_name = record['Project_Name']
    upper_name = project_name.upper()
    if 'FEMA' in upper_name or 'CALOES' in upper_name or 'CALJPIA' in upper_name:
        amount = int(record['Amount'])
        disaster_funding[project_name] = amount

print('Disaster projects in funding:', len(disaster_funding))
print('Sample:', list(disaster_funding.items())[:5])

result = {'disaster_funding_lookup': disaster_funding, 'count': len(disaster_funding)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.query_db:26': [{'count': '500'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
