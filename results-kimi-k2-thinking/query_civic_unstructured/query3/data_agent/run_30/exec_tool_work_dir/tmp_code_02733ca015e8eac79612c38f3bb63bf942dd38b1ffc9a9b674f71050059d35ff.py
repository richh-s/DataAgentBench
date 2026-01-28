code = """import json

funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

results = []

for item in funding_data:
    name = item['Project_Name']
    if 'FEMA' in name or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = item

print('__RESULT__:')
print(json.dumps({'count': len(results), 'sample': results[:3]}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
