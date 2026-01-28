code = """import json

# Access stored results dynamically
funding_result = list(filter(lambda x: 'query_db' in x and '190' in x, dir()))
mongo_result = list(filter(lambda x: 'query_db' in x and '182' in x, dir()))

if funding_result and mongo_result:
    funding_key = funding_result[0]
    mongo_key = mongo_result[0]
    
    funding_path = locals()[funding_key]
    mongo_path = locals()[mongo_key]
    
    funding_file = open(funding_path, 'r')
    funding_data = json.load(funding_file)
    funding_file.close()
    
    mongo_file = open(mongo_path, 'r')
    mongo_data = json.load(mongo_file)
    mongo_file.close()
    
    # Get funding project names
    funding_names = []
    for f in funding_data:
        funding_names.append(f['Project_Name'])
    
    # Extract design projects from mongo
    design_projects = []
    for doc in mongo_data:
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
                skip = False
                bad_keywords = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page']
                for kw in bad_keywords:
                    if kw in clean:
                        skip = True
                        break
                if not skip and not clean.startswith('(') and not clean.startswith('•'):
                    if not clean.isupper() and 'Consultant' not in clean and 'Staff' not in clean:
                        design_projects.append(clean)
    
    # Find matches
    matches = set()
    for design in design_projects:
        for fund in funding_names:
            design_lower = design.lower()
            fund_lower = fund.lower()
            if design_lower in fund_lower or fund_lower in design_lower:
                matches.add(fund)
                break
    
    answer = len(matches)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json', 'var_functions.query_db:162': 'file_storage/functions.query_db:162.json', 'var_functions.query_db:182': 'file_storage/functions.query_db:182.json', 'var_functions.execute_python:186': 0, 'var_functions.query_db:188': 'file_storage/functions.query_db:188.json', 'var_functions.query_db:190': 'file_storage/functions.query_db:190.json'}

exec(code, env_args)
