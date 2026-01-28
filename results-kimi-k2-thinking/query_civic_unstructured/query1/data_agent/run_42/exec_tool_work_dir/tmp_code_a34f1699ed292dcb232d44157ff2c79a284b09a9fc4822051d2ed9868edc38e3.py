code = """import json

# Load funding data
funding_file = open('var_functions.query_db_6', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load mongo data  
mongo_file = open('var_functions.query_db_2', 'r')
mongo_data = json.load(mongo_file)
mongo_file.close()

# Get project names with funding > $50,000
funding_names = []
for rec in funding_data:
    if rec['Amount'] > 50000:
        funding_names.append(rec['Project_Name'])

# Extract design projects from mongo documents
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

# Print result
answer = json.dumps(matches)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
