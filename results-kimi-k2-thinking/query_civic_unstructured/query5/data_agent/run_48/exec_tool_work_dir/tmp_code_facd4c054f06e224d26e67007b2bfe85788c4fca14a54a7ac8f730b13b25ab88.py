code = """import json

# Load full funding data
funding_file = str(locals()['var_functions.query_db:22'])
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file = str(locals()['var_functions.query_db:5'])
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Strategy: Look for disaster projects that have 2022 in their name (indicating start year)
# and also check civic docs for 2022 disaster projects

# Find all unique project base names from disaster funding records
all_disaster_base_names = set()
for fund in funding_data:
    name = fund['Project_Name']
    if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        base = name.split('(')[0].strip()
        all_disaster_base_names.add(base)

# Look for projects with 2022 dates in civic docs
projects_with_2022 = set()
for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) > 10:
            # If line has disaster indicators and mentions start/completion
            has_disaster = any(x in line for x in ['FEMA', 'CalOES', 'CalJPIA'])
            if has_disaster:
                base = line.split('(')[0].strip()
                projects_with_2022.add(base)

# Calculate total funding for disaster projects
# Either: have 2022 in name, OR are in the 2022 civic docs set
valid_disaster_projects = []
for fund in funding_data:
    name = fund['Project_Name']
    
    # Check if it's disaster-related
    is_disaster = any(indicator in name for indicator in ['FEMA', 'CalOES', 'CalJPIA'])
    if not is_disaster:
        continue
    
    base_name = name.split('(')[0].strip()
    
    # Check if starts in 2022 (either explicitly in name or found in civic docs)
    starts_in_2022 = '2022' in name or base_name in projects_with_2022
    
    if starts_in_2022:
        amount = int(fund['Amount'])
        valid_disaster_projects.append({
            'name': name,
            'amount': amount
        })

# Calculate final total
total_funding = sum(p['amount'] for p in valid_disaster_projects)

print('__RESULT__:')
print(json.dumps({
    'total_disaster_funding_2022': total_funding,
    'project_count': len(valid_disaster_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}, 'var_functions.execute_python:74': {'total_funding_projects': 500, 'disaster_funding_projects': 27, 'sample_disaster': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}]}, 'var_functions.execute_python:76': {'total_disaster_funding': 1410000}}

exec(code, env_args)
