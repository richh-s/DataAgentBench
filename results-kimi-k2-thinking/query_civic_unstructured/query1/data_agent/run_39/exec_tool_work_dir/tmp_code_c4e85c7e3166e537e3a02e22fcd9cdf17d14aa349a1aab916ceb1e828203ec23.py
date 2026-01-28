code = """import json

# Load the funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Manual extraction of capital projects in design status from the document preview
design_section_projects = [
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
    "Malibu Canyon Road Traffic Study"
]

# Match with funding records > $50,000
matching_projects = []
for project_name in design_section_projects:
    for fund_record in funding_data:
        if fund_record['Project_Name'] == project_name and int(fund_record['Amount']) > 50000:
            matching_projects.append({
                'project': project_name,
                'amount': int(fund_record['Amount'])
            })

# Also check additional projects that might be in design from other sections
additional_design_candidates = [
    "PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH",
    "Kanan Dume Biofilter",
    "City Traffic Signals Backup Power"
]

for project_name in additional_design_candidates:
    for fund_record in funding_data:
        if fund_record['Project_Name'] == project_name and int(fund_record['Amount']) > 50000:
            # Check if not already in matching_projects
            if not any(p['project'] == project_name for p in matching_projects):
                matching_projects.append({
                    'project': project_name,
                    'amount': int(fund_record['Amount'])
                })

result = {
    'matching_projects': matching_projects,
    'count': len(matching_projects),
    'total_funding': sum(p['amount'] for p in matching_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
