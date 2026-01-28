code = """import json

# Get the file paths from variables
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:10']

# Load data from files
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build set of projects with funding > $50,000
high_funding_projects = set()
for rec in funding_records:
    if int(rec['Amount']) > 50000:
        high_funding_projects.add(rec['Project_Name'].lower().strip())

# Extract design capital projects and count matches
matched_count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of design section
    construction_pos = text.find('Capital Improvement Projects (Construction)', design_start)
    not_started_pos = text.find('Capital Improvement Projects (Not Started)', design_start)
    
    end_pos = construction_pos if construction_pos != -1 else not_started_pos
    if end_pos == -1:
        end_pos = design_start + 6000
    
    # Extract section
    section = text[design_start:end_pos]
    
    # Check each line
    for line in section.split('\n'):
        line = line.strip()
        
        # Heuristic: project names are typically longer, not all caps, not starting with (
        if len(line) > 10 and not line.startswith('(') and not line.isupper():
            if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                line_lower = line.lower()
                
                # Check if funded
                for funded in high_funding_projects:
                    if funded in line_lower or line_lower in funded:
                        matched_count += 1
                        break

result = json.dumps({'count': matched_count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
