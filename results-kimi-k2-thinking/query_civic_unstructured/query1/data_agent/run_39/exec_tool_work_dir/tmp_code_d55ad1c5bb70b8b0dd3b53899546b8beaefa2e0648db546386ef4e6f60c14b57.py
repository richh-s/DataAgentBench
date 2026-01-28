code = """import json

# Load full funding data
funding_path = var_functions.query_db:0
with open(funding_path, 'r') as f:
    funding_all = json.load(f)

# Identify capital projects in design status from document preview
# These were manually extracted from the civic document text
capital_design_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project", 
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drain",
    "Latigo Canyon Road Retaining Wall Repair Project",
    "Storm Drain Master Plan",
    "Civic Center Water Treatment Facility Phase 2",
    "Permanent Skate Park",
    "PCH at Trancas Canyon Road Right Turn Lane",
    "Outdoor Warning Signs",
    "Malibu Bluffs Park South Walkway Repairs",
    "Trancas Canyon Park Playground",
    "Malibu Canyon Road Traffic Study",
    "PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH",
    "Kanan Dume Biofilter",
    "City Traffic Signals Backup Power"
]

# Filter funding records: project must be in design list, amount > $50,000
matching_projects = []
for fund in funding_all:
    proj_name = fund['Project_Name']
    amount = int(fund['Amount'])
    if proj_name in capital_design_projects and amount > 50000:
        matching_projects.append({
            'Project_Name': proj_name,
            'Amount': amount,
            'Funding_Source': fund['Funding_Source']
        })

# Prepare result
result = {
    'matching_projects': sorted(matching_projects, key=lambda x: x['Project_Name']),
    'count': len(matching_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
