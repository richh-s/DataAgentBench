code = """import json

# Load funding data
with open(var_functions.query_db:6, 'r') as f:
    funding_records = json.load(f)

# Filter for funding > $50,000
funded_over_50k = {}
for rec in funding_records:
    if int(rec['Amount']) > 50000:
        funded_over_50k[rec['Project_Name'].lower().strip()] = int(rec['Amount'])

# Load civic documents
with open(var_functions.query_db:10, 'r') as f:
    civic_documents = json.load(f)

# Find design capital projects with funding > $50,000
count = 0

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Extract design section (up to next major section)
    next_section = text.find('Capital Improvement Projects (Construction)', design_start)
    if next_section < 0:
        next_section = text.find('Capital Improvement Projects (Not Started)', design_start)
    if next_section < 0:
        next_section = design_start + 6000
    
    design_section = text[design_start:next_section]
    
    # Look for project names and check if they have high funding
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) > 15 and not line.startswith('(') and not line.isupper():
            if all(x not in line for x in ['Updates:', 'Schedule:', 'Page', 'Complete', 'Advertise', 'Begin']):
                # Check if this project has funding > $50,000
                line_lower = line.lower()
                for funded_name in funded_over_50k:
                    if line_lower in funded_name or funded_name in line_lower:
                        count += 1
                        break

print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
