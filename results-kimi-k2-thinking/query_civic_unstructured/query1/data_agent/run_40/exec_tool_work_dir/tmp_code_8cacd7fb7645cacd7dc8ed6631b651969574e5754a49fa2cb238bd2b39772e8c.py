code = """import json

# Load funding data
f_path = var_functions.query_db:6
with open(f_path, 'r') as f:
    funding = json.load(f)

# Filter for funding > $50,000
high_funding = {}
for rec in funding:
    amount = int(rec['Amount'])
    if amount > 50000:
        name = rec['Project_Name'].lower().strip()
        high_funding[name] = amount

# Load civic documents
c_path = var_functions.query_db:10
with open(c_path, 'r') as f:
    docs = json.load(f)

# Extract design capital projects
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
        if in_design_section:
            if any(marker in line for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'DISASTER RECOVERY']):
                break
            if len(line) > 10 and not line.startswith('(') and not line.isupper():
                if all(x not in line for x in ['Updates:', 'Schedule:', 'Page', 'Complete', 'Advertise', 'Begin']):
                    design_projects.add(line)

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for fund_name in high_funding:
        if proj_lower in fund_name or fund_name in proj_lower:
            count += 1
            break

result = str(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
