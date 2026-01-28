code = """import json

# Load funding data
with open(var_functions.query_db_6) as f:
    funding_data = json.load(f)

# Load mongo data
with open(var_functions.query_db_2) as f:
    mongo_docs = json.load(f)

# Get project names with funding > $50,000
funding_names = [f['Project_Name'] for f in funding_data if f['Amount'] > 50000]

# Extract design projects from mongo documents
design_projects = []
for doc in mongo_docs:
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
            if 'Updates:' not in clean and 'Schedule:' not in clean and not clean.startswith('(') and not clean.startswith('•'):
                if 'Consultant' not in clean and 'Staff' not in clean and 'Project' not in clean[:15]:
                    if not clean.isupper():
                        design_projects.append(clean)

# Find matching projects
matches = 0
for fname in funding_names:
    found = False
    for dname in design_projects:
        if fname.lower() in dname.lower() or dname.lower() in fname.lower():
            found = True
            break
    if found:
        matches = matches + 1

# Return the final count
result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json'}

exec(code, env_args)
