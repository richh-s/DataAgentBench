code = """import json

# Read the funding data
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Create lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name.lower()] = amount

# Read civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects - simpler approach
capital_design_projects = []

# Common capital design project names found in the documents
design_project_names = [
    'Clover Heights Storm Drain',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'PCH Median Improvements Project',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study',
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    'Westward Beach Road Drainage Improvements Project',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane'
]

# Check if these appear in the text and have design status
for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this document discusses design projects
    if 'capital improvement projects (design)' in text.lower():
        for name in design_project_names:
            if name.lower() in text:
                capital_design_projects.append(name.lower())

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))

# Match with funding data
count = 0
matched = []
for project_name in capital_design_projects:
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        if amount > 50000:
            count += 1
            matched.append(project_name)

# Also check for partial matches for variations
for project_name in capital_design_projects:
    if project_name not in matched:
        for funding_name in funding_lookup:
            if project_name in funding_name or funding_name in project_name:
                amount = funding_lookup[funding_name]
                if amount > 50000:
                    count += 1
                    matched.append(project_name)
                    break

result = {
    'count': count,
    'matched_projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
