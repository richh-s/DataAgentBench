code = """import json

# Get the results from storage
funding_results = 'var_functions.query_db:5'
civic_results = 'var_functions.query_db:2'

# Create funding lookup
funding_projects = {}
for item in funding_results:
    funding_projects[item['Project_Name'].lower()] = int(item['Amount'])

# List of capital design projects identified from the civic documents text
design_projects = [
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
    'Westward Beach Road Repair Project',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Storm Drain Master Plan'
]

# Check which of these have design status in text and > $50,000 funding
count = 0
for project in design_projects:
    proj_lower = project.lower()
    if proj_lower in funding_projects and funding_projects[proj_lower] > 50000:
        count += 1

result = str(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
