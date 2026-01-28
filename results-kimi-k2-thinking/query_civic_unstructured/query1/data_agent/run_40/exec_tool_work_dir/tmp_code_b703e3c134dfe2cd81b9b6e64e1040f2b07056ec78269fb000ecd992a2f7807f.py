code = """import json
import re

# Load funding data
f_path = 'storage/query_result_6.json'
with open(f_path, 'r') as f:
    funding = json.load(f)

# Get project names with funding > $50,000
funded_names = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        funded_names.append(rec['Project_Name'].lower())

# Load civic documents
c_path = 'storage/query_result_10.json'
with open(c_path, 'r') as f:
    civic = json.load(f)

# Extract and match design status capital projects
design_capital_with_funding = 0

for doc in civic:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    if construction_start == -1:
        construction_start = text.find('Capital Improvement Projects (Not Started)', design_start)
    if construction_start == -1:
        construction_start = design_start + 6000
    
    # Extract design section
    design_text = text[design_start:construction_start]
    
    # Find project names (look for lines that could be project names)
    for line in design_text.split('\n'):
        line = line.strip()
        
        # Heuristic: project names are typically longer, not all caps, and not update/schedule lines
        if len(line) > 10 and not line.isupper():
            if not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
                if 'Page' not in line and 'Complete' not in line and 'Advertise' not in line:
                    # Check if this project has high funding
                    line_lower = line.lower()
                    for funded in funded_names:
                        if line_lower in funded or funded in line_lower:
                            design_capital_with_funding += 1
                            break

result = {'count': design_capital_with_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
