code = """import json

# Get file paths from stored results
funding_path = var_functions.query_db_110
mongo_path = var_functions.query_db_104

# Read funding data (projects > $50,000)
funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Read mongo data (documents with 'design')
mongo_file = open(mongo_path, 'r')
mongo_data = json.load(mongo_file)
mongo_file.close()

# Get funding project names
funding_names = []
for rec in funding_data:
    funding_names.append(rec['Project_Name'])

# Extract design projects from mongo docs
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
        elif in_design_section and clean and len(clean) > 5:
            skip_patterns = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 'Project is']
            should_skip = any(pattern in clean for pattern in skip_patterns)
            if not should_skip and not clean.startswith('(') and not clean.startswith('•') and not clean.isupper():
                design_projects.append(clean)

# Find matching projects
matches = 0
seen = set()
for design_name in design_projects:
    for funding_name in funding_names:
        name_lower = funding_name.lower()
        design_lower = design_name.lower()
        if name_lower in design_lower or design_lower in name_lower:
            if funding_name not in seen:
                matches += 1
                seen.add(funding_name)
            break

result_json = json.dumps(matches)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
