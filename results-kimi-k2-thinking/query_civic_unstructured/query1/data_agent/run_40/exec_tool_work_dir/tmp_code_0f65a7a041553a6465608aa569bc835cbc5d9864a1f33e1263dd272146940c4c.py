code = """import json

# Access the tool results storage
tool_result_funding = var_functions.query_db_6
tool_result_civic = var_functions.query_db_10

# Load the data
with open(tool_result_funding, 'r') as f:
    funding_data = json.load(f)

with open(tool_result_civic, 'r') as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
funded_projects = set()
for rec in funding_data:
    if int(rec['Amount']) > 50000:
        funded_projects.add(rec['Project_Name'].lower().strip())

# Count design capital projects with high funding
count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_section = text.find('Capital Improvement Projects (Design)')
    if design_section == -1:
        continue
    
    # Find where the section ends
    construction_section = text.find('Capital Improvement Projects (Construction)', design_section)
    if construction_section == -1:
        construction_section = text.find('Capital Improvement Projects (Not Started)', design_section)
    if construction_section == -1:
        construction_section = design_section + 6000
    
    # Extract this section
    section_text = text[design_section:construction_section]
    lines = section_text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Filter for project names
        if len(line) > 10 and not line.startswith('(') and not line.isupper():
            if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                line_lower = line.lower()
                # Check if this project has high funding
                for funded in funded_projects:
                    if funded in line_lower or line_lower in funded:
                        count += 1
                        break

result_json = json.dumps({'count': count})
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
