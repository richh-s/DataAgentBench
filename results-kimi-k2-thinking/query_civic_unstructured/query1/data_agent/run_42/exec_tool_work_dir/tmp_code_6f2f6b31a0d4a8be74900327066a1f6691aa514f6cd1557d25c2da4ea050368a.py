code = """import json

print('=== STARTING ANALYSIS ===')

# Access the stored results - these are file paths
funding_file = var_functions.query_db_110
mongo_file = var_functions.query_db_104

print('Funding file:', funding_file)
print('Mongo file:', mongo_file)

# Load funding data (projects > $50k)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funding_count = len(funding_data)
print('Funding records loaded:', funding_count)

# Load mongo data
with open(mongo_file, 'r') as f:
    mongo_data = json.load(f)

mongo_count = len(mongo_data)
print('Mongo documents loaded:', mongo_count)

# Get unique project names from funding
funding_names = []
for f in funding_data:
    funding_names.append(f['Project_Name'])

# Extract design projects from mongo
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
            if len(clean) > 5:
                # Skip non-project lines
                skip_patterns = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 'Project is']
                should_skip = any(pattern in clean for pattern in skip_patterns)
                if not should_skip and not clean.startswith('(') and not clean.startswith('•') and not clean.isupper():
                    project_name = clean.strip('•- ')
                    design_projects.append(project_name)

print('Design projects found:', len(design_projects))

# Find matching projects
matches = []
for design_name in design_projects:
    for funding_name in funding_names:
        design_lower = design_name.lower()
        funding_lower = funding_name.lower()
        if funding_lower in design_lower or design_lower in funding_lower:
            matches.append(funding_name)
            break

answer = len(matches)
print('FINAL ANSWER:', answer)

__RESULT__:
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
