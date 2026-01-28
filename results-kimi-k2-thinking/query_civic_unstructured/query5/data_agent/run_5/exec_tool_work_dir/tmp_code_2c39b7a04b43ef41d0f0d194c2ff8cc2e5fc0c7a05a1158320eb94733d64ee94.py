code = """import json

# Load data
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Find disaster projects
disaster_projects = []
for rec in funding_data:
    name = rec['Project_Name']
    if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        disaster_projects.append({
            'full_name': name,
            'base_name': name.replace('(FEMA Project)', '').replace('(FEMA/CalOES Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '').replace('(FEMA)', '').strip(),
            'amount': int(rec['Amount'])
        })

# Check which started in 2022
starting_2022 = []
for proj in disaster_projects:
    base_lower = proj['base_name'].lower()
    
    for doc in civic_docs:
        if '2022' in doc.get('filename', ''):
            if base_lower in doc['text'].lower():
                starting_2022.append(proj)
                break
        else:
            # Check document text for 2022 mentions
            text_lower = doc['text'].lower()
            if '2022' in text_lower and base_lower in text_lower:
                # Check lines for context
                lines = doc['text'].split('\n')
                for line in lines:
                    line_lower = line.lower()
                    if '2022' in line_lower and base_lower in line_lower:
                        if 'begin' in line_lower or 'start' in line_lower or 'advertise' in line_lower:
                            starting_2022.append(proj)
                            break

# Calculate total funding
total_amount = sum(p['amount'] for p in starting_2022)
print('__RESULT__:')
print(json.dumps({'total_funding': total_amount, 'project_count': len(starting_2022)}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)
