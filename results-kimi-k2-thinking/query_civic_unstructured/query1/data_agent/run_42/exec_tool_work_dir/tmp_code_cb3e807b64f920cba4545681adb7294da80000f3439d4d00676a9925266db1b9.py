code = """import json

# Get file paths from stored results
funding_path = var_functions.query_db_110
mongo_path = var_functions.query_db_104

# Read data files
with open(funding_path) as f:
    funding_data = json.load(f)

with open(mongo_path) as f:
    mongo_data = json.load(f)

# Count matching projects
match_count = 0

# Extract design project names
design_project_names = set()
for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif '(Construction)' in line or '(Not Started)' in line:
            in_design = False
        elif in_design and line and len(line) > 5:
            skip_terms = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will']
            should_skip = any(term in line for term in skip_terms)
            if not should_skip and not line.startswith('(') and not line.startswith('•') and not line.isupper():
                clean_name = line.strip('•- ')
                design_project_names.add(clean_name)

# Get funding project names with funding > $50,000  
funding_project_names = [f['Project_Name'] for f in funding_data]

# Find matches
for design_name in design_project_names:
    for funding_name in funding_project_names:
        if (funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower()) and len(funding_name) > 0:
            match_count += 1
            break

result = match_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
