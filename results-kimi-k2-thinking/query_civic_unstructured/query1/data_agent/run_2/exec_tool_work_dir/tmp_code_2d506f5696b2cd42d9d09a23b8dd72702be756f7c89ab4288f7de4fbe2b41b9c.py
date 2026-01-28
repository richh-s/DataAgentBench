code = """import json

funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name'].lower()] = int(item['Amount'])

# Extract design projects from text
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start == -1:
        design_section_start = text.find('Capital Improvement Projects (design)')
    if design_section_start == -1:
        continue
    
    # Get section end
    section_end = text.find('Capital Improvement Projects (', design_section_start + 10)
    if section_end == -1:
        section_end = text.find('Disaster Recovery Projects', design_section_start + 10)
    if section_end == -1:
        section_end = len(text)
    
    section = text[design_section_start:section_end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and not line.startswith('cid:'):
            if 'Updates' not in line and 'Project Schedule' not in line:
                if line.startswith('•') or not any(word in line for word in ['Complete Design', 'Advertise', 'Begin Construction']):
                    project_name = line.strip('•- ').strip()
                    if project_name and len(project_name) > 15:
                        design_projects.append(project_name.lower())

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding
count = 0
for project in design_projects:
    for funding_name in funding_lookup:
        if project in funding_name or funding_name in project:
            amount = funding_lookup[funding_name]
            if amount > 50000:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
