code = """import json

funding_path = var_functions.query_db_138
mongo_path = var_functions.query_db_104

with open(funding_path) as f:
    funding = json.load(f)

with open(mongo_path) as f:
    mongo = json.load(f)

funding_names = [item['Project_Name'] for item in funding]

design_projects = []
for doc in mongo:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean:
            in_design = True
        elif '(Construction)' in clean or '(Not Started)' in clean:
            in_design = False
        elif in_design and clean and len(clean) > 5:
            bad_terms = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is']
            skip = False
            for term in bad_terms:
                if term in clean:
                    skip = True
                    break
            if not skip and not clean.startswith('(') and not clean.startswith('•') and not clean.isupper():
                design_projects.append(clean)

matches = set()
for design_name in design_projects:
    for funding_name in funding_names:
        d_lower = design_name.lower()
        f_lower = funding_name.lower()
        if f_lower in d_lower or d_lower in f_lower:
            matches.add(funding_name)
            break

result = len(matches)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json'}

exec(code, env_args)
