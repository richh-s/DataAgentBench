code = """import json

# Get data from storage
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

# Build funding lookup
funding = {}
for item in funding_data:
    funding[item['Project_Name'].lower()] = int(item['Amount'])

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start position
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos == -1:
        continue
    
    # Find where the design section ends
    next_pos = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, design_pos + 10)
        if pos > 0 and pos < next_pos:
            next_pos = pos
    
    design_text = text[design_pos:next_pos]
    lines = design_text.split('\n')
    
    # Collect likely project names
    collect_mode = False
    for line in lines:
        line = line.strip()
        if len(line) > 20 and 'Capital Improvement Projects (Design)' not in line:
            # Skip status/update lines
            if 'Updates:' not in line and 'Project Schedule:' not in line and 'Complete Design:' not in line:
                if 'Advertise:' not in line and 'Begin Construction:' not in line:
                    # Remove bullet markers
                    project_name = line.strip('•-').strip()
                    design_projects.add(project_name.lower())

# Match with funding
matches = []
for proj in design_projects:
    for fund_name in funding:
        if proj in fund_name or fund_name in proj:
            if funding[fund_name] > 50000:
                matches.append(proj)
                break

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
