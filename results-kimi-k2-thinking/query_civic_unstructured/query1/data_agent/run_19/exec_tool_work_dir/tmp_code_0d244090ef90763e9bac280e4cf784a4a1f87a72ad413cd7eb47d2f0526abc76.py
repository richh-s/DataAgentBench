code = """import json

# Load data from storage
funding_var = locals()['var_functions.query_db:4']
civic_var = locals()['var_functions.query_db:11']

# Load funding data
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_var

# Load civic documents
if isinstance(civic_var, str) and civic_var.endswith('.json'):
    with open(civic_var, 'r') as f:
        civic = json.load(f)
else:
    civic = civic_var

print('Loaded', len(funding), 'funding records and', len(civic), 'civic documents')

# Create set of well-funded projects (> $50,000)
well_funded = set()
for rec in funding:
    if int(rec['Amount']) > 50000:
        well_funded.add(rec['Project_Name'])

print('Found', len(well_funded), 'projects with funding > $50,000')

# Extract capital projects in design status
design_capital_projects = set()

for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        # Detect capital improvement projects design section
        if 'Capital Improvement Projects' in clean_line and 'Design' in clean_line:
            in_design_section = True
            continue
        
        # Exit design section when hitting other major sections
        if in_design_section and ('Capital Improvement Projects' in clean_line and 'Construction' in clean_line):
            break
        if in_design_section and ('Capital Improvement Projects' in clean_line and 'Not Started' in clean_line):
            break
        
        # Capture project names in design section
        if in_design_section and clean_line and len(clean_line) > 5:
            # Remove common bullet/symbol characters
            project_name = clean_line.encode('ascii', errors='ignore').decode().strip()
            
            # Check if project has sufficient funding
            if project_name in well_funded:
                design_capital_projects.add(project_name)

result = len(design_capital_projects)
print('Final count:', result)
print('Some examples:', list(design_capital_projects)[:5])

import json as js
print('__RESULT__:')
print(js.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
