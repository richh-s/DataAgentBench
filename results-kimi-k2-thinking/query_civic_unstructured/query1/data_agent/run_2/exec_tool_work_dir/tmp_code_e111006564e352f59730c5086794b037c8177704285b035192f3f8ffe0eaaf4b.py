code = """import json

# Get data from storage
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

# Build funding lookup - map project names to amounts
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower()
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount

# Extract names of capital projects that are in design phase
design_project_names = set()

# Based on the text preview, these are likely capital design projects
likely_names = [
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
    'PCH at Trancas Canyon Road Right Turn Lane'
]

# Check if these projects appear in design context
for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if document has a design section
    if 'capital improvement projects (design)' in text:
        for name in likely_names:
            if name.lower() in text:
                design_project_names.add(name.lower())

# Also extract from the text more systematically
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    start_marker = 'Capital Improvement Projects (Design)'
    if start_marker in text:
        start = text.index(start_marker)
        # Look for next major heading
        end = len(text)
        for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
            pos = text.find(marker, start + 50)
            if pos > start and pos < end:
                end = pos
        
        section = text[start:end]
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) > 15:
                # Skip lines that are obviously not project names
                skip_words = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'cid:']
                if not any(word in line for word in skip_words):
                    if line[0].isalpha():
                        project_name = line.strip('•- ').strip()
                        if project_name and ' ' in project_name:
                            design_project_names.add(project_name.lower())

# Count matching projects with funding > $50,000
count = 0
matched = []

for design_project in design_project_names:
    for funding_project in funding_lookup:
        if design_project == funding_project or design_project in funding_project or funding_project in design_project:
            amount = funding_lookup[funding_project]
            if amount > 50000:
                count += 1
                matched.append(design_project)
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
