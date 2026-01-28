code = """import json

# Get data from storage
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name'].lower()
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount

# Extract capital design projects from text
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find where design projects section starts
    design_start = -1
    if 'Capital Improvement Projects (Design)' in text:
        design_start = text.index('Capital Improvement Projects (Design)')
    elif 'Capital Improvement Projects (Design' in text:
        design_start = text.index('Capital Improvement Projects (Design')
    
    if design_start == -1:
        continue
    
    # Find where next section starts
    next_section_start = len(text)
    possible_next = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    for header in possible_next:
        pos = text.find(header, design_start + 50)
        if pos > design_start and pos < next_section_start:
            next_section_start = pos
    
    # Extract the design section text
    design_section = text[design_start:next_section_start]
    
    # Split into lines and find project names
    lines = design_section.split('\n')
    in_project_list = False
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines, update lines, schedule lines
        if not line or len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('cid:'):
            continue
        if 'Updates' in line or 'Project Schedule' in line:
            continue
        if line.startswith('Complete Design') or line.startswith('Advertise') or line.startswith('Begin Construction'):
            continue
        if 'Complete Design' in line or 'Advertise:' in line or 'Begin Construction:' in line:
            continue
        
        # Likely a project name if it's a relatively long line and not a bullet point detail
        if len(line) > 15 and not line.startswith('*') and not line.startswith('-'):
            # Remove common markers
            clean_name = line.strip('•- ').strip()
            if clean_name and clean_name not in capital_design_projects:
                capital_design_projects.append(clean_name.lower())

# Match capital design projects with funding
matches = []
for design_proj in capital_design_projects:
    for fund_proj in funding_lookup:
        # Check for exact or partial matches
        if design_proj == fund_proj or design_proj in fund_proj or fund_proj in design_proj:
            amount = funding_lookup[fund_proj]
            if amount > 50000:
                matches.append(design_proj)
                break

# Count unique matches
result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
