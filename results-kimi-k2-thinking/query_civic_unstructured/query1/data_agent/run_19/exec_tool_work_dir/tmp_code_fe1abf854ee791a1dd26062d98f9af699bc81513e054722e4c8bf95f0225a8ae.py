code = """import json

# Load data
f_var = locals()['var_functions.query_db:4']
if isinstance(f_var, str):
    with open(f_var, 'r') as f:
        funding = json.load(f)
else:
    funding = f_var

c_var = locals()['var_functions.query_db:11']
if isinstance(c_var, str):
    with open(c_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = c_var

# Build funding dictionary
funding_dict = {r['Project_Name']: int(r['Amount']) for r in funding}

# Extract design capital projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Find design section and extract project names
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        lines = design_section.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 5 and not line.startswith('Page') and not line.startswith('Agenda'):
                # Clean the line
                clean_line = line.strip(' -•').strip()
                if clean_line in funding_dict:
                    if funding_dict[clean_line] > 50000:
                        design_projects.add(clean_line)

count = len(design_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
