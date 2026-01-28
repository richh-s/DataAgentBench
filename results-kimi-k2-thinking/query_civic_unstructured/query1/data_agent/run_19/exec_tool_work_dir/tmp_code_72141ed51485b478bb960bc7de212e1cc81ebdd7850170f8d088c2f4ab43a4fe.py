code = """import json

# Load data
funding_info = locals()['var_functions.query_db:4']
civic_info = locals()['var_functions.query_db:11']

if isinstance(funding_info, str):
    with open(funding_info, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_info

if isinstance(civic_info, str):
    with open(civic_info, 'r') as f:
        civic = json.load(f)
else:
    civic = civic_info

print('Funding records:', len(funding))
print('Civic documents:', len(civic))

# Get well-funded project names
well_funded = [rec for rec in funding if int(rec['Amount']) > 50000]
print('Well-funded projects (> $50K):', len(well_funded))

# Find matches in civic documents
matching_projects = set()
for doc in civic:
    text = doc.get('text', '')
    for project in well_funded:
        project_name = project['Project_Name']
        if project_name in text:
            # Check if in design section
            design_pos = text.find('Capital Improvement Projects (Design)')
            construction_pos = text.find('Capital Improvement Projects (Construction)')
            project_pos = text.find(project_name)
            
            if design_pos >= 0 and project_pos > design_pos:
                if construction_pos < 0 or project_pos < construction_pos:
                    matching_projects.add(project_name)

count = len(matching_projects)

# Output in required format
result_json = json.dumps(count)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
