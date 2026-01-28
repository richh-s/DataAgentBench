code = """import json

# Load data from files
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Find projects related to emergency/FEMA
results = []
project_names = []

# First pass: projects with FEMA/EMERGENCY in name
for record in funding_data:
    proj_name = record['Project_Name']
    upper_name = proj_name.upper()
    
    if 'FEMA' in upper_name or 'EMERGENCY' in upper_name:
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount']),
            'status': 'Unknown'
        })
        project_names.append(proj_name.split('(')[0].strip().upper())

# Try to extract status from documents
for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    current_status = None
    for line in text.split('\n'):
        line_upper = line.strip().upper()
        
        # Check section headers
        if 'CAPITAL IMPROVEMENT PROJECTS' in line_upper or 'DISASTER RECOVERY PROJECTS' in line_upper:
            if '(DESIGN)' in line_upper:
                current_status = 'design'
            elif '(CONSTRUCTION)' in line_upper:
                current_status = 'construction'
            elif '(NOT STARTED)' in line_upper:
                current_status = 'not started'
        
        # Update matching projects
        if current_status:
            for proj in results:
                base_name = proj['Project_Name'].split('(')[0].strip().upper()
                if base_name in line_upper and len(base_name) > 8:
                    proj['status'] = current_status

# Final output
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
