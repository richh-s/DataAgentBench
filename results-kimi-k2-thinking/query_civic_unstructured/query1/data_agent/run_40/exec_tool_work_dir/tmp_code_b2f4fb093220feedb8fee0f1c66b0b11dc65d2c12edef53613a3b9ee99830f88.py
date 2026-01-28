code = """import json

# Load all funding records
f_path = var_functions.query_db:6
with open(f_path) as f:
    funding = json.load(f)

# Filter for funding > 50000
high_funding_names = set()
for rec in funding:
    if int(rec['Amount']) > 50000:
        high_funding_names.add(rec['Project_Name'].lower().strip())

# Load civic documents  
c_path = var_functions.query_db:10
with open(c_path) as f:
    docs = json.load(f)

# Find design capital projects
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    
    # Find design section start
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Find design section end
    end1 = text.find('Capital Improvement Projects (Construction)', start)
    end2 = text.find('Capital Improvement Projects (Not Started)', start)
    end3 = text.find('DISASTER RECOVERY', start)
    
    end = end1
    if end == -1 or (end2 != -1 and end2 < end):
        end = end2
    if end == -1 or (end3 != -1 and end3 < end):
        end = end3
    if end == -1:
        end = start + 6000
    
    section = text[start:end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        # Skip markers and short lines
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('\u25a0') or line.startswith('\u2022'):
            continue
        if line.isupper() or 'Page' in line:
            continue
        if any(x in line for x in ['Updates:', 'Schedule:', 'Complete', 'Advertise', 'Begin']):
            continue
        
        design_projects.add(line)

# Count matches
matches = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for fund in high_funding_names:
        if proj_lower in fund or fund in proj_lower:
            matches += 1
            break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
