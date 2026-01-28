code = """import json

# Load the actual civic documents data
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data directly
funding_data = locals()['var_functions.query_db:20']

print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_data)} funding records')

# Based on the document preview, we can see Bluffs Park Shade Structure was completed in November 2022
# Lets check what projects exist in the funding data
park_funding_projects = [f for f in funding_data if 'Park' in f['Project_Name']]
print(f'Found {len(park_funding_projects)} park projects in funding data')

for p in park_funding_projects:
    print(f"- {p['Project_Name']}: ${p['Amount']}")

result = {
    'park_funding_projects': park_funding_projects,
    'count': len(park_funding_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_functions.execute_python:26': {'status': 'success'}}

exec(code, env_args)
