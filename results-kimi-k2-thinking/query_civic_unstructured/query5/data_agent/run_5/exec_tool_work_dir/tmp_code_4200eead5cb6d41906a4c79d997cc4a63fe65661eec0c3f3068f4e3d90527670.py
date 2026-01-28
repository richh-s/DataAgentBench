code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8'] 
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Get all disaster-related projects from funding
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA']
disaster_funding = []

for record in funding_records:
    proj_name = record['Project_Name']
    if any(keyword in proj_name for keyword in disaster_keywords):
        amount = int(record['Amount'])
        disaster_funding.append({
            'name': proj_name,
            'amount': amount
        })

# Check if projects started in 2022
# Look for 2022 in filename or document text related to projects
total_2022_funding = 0
projects_in_2022 = []

for proj in disaster_funding:
    proj_lower = proj['name'].lower()
    
    for doc in civic_docs:
        doc_text = doc['text'].lower()
        
        # Check if project mentioned in document
        project_mentioned = False
        
        # Extract base name without disaster suffix
        base_name = proj['name'].replace('(FEMA Project)', '').replace('(FEMA/CalOES Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '').strip()
        
        if base_name.lower().strip() in doc_text:
            project_mentioned = True
            
        # Check if 2022 appears in document and refers to start/advertisement
        if project_mentioned:
            if '2022' in doc['filename']:
                # Found a match
                total_2022_funding += proj['amount']
                projects_in_2022.append(proj)
                break
            elif '2022' in doc_text:
                # Look for context around 2022
                lines = doc['text'].split('\n')
                for line in lines:
                    line_lower = line.lower()
                    if '2022' in line and base_name.lower() in line_lower:
                        total_2022_funding += proj['amount']
                        projects_in_2022.append(proj)
                        break
                
print('__RESULT__:')
print(json.dumps({
    'total_funding': total_2022_funding,
    'project_count': len(projects_in_2022)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)
