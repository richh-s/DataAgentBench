code = """import json

# Load data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Identify disaster projects from funding
disaster_projects = []
for record in funding_data:
    name = record['Project_Name']
    if '(FEMA Project)' in name or '(CalJPIA Project)' in name or '(CalOES Project)' in name:
        disaster_projects.append(record)

# Look for 2022 indicators in civic docs
civ_text_combined = ''
for doc in civic_docs:
    civ_text_combined += doc.get('text', '') + '\n'

# Find which disaster projects likely started in 2022
funds_2022 = []
total_fund = 0

for proj in disaster_projects:
    name = proj['Project_Name']
    
    # Check several conditions for 2022 start
    in_2022 = False
    
    # 1. Name starts with 2022
    if name.startswith('2022'):
        in_2022 = True
    
    # 2. Find base name in civic docs with 2022 context
    if not in_2022:
        base = name.split('(')[0].strip()
        # Look for this project with 2022 nearby
        import re
        pattern = re.compile(r'.{0,100}' + re.escape(base[:25]) + r'.{0,200}2022', re.IGNORECASE)
        if pattern.search(civ_text_combined):
            in_2022 = True
    
    if in_2022:
        funds_2022.append(proj)
        total_fund += proj['Amount']

print('__RESULT__:')
result = {
    'disaster_projects_total': len(disaster_projects),
    'disaster_2022_found': len(funds_2022),
    'total_funding_2022': total_fund,
    'project_details': [{'name': p['Project_Name'], 'amount': p['Amount']} for p in funds_2022]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:16': {'disaster_projects_found': 27, 'total_disaster_funding': 1410000, 'sample_disaster_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'sample_funding_records': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}]}, 'var_functions.execute_python:18': {'total_disaster_2022_projects': 0, 'total_funding': 0, 'sample_projects': []}}

exec(code, env_args)
