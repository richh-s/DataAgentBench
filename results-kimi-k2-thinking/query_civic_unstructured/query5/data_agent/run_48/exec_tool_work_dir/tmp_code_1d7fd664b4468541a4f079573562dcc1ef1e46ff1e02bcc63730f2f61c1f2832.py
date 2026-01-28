code = """import json

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:5']))
funding_data = json.load(open(locals()['var_functions.query_db:22']))

# Find disaster projects that started in 2022
# Look for 2022 in the text and extract project names
projects_2022 = set()
for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for lines that look like project names
        if len(line) > 10 and not line.startswith('(') and not line.startswith('Page'):
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Drainage', 'Road']
            if any(k in line for k in project_keywords):
                # Check if 2022 appears in this line or nearby
                context = ' '.join(lines[max(0,i-2):min(len(lines),i+3)])
                if '2022' in context:
                    projects_2022.add(line.split('(')[0].strip())

# Match with funding data - sum for disaster projects
matched_funding = 0
matched_projects = []
for fund in funding_data:
    proj_name = fund['Project_Name']
    # Check if disaster-related
    is_disaster = any(indicator in proj_name for indicator in ['FEMA', 'CalOES', 'CalJPIA'])
    
    base_name = proj_name.split('(')[0].strip()
    
    # Check if matches 2022 set or has 2022 in name
    if is_disaster and (base_name in projects_2022 or '2022' in proj_name):
        matched_funding += int(fund['Amount'])
        matched_projects.append(proj_name)

print('__RESULT__:')
print(json.dumps({'total_funding': matched_funding, 'projects': matched_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}, 'var_functions.execute_python:74': {'total_funding_projects': 500, 'disaster_funding_projects': 27, 'sample_disaster': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}]}, 'var_functions.execute_python:76': {'total_disaster_funding': 1410000}}

exec(code, env_args)
