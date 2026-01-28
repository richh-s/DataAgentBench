code = """import json

# Load funding data
f_path = var_functions.query_db:6
f_data = open(f_path).read()
funding = json.loads(f_data)

# Filter for projects with funding > $50,000
high_funding_names = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        high_funding_names.append(rec['Project_Name'].lower().strip())

# Load civic documents
c_path = var_functions.query_db:10
c_data = open(c_path).read()
docs = json.loads(c_data)

# Extract design capital projects
design_projects = []

for doc in docs:
    text = doc.get('text', '')
    
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital Improvement Projects (Construction)'
    
    start_pos = text.find(start_marker)
    if start_pos >= 0:
        end_pos = text.find(end_marker, start_pos)
        if end_pos < 0:
            end_pos = start_pos + 5000
        
        section = text[start_pos:end_pos]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('(') and not line.isupper():
                if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                    design_projects.append(line.lower())

# Count matches
count = 0
for design in design_projects:
    for funded in high_funding_names:
        if design in funded or funded in design:
            count += 1
            break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
