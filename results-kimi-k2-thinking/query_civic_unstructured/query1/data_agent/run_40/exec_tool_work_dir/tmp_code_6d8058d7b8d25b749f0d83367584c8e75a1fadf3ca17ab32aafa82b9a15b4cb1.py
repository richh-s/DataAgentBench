code = """import json

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Get projects with funding > $50,000
high_funding_projects = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        name = record['Project_Name'].lower().strip()
        high_funding_projects[name] = amount

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Simple extraction - look for project names in design sections
all_design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        continue
    
    # Get a chunk of text after this header
    section_text = text[start_idx:start_idx+6000]
    lines = section_text.split('\n')
    
    for line in lines[1:]:  # Skip header
        line = line.strip()
        
        # Simple heuristics for project names
        if (len(line) > 15 and not line.startswith('(') and 
            not line.startswith('■') and not line.isupper() and
            'Page' not in line and 'Updates:' not in line and
            'Schedule:' not in line):
            
            all_design_projects.add(line)

# Match projects with funding
match_count = 0
for design_proj in all_design_projects:
    design_lower = design_proj.lower()
    
    for fund_name in high_funding_projects:
        # Check if either string contains the other
        if design_lower in fund_name or fund_name in design_lower:
            match_count += 1
            break

result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
