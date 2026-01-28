code = """import json

# Load funding data
funding_store = locals()['var_functions.query_db:6']
with open(funding_store, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_store = locals()['var_functions.query_db:8']
with open(civic_store, 'r') as f:
    civic_docs = json.load(f)

# Get disaster-related projects
disaster_projects = []
for rec in funding_data:
    name = rec['Project_Name']
    if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        cleaned_name = name.replace('(FEMA Project)', '').replace('(FEMA/CalOES Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '').replace('(FEMA)', '').strip()
        disaster_projects.append({
            'full': name,
            'base': cleaned_name,
            'amount': int(rec['Amount'])
        })

# Check which projects relate to 2022
projects_2022 = []
for proj in disaster_projects:
    base_lower = proj['base'].lower()
    
    for doc in civic_docs:
        # Check filename for 2022
        if '2022' in doc.get('filename', ''):
            # Check if project mentioned
            if base_lower in doc['text'].lower():
                projects_2022.append(proj)
                break
        
        # Check document content
        text = doc['text'].lower()
        if base_lower in text and '2022' in text:
            # Look for schedule context
            lines = [l.lower() for l in doc['text'].split('\n')]
            for line in lines:
                if base_lower in line and '2022' in line:
                    if 'begin' in line or 'start' in line or 'advertise' in line or 'complete' in line:
                        projects_2022.append(proj)
                        break

# Calculate total funding
total_funding = sum(p['amount'] for p in projects_2022)

result = {
    'total_funding': total_funding,
    'project_count': len(projects_2022),
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)
