code = """import json

# Get data
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

# Create funding lookup
funding = {}
for item in funding_data:
    funding[item['Project_Name'].lower()] = int(item['Amount'])

# Manually identified capital design projects from the preview text
capital_design_projects = [
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
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Westward Beach Road Repair Project'
]

# Check each document for these projects in design context
design_projects_found = set()

for doc in civic_docs:
    text_upper = doc.get('text', '')
    text_lower = text_upper.lower()
    
    # Check if this document has a design section
    if 'capital improvement projects (design)' in text_lower:
        for project in capital_design_projects:
            if project.lower() in text_lower:
                design_projects_found.add(project.lower())

# Count matches with funding > $50,000
count = 0
for project in design_projects_found:
    for fund_project in funding:
        if project in fund_project or fund_project in project:
            if funding[fund_project] > 50000:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(str(result))

# Also try a different approach - check ALL projects in funding against documents
all_matches = []
for fund_project, amount in funding.items():
    if amount > 50000:
        for doc in civic_docs:
            text = doc.get('text', '').lower()
            # Check if project has design status
            if fund_project in text:
                # Now check if in design section
                design_start = text.find('capital improvement projects (design)')
                if design_start > 0:
                    next_section = text.find('capital improvement projects (construction)', design_start)
                    if next_section == -1:
                        next_section = len(text)
                    design_section = text[design_start:next_section]
                    if fund_project in design_section:
                        all_matches.append(fund_project)
                        break

result2 = {'count_using_all_funding': len(set(all_matches))}
print('__RESULT__:')
print(str(result2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
