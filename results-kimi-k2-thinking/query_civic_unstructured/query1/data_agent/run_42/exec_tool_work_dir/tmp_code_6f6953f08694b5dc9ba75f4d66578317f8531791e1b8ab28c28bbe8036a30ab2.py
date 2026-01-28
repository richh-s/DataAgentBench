code = """import json

# Simple approach to count matches between funding and design projects

# Load funding data
f_file = open(var_functions.query_db_162, 'r')
funding = json.load(f_file)
f_file.close()

# Load mongo data
m_file = open(var_functions.query_db_158, 'r')
mongo = json.load(m_file)
m_file.close()

# Get funding project names over $50k
funding_names = [item['Project_Name'] for item in funding]

# Extract design project names from mongo docs
design_names = []

for doc in mongo:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design = False
        elif in_design and clean and len(clean) > 5:
            # Skip update/schedule lines
            if 'Updates:' not in clean and 'Schedule:' not in clean and 'To:' not in clean:
                if 'Page' not in clean and not clean.startswith('(') and not clean.startswith('•'):
                    if not clean.isupper() and 'Consultant' not in clean and 'Staff' not in clean:
                        design_names.append(clean)

# Count matching projects
matches = []
for d in design_names:
    for f in funding_names:
        if len(d) > 5 and len(f) > 0:
            if f.lower() in d.lower() or d.lower() in f.lower():
                if f not in matches:
                    matches.append(f)
                break

answer = len(matches)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json', 'var_functions.query_db:162': 'file_storage/functions.query_db:162.json'}

exec(code, env_args)
