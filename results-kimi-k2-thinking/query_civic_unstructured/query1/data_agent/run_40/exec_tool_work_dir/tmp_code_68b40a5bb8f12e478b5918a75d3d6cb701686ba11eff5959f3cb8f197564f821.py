code = """import json

# Load all funding records
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create a dictionary of projects with funding > $50,000
high_funding = {}
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        proj_name = record['Project_Name'].lower().strip()
        high_funding[proj_name] = {
            'amount': amount,
            'original_name': record['Project_Name']
        }

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital projects
all_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Find where design section ends
    construction_pos = text.find('Capital Improvement Projects (Construction)', design_start)
    not_started_pos = text.find('Capital Improvement Projects (Not Started)', design_start)
    
    # Determine end position
    end_pos = construction_pos
    if end_pos < 0 or (not_started_pos > 0 and not_started_pos < end_pos):
        end_pos = not_started_pos
    if end_pos < 0:
        end_pos = design_start + 8000  # Reasonable section length
    
    # Extract design section text
    design_section = text[design_start:end_pos]
    
    # Split into lines and process
    lines = design_section.split('\n')
    in_project_list = True
    
    for line in lines:
        line = line.strip()
        
        # Skip header line
        if 'Capital Improvement Projects (Design)' in line:
            continue
        
        # Skip empty lines and markers
        if not line:
            continue
        
        if (line.startswith('(') or line.startswith('■') or 
            line.startswith('□') or line.startswith('•')):
            continue
        
        # Skip update/schedule lines
        if ('Updates:' in line or 'Schedule:' in line or 
            line.startswith('Complete') or line.startswith('Advertise') or 
            line.startswith('Begin')):
            continue
        
        # Skip page numbers and headers
        if line.isupper() or 'Page' in line:
            continue
        
        # Valid project names are typically longer
        if len(line) > 10:
            all_design_projects.add(line)

# Match projects with funding
matched = 0
for design_proj in all_design_projects:
    design_lower = design_proj.lower()
    
    # Check against funded projects
    for fund_name in high_funding:
        # Match if one contains the other
        if (design_lower in fund_name or fund_name in design_lower):
            matched += 1
            break

result = {'count': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
