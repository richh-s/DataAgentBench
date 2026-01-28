code = """import json

# Load the data
with open(locals()['var_functions.query_db:40'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Extract design project names mentioned in the design section
design_projects = [
    'PCH Median Improvements Project',
    'Westward Beach Road Drainage Improvements Project', 
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study'
]

# Match with funding data > 50,000
matched = []
for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        project_name = funding['Project_Name']
        # Remove suffixes like (FEMA Project) to get base name
        if '(' in project_name:
            base_name = project_name.split('(')[0].strip()
        else:
            base_name = project_name
        
        # Check if matches a design project
        if base_name in design_projects:
            matched.append(base_name)

result = json.dumps({'count': len(set(matched))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
