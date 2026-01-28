code = """import json

# Load funding data
f_file = open(locals()['var_functions.query_db:2'], 'r')
funding_records = json.load(f_file)
f_file.close()

# Load civic documents
c_file = open(locals()['var_functions.query_db:4'], 'r')
civic_docs = json.load(c_file)
c_file.close()

# Find FEMA/emergency projects
projects_list = []

# Extract projects with FEMA/EMERGENCY in name
for rec in funding_records:
    pname = rec['Project_Name']
    pname_upper = pname.upper()
    if 'FEMA' in pname_upper or 'EMERGENCY' in pname_upper:
        projects_list.append({
            'Project_Name': pname,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'status': 'Unknown'
        })

# Try to find status from documents
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    curr_status = None
    
    for line in lines:
        line_up = line.upper().strip()
        # Determine section
        if 'DESIGN' in line_up and 'PROJECT' in line_up:
            curr_status = 'design'
        elif 'CONSTRUCTION' in line_up and 'PROJECT' in line_up:
            curr_status = 'construction'
        elif 'NOT STARTED' in line_up and 'PROJECT' in line_up:
            curr_status = 'not started'
        
        # Update project status if found
        if curr_status:
            for proj in projects_list:
                base = proj['Project_Name'].split('(')[0].strip().upper()
                if base in line_up and len(base) > 5:
                    proj['status'] = curr_status

# Output results
result_str = json.dumps(projects_list, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
