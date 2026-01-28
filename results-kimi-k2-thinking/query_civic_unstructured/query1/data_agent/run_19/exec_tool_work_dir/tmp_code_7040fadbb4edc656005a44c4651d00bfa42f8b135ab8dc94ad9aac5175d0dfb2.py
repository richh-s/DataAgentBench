code = """import json

# Get the funding data
funding_result = locals()['var_functions.query_db:4']
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_result

# Get the civic documents
civic_result = locals()['var_functions.query_db:11']
if isinstance(civic_result, str):
    with open(civic_result, 'r') as f:
        civic = json.load(f)
else:
    civic = civic_result

print('Loaded', len(funding), 'funding records and', len(civic), 'civic documents')

# Create set of projects with funding > 50000
well_funded = set()
for record in funding:
    if int(record['Amount']) > 50000:
        well_funded.add(record['Project_Name'])

# Find capital projects in design status
design_projects = set()

for doc in civic:
    text = doc.get('text', '') 
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        
        # Detect design section
        if 'Capital Improvement Projects' in clean_line and 'Design' in clean_line:
            in_design_section = True
            continue
            
        # Exit design section
        if in_design_section and ('Construction' in clean_line or 'Not Started' in clean_line):
            break
            
        # Add project if well-funded
        if in_design_section and clean_line and clean_line in well_funded:
            design_projects.add(clean_line)

result_count = len(design_projects)
print('Found', result_count, 'matching projects')

# Prepare output
output = json.dumps(result_count)

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
