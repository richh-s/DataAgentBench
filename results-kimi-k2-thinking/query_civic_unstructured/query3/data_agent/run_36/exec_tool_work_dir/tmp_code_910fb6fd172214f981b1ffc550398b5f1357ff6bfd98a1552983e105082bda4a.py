code = """import json

# Read the relevant funding records from previous step
relevant_records = locals()['var_functions.execute_python:20']

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    docs_data = json.load(f)

# Find statuses for projects
projects_info = []

for record in relevant_records:
    project_name = record['project_name']
    found_status = 'unknown'
    doc_found = ''
    
    # Search for project in documents
    for doc in docs_data:
        text = doc.get('text', '')
        if project_name.lower() in text.lower():
            doc_found = doc.get('filename', '')
            # Try to find status by looking for keywords
            if 'construction' in text.lower() and 'completed' in text.lower():
                found_status = 'completed'
            elif 'design' in text.lower():
                found_status = 'design'
            elif 'construction' in text.lower():
                found_status = 'construction'
            elif 'not started' in text.lower():
                found_status = 'not started'
            break
    
    projects_info.append({
        'project_name': project_name,
        'funding_source': record['funding_source'],
        'amount': record['amount'],
        'status': found_status,
        'document': doc_found
    })

# Add projects that have disaster-related keywords but might not have FEMA in name
disaster_keywords = ['woolsey fire', 'caloes', 'caljpia', 'recovery', 'disaster']

all_funding = locals()['var_functions.query_db:5']
for record in all_funding:
    project_name = record.get('Project_Name', '')
    name_lower = project_name.lower()
    funding_lower = record.get('Funding_Source', '').lower()
    
    is_disaster_related = False
    for keyword in disaster_keywords:
        if keyword in name_lower or keyword in funding_lower:
            is_disaster_related = True
            break
    
    # Check if it's FEMA related
    if 'fema' in name_lower:
        is_disaster_related = True
    
    if is_disaster_related:
        # Check if already in list
        already_exists = False
        for existing in projects_info:
            if existing['project_name'] == project_name:
                already_exists = True
                break
        
        if not already_exists:
            # Try to find status
            found_status = 'unknown'
            doc_found = ''
            for doc in docs_data:
                text = doc.get('text', '')
                if project_name.lower() in text.lower():
                    doc_found = doc.get('filename', '')
                    if 'construction' in text.lower() and 'completed' in text.lower():
                        found_status = 'completed'
                    elif 'design' in text.lower():
                        found_status = 'design'
                    elif 'construction' in text.lower():
                        found_status = 'construction'
                    break
            
            projects_info.append({
                'project_name': project_name,
                'funding_source': record.get('Funding_Source', ''),
                'amount': int(record.get('Amount', 0)),
                'status': found_status,
                'document': doc_found
            })

# Sort by amount descending
projects_info.sort(key=lambda x: x['amount'], reverse=True)

print('Emergency/FEMA Related Projects')
print('================================')
for p in projects_info:
    print('Project: ' + p['project_name'])
    print('Funding: ' + p['funding_source'] + ' ($' + str(p['amount']) + ')')
    print('Status: ' + p['status'])
    if p['document']:
        print('Document: ' + p['document'])
    print('')

print('__RESULT__:')
print(json.dumps(projects_info))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '23', 'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '27', 'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '30', 'Project_Name': 'Discussion', 'Funding_Source': 'International Aid', 'Amount': '80000'}, {'Funding_ID': '31', 'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project', 'Funding_Source': 'Philanthropic Donation', 'Amount': '90000'}, {'Funding_ID': '32', 'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': '56000'}, {'Funding_ID': '33', 'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '36', 'Project_Name': 'Encinal Canyon Road Repairs', 'Funding_Source': 'State Development Grant', 'Amount': '47000'}, {'Funding_ID': '37', 'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '40', 'Project_Name': 'Harbor Vista Curb Return', 'Funding_Source': 'Social Impact Investment', 'Amount': '91000'}, {'Funding_ID': '41', 'Project_Name': 'Kanan Dume Biofilter', 'Funding_Source': 'Venture Capital Fund', 'Amount': '56000'}, {'Funding_ID': '42', 'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '45', 'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000'}, {'Funding_ID': '46', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 50, 'civic_docs': 19, 'fema_docs': 19, 'emergency_docs': 5}, 'var_functions.execute_python:20': [{'project_name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'funding_source': 'Research Institution Funding', 'amount': 14000, 'funding_id': '7'}, {'project_name': 'Clover Heights Storm Drain (FEMA Project)', 'funding_source': 'Local NGO Fund', 'amount': 21000, 'funding_id': '22'}, {'project_name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'funding_source': 'Municipal Fund', 'amount': 43000, 'funding_id': '25'}, {'project_name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'funding_source': 'Taxpayer Contribution', 'amount': 15000, 'funding_id': '26'}, {'project_name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'funding_source': 'Local Business Support', 'amount': 25000, 'funding_id': '28'}, {'project_name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'funding_source': 'Cultural Heritage Grant', 'amount': 58000, 'funding_id': '29'}, {'project_name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'funding_source': 'Private Sponsor', 'amount': 94000, 'funding_id': '35'}, {'project_name': 'Guardrail Replacement Citywide (FEMA Project)', 'funding_source': 'Impact Investment Fund', 'amount': 22000, 'funding_id': '38'}, {'project_name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'funding_source': 'Development Bank Loan', 'amount': 45000, 'funding_id': '39'}, {'project_name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'funding_source': 'Federal Assistance', 'amount': 36000, 'funding_id': '43'}, {'project_name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'funding_source': 'National Foundation Fund', 'amount': 44000, 'funding_id': '44'}, {'project_name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'funding_source': 'Municipal Fund', 'amount': 91000, 'funding_id': '47'}, {'project_name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'funding_source': 'Community Fund', 'amount': 78000, 'funding_id': '48'}, {'project_name': 'Birdview Avenue Improvements (CalOES Project)', 'funding_source': 'International Aid', 'amount': 85000, 'funding_id': '6'}, {'project_name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'funding_source': 'Government Grant', 'amount': 81000, 'funding_id': '11'}, {'project_name': 'Corral Canyon Culvert Repairs', 'funding_source': 'Federal Assistance', 'amount': 54000, 'funding_id': '24'}, {'project_name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'funding_source': 'Educational Sponsorship', 'amount': 18000, 'funding_id': '34'}]}

exec(code, env_args)
