code = """import json
import re

# Load funding data
funding_var = locals()['var_functions.query_db:4']
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

# Load civic documents
civic_var = locals()['var_functions.query_db:11']
if isinstance(civic_var, str) and civic_var.endswith('.json'):
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

print(f"Funding records loaded: {len(funding_data)}")
print(f"Civic documents loaded: {len(civic_docs)}")

# Create a mapping from funding data
funding_map = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[name] = {
        'Amount': amount,
        'Funding_Source': record['Funding_Source']
    }

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for "Capital Improvement Projects (Design)" section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
        
        # Exit design section when we hit another major section
        if in_design_section and ('Capital Improvement Projects' in line and 'Construction' in line):
            break
        if in_design_section and ('Capital Improvement Projects' in line and 'Not Started' in line):
            break
            
        # If we're in the design section, extract project names
        if in_design_section and line:
            # Skip empty lines, headers, and descriptive text
            if (len(line) < 5 or 
                line.startswith('Page') or 
                line.startswith('Agenda Item') or
                'Updates:' in line or
                'Project Schedule:' in line or
                'Complete Design:' in line or
                'Advertise:' in line or
                'Begin Construction:' in line):
                continue
            
            # Skip uppercase header lines that are all caps
            if line.isupper() and len(line.split()) <= 4:
                continue
                
            # Clean up the project name
            project_name = line.strip('â€¢â€‘- ').strip()
            
            # Most project names are reasonable length and start with capital letters
            if 5 < len(project_name) < 100 and project_name[0].isupper():
                # Check if this project has funding
                if project_name in funding_map:
                    amount = funding_map[project_name]['Amount']
                    if amount > 50000:
                        design_capital_projects.append({
                            'Project_Name': project_name,
                            'Amount': amount,
                            'Funding_Source': funding_map[project_name]['Funding_Source']
                        })

print(f"Capital projects with design status and funding > $50,000: {len(design_capital_projects)}")

# Remove duplicates
distinct_projects = []
seen_names = set()
for proj in design_capital_projects:
    if proj['Project_Name'] not in seen_names:
        distinct_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print(f"Distinct capital projects: {len(distinct_projects)}")

# Display some examples
for proj in distinct_projects[:10]:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']}")

# Return the count
result = len(distinct_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
