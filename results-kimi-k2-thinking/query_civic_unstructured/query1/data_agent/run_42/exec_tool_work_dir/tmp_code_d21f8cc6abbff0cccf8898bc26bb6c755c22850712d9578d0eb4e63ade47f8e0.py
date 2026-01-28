code = """import json

# Load data files
funding_file = open(var_functions.query_db_162, 'r')
funding_data = json.load(funding_file)
funding_file.close()

mongo_file = open(var_functions.query_db_158, 'r')
mongo_data = json.load(mongo_file)
mongo_file.close()

# Get funding project names from SQLite data
funding_names = [rec['Project_Name'] for rec in funding_data]

# Extract design projects from MongoDB documents
design_projects = []

for doc in mongo_data:
    text_value = doc.get('text', '')
    all_lines = text_value.split('\n')
    in_design_section = False
    
    for one_line in all_lines:
        clean_line = one_line.strip()
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
        elif '(Construction)' in clean_line or '(Not Started)' in clean_line:
            in_design_section = False
        elif in_design_section and clean_line and len(clean_line) > 5:
            # Skip non-project lines
            updates_check = 'Updates:' in clean_line
            schedule_check = 'Schedule:' in clean_line
            page_check = 'Page' in clean_line
            paren_check = clean_line.startswith('(')
            bullet_check = clean_line.startswith('•')
            upper_check = clean_line.isupper()
            consultant_check = 'Consultant' in clean_line
            staff_check = 'Staff' in clean_line
            
            if not (updates_check or schedule_check or page_check or paren_check or bullet_check or upper_check or consultant_check or staff_check):
                design_projects.append(clean_line)

# Count matching projects
match_count = 0
matched_names = set()

for design_name in design_projects:
    for funding_name in funding_names:
        if len(funding_name) > 0:
            design_lower = design_name.lower()
            funding_lower = funding_name.lower()
            
            one_in_two = funding_lower in design_lower
            two_in_one = design_lower in funding_lower
            
            if one_in_two or two_in_one:
                if funding_name not in matched_names:
                    match_count += 1
                    matched_names.add(funding_name)
                break

result_json = json.dumps(match_count)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json', 'var_functions.query_db:162': 'file_storage/functions.query_db:162.json'}

exec(code, env_args)
