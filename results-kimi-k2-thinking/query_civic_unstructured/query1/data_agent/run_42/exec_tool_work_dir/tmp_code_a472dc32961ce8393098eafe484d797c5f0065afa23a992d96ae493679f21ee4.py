code = """import json

# Load funding data (projects > $50,000)
funding_path = var_functions.query_db_138
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load mongo data (civic documents with project information)
mongo_path = var_functions.query_db_158
with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

# Extract funding project names
funding_names = set()
for record in funding_data:
    funding_names.add(record['Project_Name'])

# Extract design projects from mongo documents
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design_section = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design_section = False
        elif in_design_section and clean:
            # Skip non-project lines
            skip_patterns = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 
                           'Begin Construction:', 'To:', 'Subject:', 'Page', 'Prepared by:', 
                           'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 
                           'Staff will', 'City is', 'City will', 'Project is', 'Plans are']
            should_skip = any(pattern in clean for pattern in skip_patterns)
            
            if not should_skip and len(clean) > 5 and not clean.startswith('(') and not clean.startswith('•'):
                if not clean.isupper():
                    project_name = clean.strip('•- ')
                    design_projects.append(project_name)

# Find matches between funding projects and design projects
matches = set()
for design_name in design_projects:
    for funding_name in funding_names:
        # Case-insensitive partial matching
        design_lower = design_name.lower()
        funding_lower = funding_name.lower()
        if funding_lower in design_lower or design_lower in funding_lower:
            matches.add(funding_name)

result = len(matches)

print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json'}

exec(code, env_args)
