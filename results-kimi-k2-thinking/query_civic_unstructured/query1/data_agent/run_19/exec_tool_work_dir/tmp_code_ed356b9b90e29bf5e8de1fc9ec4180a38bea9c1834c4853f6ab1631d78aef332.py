code = """import json

# Access the results from storage
funding_result = locals()['var_functions.query_db:4']
civic_result = locals()['var_functions.query_db:11']

# Load data from files if needed
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_result

if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic = json.load(f)
else:
    civic = civic_result

# Create a set of project names that have funding > 50000
funded_projects = set()
for rec in funding:
    if int(rec['Amount']) > 50000:
        funded_projects.add(rec['Project_Name'])

# Find capital projects in design status from civic documents
matching_projects = set()

for doc in civic:
    text = doc.get('text', '')
    # Split document into lines
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line_clean = line.strip()
        # Detect when we enter the capital improvement projects design section
        if 'Capital Improvement Projects' in line_clean and 'Design' in line_clean:
            in_design_section = True
            continue
        
        # Exit design section when hitting other sections
        if in_design_section and ('Construction' in line_clean or 'Not Started' in line_clean):
            break
        
        # Record project names in the design section
        if in_design_section and line_clean and len(line_clean) > 5:
            # Check if this line is a project name with funding
            if line_clean in funded_projects:
                matching_projects.add(line_clean)

# Count distinct matches
count = len(matching_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
