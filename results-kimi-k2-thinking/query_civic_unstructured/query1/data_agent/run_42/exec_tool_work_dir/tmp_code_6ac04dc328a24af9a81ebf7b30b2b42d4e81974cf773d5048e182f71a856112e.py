code = """import json

# Load data
funding_data = json.load(open(var_functions.query_db_110))
mongo_data = json.load(open(var_functions.query_db_104))

# Extract funding project names > $50k
funding_names = []
for f in funding_data:
    funding_names.append(f['Project_Name'])

# Extract design projects
design_projects = []
for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    for line in lines:
        clean = line.strip()
        if 'Capital Improvement Projects (Design)' in clean: in_design = True
        elif '(Construction)' in clean or '(Not Started)' in clean: in_design = False
        elif in_design and clean and len(clean) > 5:
            skip_words = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff', 'Project']
            should_skip = any(word in clean for word in skip_words)
            if not should_skip and not clean.startswith('(') and not clean.startswith('•') and not clean.isupper():
                design_projects.append(clean)

# Find matches
matches = []
for design_name in design_projects:
    for funding_name in funding_names:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches.append(funding_name)
            break

answer = len(matches)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
