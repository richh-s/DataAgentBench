code = """import json

f_data = locals()['var_functions.query_db:2']
c_data = locals()['var_functions.query_db:4']

with open(f_data, 'r') as f:
    funding = json.load(f)

with open(c_data, 'r') as f:
    docs = json.load(f)

print('Funding records:', len(funding))
print('Documents:', len(docs))

fema_projects = []

for rec in funding:
    name = rec['Project_Name']
    if 'FEMA' in name.upper() or 'EMERGENCY' in name.upper():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'status': 'Unknown'
        })

print('FEMA projects:', len(fema_projects))

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    status = None
    
    for line in lines:
        up = line.upper()
        
        if 'DESIGN' in up and 'PROJECT' in up:
            status = 'design'
        elif 'CONSTRUCTION' in up and 'PROJECT' in up:
            status = 'construction'
        elif 'NOT STARTED' in up and 'PROJECT' in up:
            status = 'not started'
        
        if status:
            for proj in fema_projects:
                base = proj['Project_Name'].split('(')[0].strip().upper()
                if base in up and len(base) > 5:
                    proj['status'] = status

print('__RESULT__:')
print(json.dumps(fema_projects, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
