code = """import json

# Load data from files
funding_path = var_functions.query_db_138
mongo_path = var_functions.query_db_104

with open(funding_path) as f:
    funding_data = json.load(f)

with open(mongo_path) as f:
    mongo_data = json.load(f)

# Extract funding project names
funding_names = [item["Project_Name"] for item in funding_data]

# Extract design projects from mongo documents
design_projects = []
for doc in mongo_data:
    text = doc.get("text", "")
    lines = text.split("\n")
    in_section = False
    
    for line in lines:
        clean = line.strip()
        if "Capital Improvement Projects (Design)" in clean:
            in_section = True
        elif "(Construction)" in clean or "(Not Started)" in clean:
            in_section = False
        elif in_section and clean and len(clean) > 5:
            skip = False
            bad = ["Updates:", "Schedule:", "To:", "Subject:", "Page", "RECOMMENDED", "DISCUSSION", "Consultant", "Staff is"]
            for term in bad:
                if term in clean:
                    skip = True
                    break
            if not skip and not clean.startswith("(") and not clean.startswith("•") and not clean.isupper():
                design_projects.append(clean)

# Count matching projects
matches = set()
for d in design_projects:
    for f in funding_names:
        d_lower = d.lower()
        f_lower = f.lower()
        if f_lower in d_lower or d_lower in f_lower:
            matches.add(f)
            break

answer = len(matches)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json'}

exec(code, env_args)
