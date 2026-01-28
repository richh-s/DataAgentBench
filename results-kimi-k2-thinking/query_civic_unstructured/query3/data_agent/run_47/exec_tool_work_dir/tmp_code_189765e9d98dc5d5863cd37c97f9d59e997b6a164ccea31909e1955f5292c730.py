code = """import json

# Load funding data
f_data = locals()['var_functions.query_db:2']
with open(f_data, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
c_data = locals()['var_functions.query_db:4']
with open(c_data, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic documents')

# Find projects with FEMA/EMERGENCY in names
target_projects = []
for rec in funding_records:
    name = rec['Project_Name']
    if 'FEMA' in name.upper() or 'EMERGENCY' in name.upper() or 'WARNING' in name.upper():
        target_projects.append({
            'Project_Name': name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'status': 'Unknown'
        })

print('Found', len(target_projects), 'projects with FEMA/EMERGENCY in name')

# Try to find statuses from documents
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    current_status = None
    
    for line in lines:
        line_up = line.upper()
        
        # Check for status sections
        if 'DESIGN)' in line_up and 'PROJECT' in line_up:
            current_status = 'design'
        elif 'CONSTRUCTION)' in line_up and 'PROJECT' in line_up:
            current_status = 'construction'
        elif 'NOT STARTED)' in line_up and 'PROJECT' in line_up:
            current_status = 'not started'
        
        # Check if line contains any of our project base names
        if current_status:
            for proj in target_projects:
                base_name = proj['Project_Name'].split('(')[0].strip().upper()
                if base_name in line_up and len(base_name) > 5:
                    proj['status'] = current_status

# Create final result
result = json.dumps(target_projects, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
