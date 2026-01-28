code = """import json

# Load funding data
funding_data = json.load(open(locals()['var_functions.query_db:22']))

# Load civic docs data
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Calculate funding for disaster projects with indicators they started in 2022
# We'll use multiple indicators: 1) project name contains 2022, 2) found in civic docs with 2022
total_funding = 0
disaster_projects_2022 = []

# First pass: find all disaster projects that have 2022 in the name
for fund in funding_data:
    proj_name = fund['Project_Name']
    is_disaster = any(indicator in proj_name for indicator in ['FEMA', 'CalOES', 'CalJPIA'])
    has_2022 = '2022' in proj_name
    
    if is_disaster and has_2022:
        amount = int(fund['Amount'])
        total_funding += amount
        disaster_projects_2022.append(proj_name)

# Also check for disaster projects in 2022 from civic docs
# Look for projects mentioned with 2022 dates
civic_2022_projects = set()
for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) > 10:
            has_disaster_indicators = any(x in line for x in ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster'])
            if has_disaster_indicators:
                base_name = line.split('(')[0].strip()
                if base_name:
                    civic_2022_projects.add(base_name)

# Add funding for projects found in civic docs with 2022
for fund in funding_data:
    proj_name = fund['Project_Name']
    base_name = proj_name.split('(')[0].strip()
    is_disaster = any(indicator in proj_name for indicator in ['FEMA', 'CalOES', 'CalJPIA'])
    
    if is_disaster and base_name in civic_2022_projects and proj_name not in disaster_projects_2022:
        amount = int(fund['Amount'])
        total_funding += amount
        disaster_projects_2022.append(proj_name)

result = {'total_funding_2022_disaster': total_funding, 'projects_count': len(disaster_projects_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}, 'var_functions.execute_python:74': {'total_funding_projects': 500, 'disaster_funding_projects': 27, 'sample_disaster': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}]}, 'var_functions.execute_python:76': {'total_disaster_funding': 1410000}}

exec(code, env_args)
