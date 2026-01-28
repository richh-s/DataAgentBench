code = """import json

# Load funding data
funding_var = locals()['var_functions.query_db:4']
if type(funding_var) is str and funding_var.endswith('.json'):
    f = open(funding_var, 'r')
    funding_data = json.load(f)
    f.close()
else:
    funding_data = funding_var

# Load civic documents  
civic_var = locals()['var_functions.query_db:11']
if type(civic_var) is str and civic_var.endswith('.json'):
    f = open(civic_var, 'r')
    civic_docs = json.load(f)
    f.close()
else:
    civic_docs = civic_var

# Build funding map
funding_map = {}
for rec in funding_data:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Find capital projects in design
found_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Check for capital improvement projects in design
    if 'Capital Improvement Projects (Design)' in text:
        lines = text.split('\n')
        in_design = False
        for line in lines:
            if 'Capital Improvement Projects (Design)' in line:
                in_design = True
            elif 'Capital Improvement Projects (Construction)' in line:
                break
            elif in_design and line.strip():
                project_name = line.strip()
                if project_name in funding_map:
                    if funding_map[project_name] > 50000:
                        found_projects.add(project_name)

count = len(found_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
