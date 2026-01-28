code = """import json

# Load funding data
with open('storage/query_result_6.json') as f:
    funding_data = json.load(f)

# Load civic documents
with open('storage/query_result_10.json') as f:
    civic_docs = json.load(f)

# Get set of project names with funding > $50,000
funded_projects = set()
for rec in funding_data:
    if int(rec['Amount']) > 50000:
        funded_projects.add(rec['Project_Name'].lower().strip())

# Count design capital projects with high funding
count = 0
matched_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos == -1:
        continue
    
    # Find end of design section
    construction_pos = text.find('Capital Improvement Projects (Construction)', design_pos)
    if construction_pos == -1:
        construction_pos = text.find('Capital Improvement Projects (Not Started)', design_pos)
    if construction_pos == -1:
        construction_pos = design_pos + 6000
    
    design_section = text[design_pos:construction_pos]
    
    # Extract project names
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) > 15 and not line.startswith('(') and not line.isupper():
            if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                if 'Complete Design:' not in line and 'Advertise:' not in line and 'Begin Construction:' not in line:
                    line_lower = line.lower()
                    # Check if this project has high funding
                    for funded in funded_projects:
                        if funded in line_lower or line_lower in funded:
                            count += 1
                            matched_names.append(line)
                            break

result = json.dumps({'count': count, 'projects': matched_names})
print('____RESULT____:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
