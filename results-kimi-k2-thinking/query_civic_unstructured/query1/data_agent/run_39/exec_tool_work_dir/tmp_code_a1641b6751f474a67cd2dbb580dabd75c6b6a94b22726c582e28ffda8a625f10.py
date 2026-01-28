code = """import json

# Load data from files
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Based on the document preview, extract design projects directly
design_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project", 
    "Westward Beach Road Repair Project",
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drainage Improvements",
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

# Filter for capital type (exclude disaster projects)
capital_design_projects = []
for project in design_projects:
    if not any(x in project.lower() for x in ['fema', 'caloes', 'caljpia', 'disaster']):
        capital_design_projects.append(project)

# Match with funding > $50,000
matching_projects = []
for project_name in capital_design_projects:
    for fund in funding_data:
        if fund['Project_Name'] == project_name and int(fund['Amount']) > 50000:
            matching_projects.append({
                'project': project_name,
                'amount': int(fund['Amount'])
            })

result = {
    'capital_design_projects': capital_design_projects,
    'count_design_projects': len(capital_design_projects),
    'matching_projects': matching_projects,
    'matching_count': len(matching_projects),
    'total_funding_matched': sum(p['amount'] for p in matching_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
