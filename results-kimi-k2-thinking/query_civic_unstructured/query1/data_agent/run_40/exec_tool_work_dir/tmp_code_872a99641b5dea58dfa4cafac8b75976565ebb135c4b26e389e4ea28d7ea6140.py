code = """import json

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    all_funding = json.load(f)

# Get projects with funding > $50,000
high_funding = {}
for record in all_funding:
    amount = int(record['Amount'])
    if amount > 50000:
        name = record['Project_Name'].lower().strip()
        high_funding[name] = amount

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital projects from documents
all_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we entered the Design section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        # Check if we left the Design section
        if in_design_section and ('Capital Improvement Projects (Construction)' in line or 
                                  'Capital Improvement Projects (Not Started)' in line or
                                  'DISASTER RECOVERY' in line):
            break
            
        # If we're in the design section, extract project names
        if in_design_section and line:
            # Skip markers and schedule lines
            if (not line.startswith('(') and 
                not line.startswith('■') and 
                not line.startswith('□') and 
                not line.startswith('•') and
                'Updates:' not in line and
                'Schedule:' not in line and
                'Complete Design:' not in line and
                'Advertise:' not in line and
                'Begin Construction:' not in line and
                len(line) > 10 and
                not line.isupper() and
                'Page' not in line):
                
                all_design_projects.add(line)

# Match projects with funding data
matched = []
for design_proj in all_design_projects:
    design_lower = design_proj.lower()
    
    for fund_name in high_funding:
        if design_lower in fund_name or fund_name in design_lower:
            matched.append(design_proj)
            break

# Deduplicate and count
count = len(set(matched))

result = {'count': count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
