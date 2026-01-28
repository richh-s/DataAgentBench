code = """import json
import re

funding_data = locals()['var_functions.query_db:2']
civic_docs_data = locals()['var_functions.query_db:5']

results = []

for item in funding_data:
    name = item['Project_Name']
    if 'FEMA' in name or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': item['Funding_Source'],
            'Amount': item['Amount'],
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

funding_names = [item['Project_Name'] for item in funding_data]

for doc in civic_docs_data:
    text = doc.get('text', '')
    if 'FEMA' in text:
        for fund_name in funding_names:
            if 'FEMA' in fund_name and fund_name in text:
                for item in funding_data:
                    if item['Project_Name'] == fund_name:
                        results.append({
                            'Project_Name': fund_name,
                            'Funding_Source': item['Funding_Source'],
                            'Amount': item['Amount'],
                            'Status': 'unknown',
                            'Topic': 'FEMA,emergency'
                        })

unique = {}
for p in results:
    unique[p['Project_Name']] = p

final = list(unique.values())
final.sort(key=lambda x: x['Project_Name'])

output = []
for p in final:
    output.append({
        'Project_Name': p['Project_Name'],
        'Funding_Source': p['Funding_Source'],
        'Amount': int(p['Amount']),
        'Status': p['Status'],
        'Topic': p['Topic']
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
