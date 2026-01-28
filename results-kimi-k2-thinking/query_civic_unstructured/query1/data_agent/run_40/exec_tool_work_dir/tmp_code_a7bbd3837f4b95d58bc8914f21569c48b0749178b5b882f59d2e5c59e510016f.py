code = """import json

# Load all funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    all_funding = json.load(f)

# Get funding amounts > $50,000
high_funding = {}
for record in all_funding:
    amount = int(record['Amount'])
    if amount > 50000:
        proj_name = record['Project_Name'].lower().strip()
        high_funding[proj_name] = amount

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital projects from all documents
all_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design section manually
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        # Find where design section ends
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start > 0:
            design_section = text[design_start:construction_start]
        else:
            not_started_start = text.find('Capital Improvement Projects (Not Started)', design_start)
            if not_started_start > 0:
                design_section = text[design_start:not_started_start]
            else:
                design_section = text[design_start:design_start + 5000]
        
        # Extract project names from this section
        lines = design_section.split('\n')
        in_updates = False
        
        for line in lines[1:]:  # Skip the header line
            line = line.strip()
            
            # Skip empty lines and markers
            if not line:
                continue
                
            # Skip update/schedule markers
            if line.startswith('(') or line.startswith('■') or line.startswith('□') or line.startswith('•'):
                continue
                
            if 'Updates:' in line or 'Schedule:' in line:
                in_updates = True
                continue
                
            if in_updates and (':' in line or line.startswith('Complete') or line.startswith('Advertise') or line.startswith('Begin')):
                continue
                
            # Skip if all uppercase (likely a section header)
            if line.isupper():
                continue
                
            # Skip page numbers
            if 'Page' in line and 'of' in line:
                continue
                
            # Valid project name should be reasonably long
            if len(line) > 10:
                all_design_projects.add(line)
                in_updates = False

# Match design projects with high funding
matched_count = 0
matched_names = []

for design_proj in all_design_projects:
    design_lower = design_proj.lower()
    
    # Try to match with any funded project
    for fund_name in high_funding:
        # Check if one is substring of the other
        if design_lower in fund_name or fund_name in design_lower:
            matched_count += 1
            matched_names.append(design_proj)
            break

result = {'count': matched_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
