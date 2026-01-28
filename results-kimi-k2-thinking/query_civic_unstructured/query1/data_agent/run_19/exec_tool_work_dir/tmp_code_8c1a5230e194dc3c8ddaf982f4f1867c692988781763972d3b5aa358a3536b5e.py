code = """import json

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

print('Records loaded - Funding:', len(funding_data), 'Civic docs:', len(civic_docs))

# Create funding lookup
funding_lookup = {}
for rec in funding_data:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[name] = amount

# Process civic documents
projects_in_design = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we're in the design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            design_section = True
            continue
        
        # Exit design section
        if design_section and 'Capital Improvement Projects' in line and 'Construction' in line:
            break
        if design_section and 'Capital Improvement Projects' in line and 'Not Started' in line:
            break
        
        # Extract project names
        if design_section and line and 5 < len(line) < 100:
            proj_name = line.strip('â€¢â€‘- ').strip()
            if proj_name in funding_lookup:
                amount = funding_lookup[proj_name]
                if amount > 50000:
                    projects_in_design.add(proj_name)

count = len(projects_in_design)
print('Design capital projects > $50K:', count)

for proj in sorted(projects_in_design)[:5]:
    print(' -', proj, ': $' + str(funding_lookup[proj]))

import json as js
print('__RESULT__:')
print(js.dumps(count))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
