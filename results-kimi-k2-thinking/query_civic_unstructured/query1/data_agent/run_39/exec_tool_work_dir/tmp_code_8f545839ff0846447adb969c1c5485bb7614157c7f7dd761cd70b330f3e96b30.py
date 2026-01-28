code = """import json

# Get file paths from locals
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:2']

# Load funding data
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Design status projects from civic docs (capital type, not disaster)
# These are from the "Capital Improvement Projects (Design)" section
design_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project",
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drain",
    "Latigo Canyon Road Retaining Wall Repair Project",
    "Storm Drain Master Plan",
    "Permanent Skate Park",
    "PCH at Trancas Canyon Road Right Turn Lane",
    "Outdoor Warning Signs",
    "Malibu Bluffs Park South Walkway Repairs",
    "Trancas Canyon Park Playground",
    "Malibu Canyon Road Traffic Study"
]

# Match with funding records > $50,000
matches = []
for project in design_projects:
    for record in funding:
        if record['Project_Name'] == project and int(record['Amount']) > 50000:
            matches.append(project)

print('__RESULT__:')
print(json.dumps({
    'design_projects': design_projects,
    'matching_projects': matches,
    'count': len(matches)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
