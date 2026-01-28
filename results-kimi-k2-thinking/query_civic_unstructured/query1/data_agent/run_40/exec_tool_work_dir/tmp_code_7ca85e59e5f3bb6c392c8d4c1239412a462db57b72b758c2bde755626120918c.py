code = """import json

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Filter projects with funding > $50,000
funded_projects = {}
for rec in funding_records:
    amt = int(rec['Amount'])
    if amt > 50000:
        name = rec['Project_Name'].lower().strip()
        funded_projects[name] = amt

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital project names
design_capital_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section and extract lines
    start_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    start_pos = text.find(start_marker)
    if start_pos >= 0:
        end_pos = text.find(construction_marker, start_pos)
        if end_pos < 0:
            end_pos = start_pos + 6000
        
        section = text[start_pos:end_pos]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('(') and not line.isupper():
                if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                    design_capital_projects.add(line)

# Count matches between design projects and funded projects
match_count = 0
for design in design_capital_projects:
    d_lower = design.lower()
    for funded in funded_projects:
        if d_lower in funded or funded in d_lower:
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': match_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
