code = """import json

# Access the stored results using different approach
results = locals()
funding_path = results.get('var_functions.query_db_6')
mongo_path = results.get('var_functions.query_db_2')

# Debug: Print what we found
print('Funding path found:', funding_path is not None)
print('Mongo path found:', mongo_path is not None)

if funding_path and mongo_path:
    # Load data
    with open(funding_path) as f:
        funding_data = json.load(f)
    
    with open(mongo_path) as f:
        mongo_docs = json.load(f)
    
    # Get projects with funding > $50,000
    funding_names = [f['Project_Name'] for f in funding_data if f['Amount'] > 50000]
    
    # Extract design projects from mongo
    design_projects = []
    for doc in mongo_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        in_design = False
        
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects (Design)' in line:
                in_design = True
            elif '(Construction)' in line or '(Not Started)' in line:
                in_design = False
            elif in_design and line and not line.startswith('(') and not line.startswith('•'):
                if len(line) > 5 and 'Updates:' not in line and 'Schedule:' not in line:
                    if 'Consultant' not in line and 'Staff' not in line:
                        if not line.isupper():
                            design_projects.append(line)
    
    # Find matches
    matches = []
    for design_name in design_projects:
        for funding_name in funding_names:
            if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
                matches.append(funding_name)
                break
    
    result = len(matches)
    print('Result:', result)
else:
    result = 0
    print('Data files not accessible')

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json'}

exec(code, env_args)
