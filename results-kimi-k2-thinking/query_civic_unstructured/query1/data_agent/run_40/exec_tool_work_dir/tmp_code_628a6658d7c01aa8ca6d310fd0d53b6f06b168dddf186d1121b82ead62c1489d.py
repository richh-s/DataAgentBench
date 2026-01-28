code = """import json

# Load funding records
funding_data = json.load(open('storage/query_result_6.json'))

# Build set of projects with funding > $50,000
funded_projects = set()
for rec in funding_data:
    if int(rec['Amount']) > 50000:
        funded_projects.add(rec['Project_Name'].lower().strip())

# Load civic documents
civic_docs = json.load(open('storage/query_result_10.json'))

# Extract design capital projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    start = text.find(design_marker)
    if start == -1:
        continue
    
    # Extract design section (limited length)
    section = text[start:start+6000]
    
    for line in section.split('\n'):
        line = line.strip()
        # Filter for likely project names
        if 10 < len(line) < 100 and not line.startswith('(') and not line.isupper():
            if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                if 'Complete' not in line and 'Advertise' not in line and 'Begin' not in line:
                    design_projects.add(line.lower())

# Count matching projects
count = 0
for design in design_projects:
    for funded in funded_projects:
        # Check if strings overlap
        if design in funded or funded in design:
            count += 1
            break

result = json.dumps({'count': count})
print('____RESULT____:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
