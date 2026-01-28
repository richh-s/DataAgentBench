code = """import json

# Load the data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Check each funding record for disaster projects that started in 2022
disaster_2022_projects = []
total_funding = 0

for fund_record in funding_data:
    name = fund_record['Project_Name']
    
    # Check if it's a disaster project
    is_disaster = False
    if '(FEMA Project)' in name or '(CalJPIA Project)' in name or '(CalOES Project)' in name:
        is_disaster = True
    
    # Also check for other disaster indicators
    if not is_disaster:
        for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'emergency warning', 'fire recovery']:
            if keyword.lower() in name.lower():
                is_disaster = True
                break
    
    if is_disaster:
        # Check if started in 2022 (name starts with 2022 or in civic docs context)
        if name.startswith('2022'):
            # This definitely started in 2022
            disaster_2022_projects.append(fund_record)
            total_funding += fund_record['Amount']
        else:
            # Check if project name appears with 2022 in civic docs
            for doc in civic_docs:
                text = doc.get('text', '')
                if name in text and '2022' in text:
                    # Additional check: ensure 2022 is in context
                    import re
                    # Look for the project name and 2022 nearby
                    pattern = re.compile(r'[^.]{0,100}' + re.escape(name[:30]) + r'[^.]{0,200}2022', re.IGNORECASE)
                    if pattern.search(text):
                        disaster_2022_projects.append(fund_record)
                        total_funding += fund_record['Amount']
                        break

print('__RESULT__:')
result = {
    'total_disaster_2022_projects': len(disaster_2022_projects),
    'total_funding': total_funding,
    'sample_projects': disaster_2022_projects[:10]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:16': {'disaster_projects_found': 27, 'total_disaster_funding': 1410000, 'sample_disaster_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'sample_funding_records': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}]}}

exec(code, env_args)
